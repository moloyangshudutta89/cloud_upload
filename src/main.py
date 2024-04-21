from lib import aws, gcs, common
import os
from dotenv import load_dotenv

load_dotenv()

def main():

    directory = os.getenv('DIRECTORY_PATH')
    if directory:
        print(f"Reading files from directory: {directory}")
        files = common.list_files(directory)
        cloud_upload = common.fileType(files)
        if len(cloud_upload["aws"]) > 0:
            if aws.upload_to_aws(cloud_upload["aws"]):
                print("AWS files were successfully uploaded!!")
        if len(cloud_upload["gcc"]) > 0:   
            if gcs.upload_to_bucket(cloud_upload["gcc"]):
                print("GCS files were successfully uploaded!!")
    else:
        print("DIRECTORY_PATH environment variable not set.")

if __name__ == "__main__":
    main()