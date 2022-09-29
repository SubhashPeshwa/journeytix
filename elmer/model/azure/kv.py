from azure.keyvault.secrets.aio import SecretClient
from azure.identity.aio import DefaultAzureCredential

class KvService(object):
    """
    """

    def __init__(self, kv_name, kv_key, kv_recipient, client_id) -> None:
        """
        """
        
        self.kv_name = kv_name
        self.kv_key = kv_key
        self.kv_recipient = kv_recipient
        # Add different auth methods, what if this was deployed on AWS Lambda?
        self.credential = DefaultAzureCredential(managed_identity_client_id=client_id)
        kv_uri = f"https://{kv_name}.vault.azure.net"
        self.kv_client = SecretClient(vault_url=kv_uri, credential=self.credential)

        pass

    async def get_key(self):
        """
        """

        print(f"Retrieving your secret.")

        stream = await self.kv_client.get_secret(self.kv_key)
        await self.kv_client.close()
        return stream.value