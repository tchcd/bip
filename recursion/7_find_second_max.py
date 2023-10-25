def initial_find_second_max(array: list):
	start_idx = 2
	if len(array) < start_idx:
		return None
	if array[0] >= array[1]:
		first = array[0]
		second = array[1]
	else:
		first = array[1]
		second = array[0]

	return find_second_max(array, start_idx, second, first)


def find_second_max(
		array: list, idx: int, second_max: int | float, first_max: int | float
	):
	if idx >= len(array):
		return second_max

	if array[idx] >= first_max:
		second_max = first_max
		first_max = array[idx]

	if second_max <= array[idx] < first_max:
		second_max = array[idx]

	return find_second_max(array, idx + 1, second_max, first_max)


if __name__ == '__main__':
	print(initial_find_second_max([1, 3, 2, 5]))
	print(initial_find_second_max([0, 3]))
	print(initial_find_second_max([0]))
	print(initial_find_second_max([1, 2, 3, 4, 5]))
	print(initial_find_second_max([-100, -5, -10]))
