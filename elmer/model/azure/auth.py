import os

class AuthService(object):

    def __init__(self) -> None:
        
        pass

    def managed_identity(self):
        from azure.identity.aio import DefaultAzureCredential
        self.credential = DefaultAzureCredential(exclude_interactive_browser_credential=False)
        return self.credential

    def client_secret(self):
        from azure.identity.aio import ClientSecretCredential
        return None

    def vs_code(self):
        from azure.identity.aio import VisualStudioCodeCredential
        self.credential = VisualStudioCodeCredential()
        return self.credential

    def chained_token(self):
        from azure.identity.aio import ChainedTokenCredential
        return None

    def env_credentials(self):
        from azure.identity.aio import EnvironmentCredential
        return None
    