import argparse
import logging

from elmer.model.azure.auth import AuthService
from elmer.model.azure.blob import BlobService
import asyncio

def entrypoint(args=None):
    """
    Main callable for entry.
    """

    logger = logging.getLogger()
    logger.setLevel(logging.INFO)

    parser = argparse.ArgumentParser()
    parser.add_argument("--debug", "-D", action="store_true")

    commands = {}

    copy_from_container =""
    copy_to_container =""
    blob_name =""
    blob_url = ""


    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)

    authService = AuthService()
    credential = authService.managed_identity()
    # credential = authService.vs_code()

    blobService = BlobService(credential,copy_from_container, copy_to_container, blob_name, blob_url)
    blob = loop.run_until_complete(blobService.get_blob())

    loop.close()

    return None