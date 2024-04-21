import os, pathlib

def fileType(files):
    if len(files) == 0:
        return {}
    fileType_dict = {"aws":[],"gcc":[]}
    for i in files:
        if pathlib.Path(i).suffix in os.getenv('FILE_TYPES_AWS'):
            fileType_dict["aws"].append(i)
        elif pathlib.Path(i).suffix in os.getenv('FILE_TYPES_GCC'):
            fileType_dict["gcc"].append(i)

    return fileType_dict

def list_files(directory):
    filesList = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            filesList.append(file_path)
    return filesList