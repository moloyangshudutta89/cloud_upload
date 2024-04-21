import boto3, os
from botocore.exceptions import NoCredentialsError

def upload_to_aws(local_files, aws_access_key, aws_secret_key, aws_bucket_name):

    if not local_files:
        print("Files list is empty for AWS!!")
        return False

    s3 = boto3.client('s3', aws_access_key_id=aws_access_key,
                      aws_secret_access_key=aws_secret_key)
    bucket = aws_bucket_name

    object_prefix = ''

    try:
        for local_file in local_files:
            try:
                file_name = os.path.basename(local_file)
                object_key = os.path.join(object_prefix, file_name).replace('\\', '/')
                s3.upload_file(local_file, bucket, object_key)
            except FileNotFoundError:
                print("The file was not found")
                return False
            except Exception as e:
                print(e)
                return False
    except NoCredentialsError:
        print("Credentials not available")
        return False

    return True