def only_even_idx(input_list: list, idx=0):
	if idx >= len(input_list):
		return
	if not idx % 2:
		print(input_list[idx])
	only_even_idx(input_list, idx + 1)


if __name__ == '__main__':
	only_even_idx([1, 2, 3, 4, 5, 6])					# 1, 3, 5
	only_even_idx([-5, -4, -3, -2, -1])					# -5, -3, -1
	only_even_idx([-3, -2, -1, 0, 1, 2, 3, 4, 5])		# -3, -1, 1, 3, 5
