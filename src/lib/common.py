import os, pathlib

def fileType(files,aws_files,gcs_files):
    fileType_dict = {"aws":[],"gcc":[]}
    if not files:
        return fileType_dict
    
    for i in files:
        if pathlib.Path(i).suffix in aws_files:
            fileType_dict["aws"].append(i)
        elif pathlib.Path(i).suffix in gcs_files:
            fileType_dict["gcc"].append(i)

    return fileType_dict

def list_files(directory):
    if directory:
        filesList = []
        for root, dirs, files in os.walk(directory):
            for file in files:
                file_path = os.path.join(root, file)
                filesList.append(file_path)
        return filesList
    else:
        return []