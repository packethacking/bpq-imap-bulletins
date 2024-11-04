import os

from twisted.cred import portal, credentials
from twisted.internet import protocol, defer, task
from twisted.mail import imap4
from zope.interface import implementer

import swagger_client
from structlog import get_logger

from inbox import MemoryIMAPMailbox


RECIEVED_CREDENTIALS = {}
MAILBOXES = {}
PERONAL_MAILBOXES = {}

logger = get_logger()


@implementer(imap4.IMailbox)
@implementer(imap4.INamespacePresenter)
class IMAPUserAccount:

    def __init__(self, callsign):
        self.callsign = callsign.decode()
        self.logger = logger.bind(callsign=self.callsign)
        self.logger.info("Creating IMAPUserAccount")
        configuration = swagger_client.Configuration()
        configuration.host = f"http://{os.environ['bpqapi']}:8080"
        configuration.username = self.callsign
        configuration.password = RECIEVED_CREDENTIALS[self.callsign]
        self.client = swagger_client.ApiClient(configuration)
        self.api = swagger_client.MailApi(self.client)

        self.latest_personal = 0

        bulls = self.api.mail_bulletins_get()
        self.logger.info(f"Loaded {len(bulls)} bulletins for {self.callsign}")

        self.latest_bull = max([x.id for x in bulls])

        categories = {x.to for x in bulls}
        for category in categories:
            if category in MAILBOXES:
                continue
            MAILBOXES[category] = MemoryIMAPMailbox(
                [x for x in bulls if x.to == category],
                self.api,
                category,
                self.callsign,
            )

        if not "INBOX" in MAILBOXES:
            self.logger.info("Creating INBOX")
            personal = self.api.mail_personal_get()
            self.latest_personal = max([x.id for x in personal])
            self.logger.info(f"Loaded {len(personal)} personal messages")
            MAILBOXES["INBOX"] = MemoryIMAPMailbox(
                personal, self.api, "INBOX", self.callsign
            )

        loop = task.LoopingCall(self.updateMailboxes)
        loop.start(60)

    def updateMailboxes(self):
        self.logger.info("Updating mailboxes")
        bulls = self.api.mail_bulletins_get()
        new_bull = max([x.id for x in bulls])
        self.logger.info(f"Loaded {len(bulls)} bulletins")
        if new_bull > self.latest_bull:
            categories = {x.to for x in bulls}
            for category in categories:
                if category not in MAILBOXES:
                    MAILBOXES[category] = MemoryIMAPMailbox(
                        [x for x in bulls if x.to == category],
                        self.api,
                        category,
                        self.callsign,
                    )
                MAILBOXES[category].update_mailbox(
                    [x for x in bulls if x.to == category and x.id > self.latest_bull]
                )
        self.latest_bull = new_bull

        personal = self.api.mail_personal_get()
        self.logger.info(f"Loaded {len(personal)} personal messages")
        new_personal = max([x.id for x in personal])
        if new_personal > self.latest_personal:
            MAILBOXES["INBOX"].update_mailbox(
                [x for x in personal if x.id > self.latest_personal]
            )
        self.latest_personal = new_personal

    def getPersonalNamespaces(self):
        return [[b"", b"/"]]

    def getSharedNamespaces(self):
        return None

    def getOtherNamespaces(self):
        return None

    def getUserNamespaces(self):
        # INamespacePresenter.getUserNamespaces
        return None

    def listMailboxes(self, ref, wildcard):
        "only support one folder"

        # We don't support nested folders, so ignore wildcard
        if wildcard and wildcard != "%" and wildcard != "*":
            return []

        return [(key, value) for key, value in MAILBOXES.items()]

    def select(self, path, rw=True):
        "return the same mailbox for every path"
        print(f"Selecting {path}")
        return MAILBOXES.get(path)

    def create(self, path):
        "nothing to create"
        pass

    def delete(self, path):
        "delete the mailbox at path"
        raise imap4.MailboxException("Permission denied.")

    def rename(self, oldname, newname):
        "rename a mailbox"
        pass

    def isSubscribed(self, path):
        "return a true value if user is subscribed to the mailbox"
        return True

    def subscribe(self, path):
        return True

    def unsubscribe(self, path):
        return True


@implementer(portal.IRealm)
class IMAPServerProtocol(imap4.IMAP4Server):
    "Subclass of imap4.IMAP4Server that adds debugging."

    def capabilities(self):
        """Remove IDLE from the default selection of capabilities."""
        cap = {b"AUTH": list(self.challengers.keys())}
        cap[b"NAMESPACE"] = None
        return cap

    def lineReceived(self, line):
        logger.info(f"Received: {line}")
        super().lineReceived(line)

    def sendLine(self, line):
        imap4.IMAP4Server.sendLine(self, line)

    def do_SEARCH(self, tag, charset, query, uid=0):

        imap4.IMAP4Server.do_SEARCH(self, tag, charset, query, uid)

    def _singleSearchStep(self, query, msgId, msg, lastSequenceId, lastMessageId):

        for i, x in enumerate(query):
            if (
                isinstance(x, bytes)
                and x not in self._requiresLastMessageInfo
                and len(query) > 1
            ):
                query[i] = x.decode()
        return super()._singleSearchStep(
            query, msgId, msg, lastSequenceId, lastMessageId
        )

    select_SEARCH = (
        do_SEARCH,
        imap4.IMAP4Server.opt_charset,
        imap4.IMAP4Server.arg_searchkeys,
    )


class TestServerRealm(object):
    avatarInterfaces = {
        imap4.IAccount: IMAPUserAccount,
    }

    def requestAvatar(self, avatarId, mind, *interfaces):
        for requestedInterface in interfaces:
            if requestedInterface in self.avatarInterfaces:
                avatarClass = self.avatarInterfaces[requestedInterface]
                avatar = avatarClass(callsign=avatarId)
                # null logout function: take no arguments and do nothing
                logout = lambda: None
                return defer.succeed((requestedInterface, avatar, logout))

        # none of the requested interfaces was supported
        raise KeyError("None of the requested interfaces is supported")


class TestServerIMAPFactory(protocol.Factory):
    protocol = IMAPServerProtocol
    portal = None  # placeholder
    noisy = False

    def buildProtocol(self, address):
        p = self.protocol()
        # self.portal will be set up already "magically"
        p.portal = self.portal
        p.factory = self
        return p


class CredentialsNonChecker(object):
    credentialInterfaces = (
        credentials.IUsernamePassword,
        credentials.IUsernameHashedPassword,
    )

    def requestAvatarId(self, credentials):
        """automatically validate *any* user"""
        RECIEVED_CREDENTIALS[credentials.username.decode()] = (
            credentials.password.decode()
        )
        return credentials.username


def run(imap_port=2143):
    from twisted.internet import reactor

    imapFactory = TestServerIMAPFactory()

    imapFactory.portal = portal.Portal(TestServerRealm())
    imapFactory.portal.registerChecker(CredentialsNonChecker())
    # imapFactory.portal.registerChecker(checkers.AllowAnonymousAccess())

    imap = reactor.listenTCP(imap_port, imapFactory)

    reactor.run()


if __name__ == "__main__":
    run()
