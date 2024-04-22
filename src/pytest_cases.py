import pytest
from classes.Upload import Upload
from lib import aws, gcs, common

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

@pytest.fixture
def upload():
    return Upload('C:/Users/clb89/OneDrive/Desktop/my_projects/files',cred_dict)

def test_read_from_dir(upload):
    assert upload.read_from_dir() == print("Directory is empty!!")

@pytest.fixture
def upload1():
    return Upload('',cred_dict)

def test_read_from_dir1(upload1):
    assert upload1.read_from_dir() == print("Directory path is empty!!")

def test_list_files():
    assert common.list_files('') == []

def test_fileType():
    assert common.fileType([],[],[]) == {"aws":[],"gcc":[]}

def test_upload_to_aws():
    assert aws.upload_to_aws('','','','') == False

def test_upload_to_bucket():
    assert gcs.upload_to_bucket('','','') == False