def only_even(input_list: list):
	if not input_list:
		return
	first_num = input_list.pop(0)
	if not first_num % 2:
		print(first_num)
	only_even(input_list)


if __name__ == '__main__':
	only_even([1, 2, 3, 4, 5, 6])
	only_even([-5, -4, -3, -2, -1])
	only_even([-3, -2, -1, 0, 1, 2, 3, 4, 5])
