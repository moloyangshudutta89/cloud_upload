import os
from google.cloud import storage
import threading

def upload_to_bucket(files, gcs_bucket, gcs_credential):

    if not os.path.isfile(gcs_credential):
        print("GCS Credentials file not found!!")
        return False
    
    if not files:
        print("Files list is empty for GCS!!")
        return False
    
    threads = []
    for local_file in files:
        try:
            thread = threading.Thread(target=upload_to_gcs, args=(gcs_bucket,gcs_credential,local_file))
            threads.append(thread)
            thread.start()
        except FileNotFoundError:
            print("The file was not found")
            return False
        except Exception as e:
            print(e)
            return False
        
    for thread in threads:
        thread.join()

    return True

def upload_to_gcs(gcs_bucket,gcs_credential,local_file):
    bucket_name = gcs_bucket
    storage_client = storage.Client.from_service_account_json(gcs_credential)
    bucket = storage_client.get_bucket(bucket_name)
    file_name = os.path.basename(local_file)
    blob_name = os.path.join('', file_name).replace('\\', '/')
    blob = bucket.blob(blob_name)
    blob.upload_from_filename(local_file)
    # print(blob.public_url)