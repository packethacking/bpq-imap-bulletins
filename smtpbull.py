import os

from twisted.cred.portal import IRealm
from twisted.internet import defer
from twisted.mail import smtp
from twisted.mail.imap4 import LOGINCredentials, PLAINCredentials
from zope.interface import implementer

import swagger_client
from structlog import get_logger
from checker import RECIEVED_CREDENTIALS

logger = get_logger()

@implementer(smtp.IMessage)
class BPQMessage:
    def __init__(self, callsign=None, user=None):
        self.callsign = callsign
        self.user = user
        self.lines = []
        self.logger = logger.bind(callsign=self.callsign)
        self.logger.info("Creating BPQMessage")

        configuration = swagger_client.Configuration()
        configuration.host = f"http://{os.environ['bpqapi']}:8080"
        configuration.username = self.callsign
        configuration.password = RECIEVED_CREDENTIALS[self.callsign.decode()]
        self.client = swagger_client.ApiClient(configuration)
        self.api = swagger_client.MailApi(self.client)

    def lineReceived(self, line):
        self.lines.append(line)

    def eomReceived(self):
        print("New message received:")
        print(b"\n".join(self.lines))
        self.lines = None
        self.api.mail_send_post(body=b"\n".join(self.lines), to=self.user.dest.addrstr)
        return defer.succeed(None)

    def connectionLost(self):
        # There was an error, throw away the stored lines
        self.lines = None


@implementer(smtp.IMessageDelivery)
class BPQMessageDelivery:

    def __init__(self, callsign=None):
        self.callsign = callsign

    def receivedHeader(self, helo, origin, recipients):
        self.helo = helo
        self.origin = origin
        self.recipients = recipients
        return b"Received: BPQMessageDelivery"

    def validateFrom(self, helo, origin):
        # All addresses are accepted
        return origin

    def validateTo(self, user):
        # Only messages directed to the "console" user are accepted.
        # if user.dest.local == "console":
        #    return lambda: ConsoleMessage()
        # raise smtp.SMTPBadRcpt(user)
        return lambda: BPQMessage(callsign=self.callsign, user=user)


@implementer(IRealm)
class SimpleRealm:

    def requestAvatar(self, avatarId, mind, *interfaces):
        # if we are authenticating a IMessageDelivery
        if smtp.IMessageDelivery in interfaces:
            # a tuple of the implemented interface, an instance implementing it and a logout callable
            return (
                smtp.IMessageDelivery,
                BPQMessageDelivery(callsign=avatarId),
                lambda: None,
            )
        raise NotImplementedError()


class BPQSMTPFactory(smtp.SMTPFactory):
    protocol = smtp.ESMTP
    # portal = None

    def __init__(self, *a, **kw):
        smtp.SMTPFactory.__init__(self, *a, **kw)
        self.delivery = BPQMessageDelivery()

    def buildProtocol(self, addr):
        p = smtp.SMTPFactory.buildProtocol(self, addr)
        p.delivery = self.delivery
        p.challengers = {b"LOGIN": LOGINCredentials, b"PLAIN": PLAINCredentials}
        # p.portal = self.portal
        p.factory = self
        return p
