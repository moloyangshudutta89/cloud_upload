from lib import aws, gcs, common
import os

class Upload:

    cred_dict = {
                "FILE_TYPES_AWS":[".jpg", ".png", ".svg", ".webp", ".mp3", ".mp4", ".mpeg4", ".wmv", ".3gp", ".webm"], 
                "FILE_TYPES_GCC":[".doc", ".docx", ".csv", ".pdf"], 
                "AWS_ACCESS_KEY":"",
                "AWS_SECRET_KEY":"", 
                "AWS_BUCKET_NAME":"cloudupload", 
                "GCS_BUCKET": "gc-cloud-upload", 
                "GCS_CREDENTIALS":"gcs.json"
                }

    @staticmethod
    def read_from_dir(directory):

        if directory:
            print(f"Reading files from directory: {directory}")
            files = common.list_files(directory)
            if len(files) > 0:
                cloud_upload = common.fileType(files, Upload.cred_dict["FILE_TYPES_AWS"], Upload.cred_dict["FILE_TYPES_GCC"])
                if len(cloud_upload["aws"]) > 0:
                    if aws.upload_to_aws(cloud_upload["aws"], Upload.cred_dict['AWS_ACCESS_KEY'], Upload.cred_dict['AWS_SECRET_KEY'], Upload.cred_dict['AWS_BUCKET_NAME']):
                        print("AWS files were successfully uploaded!!")
                    else:
                        print("AWS files upload failed!!")
                if len(cloud_upload["gcc"]) > 0:   
                    if gcs.upload_to_bucket(cloud_upload["gcc"], Upload.cred_dict['GCS_BUCKET'], Upload.cred_dict['GCS_CREDENTIALS']):
                        print("GCS files were successfully uploaded!!")
                    else:
                        print("GCS files upload failed!!")
            else:
                print("Directory is empty!!")
        else:
            print("Directory path is empty!!")