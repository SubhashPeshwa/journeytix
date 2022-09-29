# from azure.storage.blob import BlockBlobService
from azure.storage.blob.aio import BlobServiceClient
from azure.identity.aio import DefaultAzureCredential
import io
import shutil

class BlobService(object):
    """
    """

    def __init__(self, credential, copy_from_container, copy_to_container, blob_name, blob_url) -> None:
        self.copy_from_container = copy_from_container
        self.copy_to_container = copy_to_container
        self.blob_name = blob_name
        self.credential = credential
        self.blob_url = blob_url
        self.blob_service_client = BlobServiceClient(account_url=blob_url, credential=self.credential)
        
        pass

    async def get_blob(self):
        """
        """
        print("Downloading file from container using managed identity")
        async with self.blob_service_client as blob_service_client, self.credential:
            
            blob_client = blob_service_client.get_blob_client(
                container=self.copy_from_container, blob=self.blob_name
            )
        
            stream = await blob_client.download_blob()
            print("Download complete using managed identity")
            return_data = io.StringIO((await stream.readall()).decode("utf-8"))
            with open("./data/{}_raw.{}".format(self.blob_name.split('.')[0],self.blob_name.split('.')[1]),'w',encoding = 'utf-8') as f:
                return_data.seek(0)
                shutil.copyfileobj(return_data, f)

            await blob_client.close()

            return None

    async def write_blob(self):
        """
        """
        print("Uploading file to container using managed identity")
        async with self.blob_service_client as blob_service_client, self.credential:
            
            blob_client = blob_service_client.get_blob_client(
                container=self.copy_to_container, blob=self.blob_name
            )

            with open("./data/{}_raw.{}".format(self.blob_name.split('.')[0],self.blob_name.split('.')[1]), "rb") as data:
                print("Uploaded complete using managed identity")
                await blob_client.upload_blob(data, overwrite=True)

            await blob_client.close()

            return None

