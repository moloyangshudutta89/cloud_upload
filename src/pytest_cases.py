import pytest
from classes.Upload import Upload
from lib import aws, gcs, common

@pytest.fixture
def upload():
    return Upload('C:/Users/clb89/OneDrive/Desktop/my_projects/file',{})

def test_read_from_dir(upload):
    assert upload.read_from_dir() == "ValueError: Credentials required!!"

def test_list_files():
    assert common.list_files('') == []

def test_fileType():
    assert common.fileType([],[],[]) == {"aws":[],"gcc":[]}

def test_upload_to_aws():
    assert aws.upload_to_aws('','','','') == False

def test_upload_to_bucket():
    assert gcs.upload_to_bucket('','','') == False