class aBST:
	def __init__(self, depth):
		tree_size = pow(2, depth + 1) - 1
		self.Tree = [None] * tree_size

	def FindKeyIndex(self, key):
		cur_idx = 0
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
				return None

	def AddKey(self, key):
		found_idx = self.FindKeyIndex(key)
		if found_idx is not None and found_idx <= 0:
			found_idx = found_idx * -1
			self.Tree[found_idx] = key
			return found_idx
		return -1
