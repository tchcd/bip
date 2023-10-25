def print_even_idx(array: list):
	start_idx = 0
	print_if_even(array, start_idx)


def print_if_even(array: list, idx: int):
	if idx == len(array):
		return

	if not idx % 2:
		print(array[idx])
	print_if_even(array, idx + 1)


if __name__ == '__main__':
	print_even_idx([1, 2, 3, 4, 5, 6])
	print_even_idx([-5, -4, -3, -2, -1])
	print_even_idx([-3, -2, -1, 0, 1, 2, 3, 4, 5])



