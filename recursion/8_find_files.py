import os


def init_find_all_files(dir):
	list_of_files = []
	find_all_files(dir, 0, list_of_files)
	return list_of_files


def find_all_files(cur_dir, file_idx, list_of_files):
	items = os.listdir(cur_dir)
	if file_idx >= len(items):
		return

	item = os.path.join(cur_dir, items[file_idx])
	if os.path.isfile(item):
		filename = os.path.basename(item)
		list_of_files.append(filename)
		find_all_files(cur_dir, file_idx + 1, list_of_files)

	elif os.path.isdir(item):
		find_all_files(item, 0, list_of_files)
