import os


def init_find_all_files(dir):
    list_of_files = []
    find_all_files(dir, list_of_files)
    return list_of_files


def find_all_files(dir, list_of_files):
    for item in os.listdir(dir):
        item_path = os.path.join(dir, item)
        if os.path.isfile(item_path):
            filename = os.path.basename(item_path)
            list_of_files.append(filename)
        elif os.path.isdir(item_path):
            find_all_files(item_path, list_of_files)
