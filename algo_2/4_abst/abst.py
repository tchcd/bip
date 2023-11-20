class aBST:
	def __init__(self, depth):
		tree_size = pow(2, depth + 1) - 1
		self.Tree = [None] * tree_size

	def FindKeyIndex(self, key):
		# ищем в массиве индекс ключа
		return None  # не найден

	def AddKey(self, key):
		# добавляем ключ в массив
		return -1;
	# индекс добавленного/существующего ключа или -1 если не удалось



if __name__ == '__main__':
	tree = aBST(3)
	print(tree.Tree)

