import os
import shutil

def createfile_if_not_exist(folder_path):
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

def move_file(file_path, destination_path):
    shutil.move(file_path, destination_path)