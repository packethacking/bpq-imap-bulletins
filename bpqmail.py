from imapbull import TestServerIMAPFactory, TestServerRealm
from smtpbull import BPQSMTPFactory, SimpleRealm
from twisted.cred import portal

from checker import CredentialsNonChecker


def run(imap_port=2143, smtp_port=2025):
    from twisted.internet import reactor

    imapFactory = TestServerIMAPFactory()
    smtpFactory = BPQSMTPFactory()

    imapFactory.portal = portal.Portal(TestServerRealm())
    imapFactory.portal.registerChecker(CredentialsNonChecker())
    # imapFactory.portal.registerChecker(checkers.AllowAnonymousAccess())

    smtpFactory.portal = portal.Portal(SimpleRealm())
    smtpFactory.portal.registerChecker(CredentialsNonChecker())

    imap = reactor.listenTCP(imap_port, imapFactory)
    smtp = reactor.listenTCP(smtp_port, smtpFactory)

    reactor.run()


if __name__ == "__main__":
    run()
