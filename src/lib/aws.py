import boto3, os
from botocore.exceptions import NoCredentialsError
import threading

def upload_to_aws(local_files, aws_access_key, aws_secret_key, aws_bucket_name):

    if not local_files:
        print("Files list is empty for AWS!!")
        return False

    s3 = boto3.client('s3', aws_access_key_id=aws_access_key,
                      aws_secret_access_key=aws_secret_key)
    bucket = aws_bucket_name

    object_prefix = ''
    threads = []
    try:
        for local_file in local_files:
            try:
                file_name = os.path.basename(local_file)
                object_key = os.path.join(object_prefix, file_name).replace('\\', '/')
                ###Creating new thread for each file upload to run in parallel####
                thread = threading.Thread(target=s3.upload_file, args=(local_file, bucket, object_key))
                threads.append(thread)
                thread.start()
            except FileNotFoundError:
                print("The file was not found")
                return False
            except Exception as e:
                print(e)
                return False
    except NoCredentialsError:
        print("Credentials not available")
        return False
    
    for thread in threads:
        thread.join()

    return True