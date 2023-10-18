def only_even_idx(input_list: list):
	len_indexes = len(input_list) - 1
	def inner(i):
		if i > len_indexes:
			return
		if not i % 2:
			print(input_list[i])
		inner(i + 1)
	inner(0)


if __name__ == '__main__':
	only_even_idx([1, 2, 3, 4, 5, 6])					# 1, 3, 5
	only_even_idx([-5, -4, -3, -2, -1])					# -5, -3, -1
	only_even_idx([-3, -2, -1, 0, 1, 2, 3, 4, 5])		# -3, -1, 1, 3, 5
