from GenerateBBST import GenerateBBSTArray


def test_GenerateBBSTArray():
	arr = [1, 4, 7, 5, 3, 9, 8]
	assert GenerateBBSTArray(arr) == [5, 3, 8, 1, 4, 7, 9]


def test_GenerateBBSTArray_one():
	arr = [1]
	assert GenerateBBSTArray(arr) == [1]


def test_GenerateBBSTArray_three():
	arr = [3, 2, 1]
	assert GenerateBBSTArray(arr) == [2, 1, 3]
