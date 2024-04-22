from lib import aws, gcs, common

class Upload:

    cred_dict = {}

    def __init__(self, directory, cred):
        if not cred:
            raise ValueError("Credentials required!!")
        Upload.cred_dict = cred
        self.directory = directory

    def read_from_dir(self):

        if self.directory:
            print(f"Reading files from directory: {self.directory}")
            files = common.list_files(self.directory)
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