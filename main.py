import click
import logging
from google.cloud import storage

logging.basicConfig(level=logging.DEBUG)


@click.command()

@click.argument("file_names", nargs=-1)
def upload_files(file_names):
    client = storage.Client()

    bucket_name = "cli-file-uploader-dump"
    bucket = client.get_bucket(bucket_name)

    try:
        blobs = bucket.list_blobs()
        for blob in blobs:
            print(blob.name)

        for file_name in file_names:
            print(f"Uploading file {file_name}")

    except Exception as e:
        logging.exception("Error Uploading files: %s", str(e))
        print("Error uploading files: %s" % str(e))

if __name__ == '__main__':
    upload_files()



