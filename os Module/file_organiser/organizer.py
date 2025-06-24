import os
from .utils import createfile_if_not_exist, move_file

def organize_folder(path):
    for file in os.listdir(path):
        file_path = os.path.join(path, file)
        if os.path.isfile(file_path):
            ext = file.split('.')[-1]
            folder = os.path.join(path, ext.upper() + "_Files")
            createfile_if_not_exist(folder)
            move_file(file_path, folder)
