import os
from google.cloud import storage

def upload_to_bucket(files):
    """ Upload data to a bucket"""
    
    bucket_name = os.getenv('GCS_BUCKET')
    # Explicitly use service account credentials by specifying the private key
    # file.
    storage_client = storage.Client.from_service_account_json(os.getenv('GCS_CREDENTIALS'))

    bucket = storage_client.get_bucket(bucket_name)

    for local_file in files:
        try:
            file_name = os.path.basename(local_file)
            blob_name = os.path.join('', file_name).replace('\\', '/')
            blob = bucket.blob(blob_name)
            blob.upload_from_filename(local_file)
            # print(blob.public_url)
        except FileNotFoundError:
            print("The file was not found")
            return False
        except Exception as e:
            print(e)

    return True