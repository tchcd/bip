
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
		#self.Tree = [8,4,12,None,6,10,14,None,None,5,7,9,None,13,15] #2,1,3, 11
		self.Tree = [None]  # 2,1,3, 11

	def FindKeyIndex(self, key):
		""" сравниваем ключ поиска с ключом текущего узла.
		Если ключ поиска меньше ключа текущего узла, переходим к левому узлу,
		иначе переходим к правому узлу."""
		cur_idx = 0
		# ищем в массиве индекс ключа
		while cur_idx < len(self.Tree):
			cur_value = self.Tree[cur_idx]
			if cur_value is None:
				return cur_idx * -1
			if key == cur_value:
				return cur_idx
			if key < cur_value:
				cur_idx = 2 * cur_idx + 1
			elif key > cur_value:
				cur_idx = 2 * cur_idx + 2
			else:
				return None # не найден

	def AddKey(self, key):
		found_idx = self.FindKeyIndex(key)
		print(found_idx)
		if found_idx is not None and found_idx <= 0:
			print('вставляю')
			found_idx = found_idx * -1
			self.Tree[found_idx] = key
			return found_idx
		return ("ответ", -1)


if __name__ == '__main__':
	tree = aBST(1)
	print(tree.Tree)
	print(tree.AddKey(2))
	print(tree.AddKey(8))
	#print(tree.AddKey(20))
	print(tree.Tree)

https://skillsmart.ru/algo/15-121-cm/bcd63523a1.html