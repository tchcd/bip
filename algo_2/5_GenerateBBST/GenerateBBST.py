def get_elements(array_left, array_right, res):
	l = len(array_left) // 2
	r = len(array_right) // 2
	if l == 0:
		res.append(array_left[0])
	else:
		res.append(array_left[l])

	if r == 0:
		res.append(array_right[0])
	else:
		res.append(array_right[r])

	if l > 0:
		get_elements(array_left[:l], array_left[l + 1:], res)

	if r > 0:
		get_elements(array_right[:r], array_right[r + 1:], res)

	return res


def GenerateBBSTArray(a):
	a = sorted(a)
	length = len(a)
	res = []
	if length == 1:
		return [a[0]]

	idx = length // 2
	res.append(a[idx])

	left = a[:idx]
	right = a[idx + 1:]

	return get_elements(left, right, res)
