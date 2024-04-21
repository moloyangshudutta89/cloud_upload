import boto3, os
from botocore.exceptions import NoCredentialsError
from multiprocessing.pool import ThreadPool

def upload_to_aws(local_files):
    s3 = boto3.client('s3', aws_access_key_id=os.getenv('AWS_ACCESS_KEY'),
                      aws_secret_access_key=os.getenv('AWS_SECRET_KEY'))
    bucket = os.getenv('AWS_BUCKET_NAME')

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
    except NoCredentialsError:
        print("Credentials not available")
        return False

    return True