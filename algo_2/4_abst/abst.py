
"""
parent
(I - 1) / 2

left_child
2 * I + 1

right_child
2 * I + 2
"""


class aBST:
	def __init__(self, depth):
		tree_size = pow(2, depth + 1) - 1
		#self.Tree = [None] * tree_size
		self.Tree = [8,4,12,2,6,10,14,1,3,5,7,9,11,13,15]

	def FindKeyIndex(self, key):
		""" сравниваем ключ поиска с ключом текущего узла.
		Если ключ поиска меньше ключа текущего узла, переходим к левому узлу,
		иначе переходим к правому узлу."""
		cur_idx = 0

		while cur_idx < len(self.Tree):
			cur_value = self.Tree[cur_idx]
			if cur_value is None:
				return cur_idx
			if key == cur_value:
				return cur_value * -1
			if key < cur_value:
				cur_idx = 2 * cur_idx + 1
			elif key > cur_value:
				cur_idx = 2 * cur_idx + 2
			else:	#TODO Как тут не писать else?
				return None


		# ищем в массиве индекс ключа
		return None  # не найден

	def AddKey(self, key):

		# добавляем ключ в массив
		return -1;
	# индекс добавленного/существующего ключа или -1 если не удалось



if __name__ == '__main__':
	tree = aBST(3)
	print(tree.Tree)
	tree.FindKeyIndex(10)

