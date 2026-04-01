import os
def find_files(path):
    return os.listdir(path)
def filter_by_extension(files, ext):
    return [f for f in files if f.endswith(ext)]
