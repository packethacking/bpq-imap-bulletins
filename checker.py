from twisted.cred import credentials

RECIEVED_CREDENTIALS = {}

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



