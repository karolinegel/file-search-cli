import os
def find_files(path):
    return os.listdir(path)
def filter_by_extension(files, ext):
    return [f for f in files if f.endswith(ext)]
def find_files_recursive(path):
    result = []
    for root, dirs, files in os.walk(path):
        for file in files:
            result.append(os.path.join(root, file))
    return result
if __name__ == "__main__":
    files = find_files(".")
    print(files)
