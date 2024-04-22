from classes.Upload import Upload

# cred_dict = {
#             "FILE_TYPES_AWS":[".jpg", ".png", ".svg", ".webp", ".mp3", ".mp4", ".mpeg4", ".wmv", ".3gp", ".webm"], 
#             "FILE_TYPES_GCC":[".doc", ".docx", ".csv", ".pdf"], 
#             "AWS_ACCESS_KEY":"",
#             "AWS_SECRET_KEY":"", 
#             "AWS_BUCKET_NAME":"cloudupload", 
#             "GCS_BUCKET": "gc-cloud-upload", 
#             "GCS_CREDENTIALS":"gcs.json"
#             }

cred_dict = {}

path = "C:/Users/clb89/OneDrive/Desktop/my_projects/files"
upload = Upload(path, cred_dict)
upload.read_from_dir()