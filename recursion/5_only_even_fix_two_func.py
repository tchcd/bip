def print_even_nums(array: list):
	start_idx = 0
	print_if_even(array, start_idx)


def print_if_even(array: list, idx: int):
	if idx == len(array):
		return

	val = array[idx]
	if not val % 2:
		print(val)
	print_if_even(array, idx + 1)


if __name__ == '__main__':
	print_even_nums([1, 2, 3, 4, 5, 6])
	print_even_nums([-5, -4, -3, -2, -1])
	print_even_nums([-3, -2, -1, 0, 1, 2, 3, 4, 5])
