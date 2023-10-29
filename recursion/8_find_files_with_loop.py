import os


def find_all_files(dir):
    files = []
    for item in os.listdir(dir):
        item_path = os.path.join(dir, item)
        if os.path.isfile(item_path):
            filename = os.path.basename(item_path)
            files.append(filename)
        elif os.path.isdir(item_path):
            files.extend(find_all_files(item_path))
    return files
