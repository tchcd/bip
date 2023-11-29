from GenerateBBST import GenerateBBSTArray


def test_GenerateBBSTArray():
	arr = [1, 4, 7, 5, 3, 9, 8] # [1,3,4,5,7,8,9]
	assert GenerateBBSTArray(arr) == [5, 3, 8, 1, 4, 7, 9]


def test_GenerateBBSTArray_one():
	arr = [1]
	assert GenerateBBSTArray(arr) == [1]


def test_GenerateBBSTArray_three():
	arr = [3, 2, 1]
	assert GenerateBBSTArray(arr) == [2, 1, 3]


def test_GenerateBBSTArray_nine():
	arr = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
	assert GenerateBBSTArray(arr) == [8,4,12,2,6,10,14,1,3,5,7,9,11,13,15]
