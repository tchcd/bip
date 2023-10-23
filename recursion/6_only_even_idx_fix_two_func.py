def print_even_idx(array: list):
	print_if_even(array, 0)


def print_if_even(array: list, idx: int):
	if idx == len(array):
		return

	if not idx % 2:
		print(array[idx])
	print_if_even(array, idx + 1)


if __name__ == '__main__':
	print_even_idx([1, 2, 3, 4, 5, 6])					# 1, 3, 5
	print_even_idx([-5, -4, -3, -2, -1])					# -5, -3, -1
	print_even_idx([-3, -2, -1, 0, 1, 2, 3, 4, 5])		# -3, -1, 1, 3, 5



