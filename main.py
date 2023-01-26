__winc_id__ = "ae539110d03e49ea8738fd413ac44ba8"
__human_name__ = "files"


import os
import shutil 
import zipfile

folder = os.getcwd()
folder_cache = folder + "/cache"
zip_file = folder + "/data.zip"

def clean_cache():
    folder_check = os.listdir(folder)
    if "cache" in folder_check:
        shutil.rmtree(folder_cache)
    os.mkdir(folder_cache)
    return

def cache_zip(zip_file, folder_cache):
    with zipfile.ZipFile(zip_file, 'r',) as zip_ref:
        zip_ref.extractall(folder_cache)
    return 

def cached_files():
    list_files = []
    with os.scandir(folder_cache) as list_of_entries:
        for entry in list_of_entries:
            if entry.is_file():
                result = os.path.abspath(entry)
                list_files.append(result)     
    return list_files

def find_password(list):
    for x in list:
        f = open(x, "r")
        text = f.read()
        if "password" in text:
            list = text.split("\n")
            for i in list:
                if "password" in i:
                    return i[i.find(" ")+1:]
        f.close()
find_password(cached_files())