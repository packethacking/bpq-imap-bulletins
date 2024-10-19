import os

from twisted.cred import portal, credentials, checkers
from twisted.internet import protocol, defer
from twisted.mail import imap4
from zope.interface import implementer

import swagger_client

from inbox import MemoryIMAPMailbox


RECIEVED_CREDENTIALS = {}
MAILBOXES = {}
PERONAL_MAILBOXES = {}


@implementer(imap4.IMailbox)
@implementer(imap4.INamespacePresenter)
class IMAPUserAccount:


    def __init__(self, callsign):
        self.callsign   = callsign.decode()
        configuration = swagger_client.Configuration()
        configuration.host = f"http://{os.environ['bpqapi']}:8080"
        configuration.username = self.callsign
        configuration.password = RECIEVED_CREDENTIALS[self.callsign]
        self.client = swagger_client.ApiClient(configuration)
        self.api = swagger_client.MailApi(self.client)

        bulls = self.api.mail_bulletins_get()

        categories = {x.to for x in bulls}
        # TODO: Hacked to limit to 3 folders
        for category in categories:
            #if category != "ASTRO":
            #    continue
            if category in MAILBOXES:
                continue
            MAILBOXES[category] = MemoryIMAPMailbox(
                [x for x in bulls if x.to == category],
                self.api,
                category
            )

        if not "INBOX" in MAILBOXES:
            personal = self.api.mail_personal_get()
            MAILBOXES["INBOX"] = MemoryIMAPMailbox(
                personal,
                self.api,
                "INBOX"
            )

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

    def lineReceived(self, line):
        print("Line received: %s" % line)
        imap4.IMAP4Server.lineReceived(self, line)

    def sendLine(self, line):
        print("Line sent: %s" % line)
        imap4.IMAP4Server.sendLine(self, line)

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
    credentialInterfaces = (credentials.IUsernamePassword,
                            credentials.IUsernameHashedPassword)

    def requestAvatarId(self, credentials):
        """automatically validate *any* user"""
        RECIEVED_CREDENTIALS[credentials.username.decode()] = credentials.password.decode()
        return credentials.username


def run(imap_port=2143):
    from twisted.internet import reactor
    imapFactory = TestServerIMAPFactory()

    imapFactory.portal = portal.Portal(TestServerRealm())
    imapFactory.portal.registerChecker(CredentialsNonChecker())
    #imapFactory.portal.registerChecker(checkers.AllowAnonymousAccess())

    imap = reactor.listenTCP(imap_port, imapFactory)

    reactor.run()

if __name__ == '__main__':
    run()
