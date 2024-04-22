cloud_upload

This module can be included as a package in other applications for uploading files to both AWS and GCS

setup:-
1. git clone https://github.com/moloyangshudutta89/cloud_upload.git / using pip install -r cloud_upload(package not uploaded)
2. For using the application create an object of the class Upload after importing the class in your application such as "from classes.Upload import Upload"
3. Initialize the class constructor with the credentials dictionary. Credentials dictionary format is given in the run.py
4. Mention the path to directory while creating the class object.
5. The application will upload multiple files in parallel by using thread for each files.
6. Please run "pytest pytest_cases.py" for running the test cases.