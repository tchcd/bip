def is_palindrome(text: str):
	length = len(text)
	l = 0
	r = length - 1

	def compare(l, r):
		if l == r:
			return True
		if text[l] != text[r]:
			return False
		return compare(l + 1, r - 1)
	return compare(l, r)


if __name__ == '__main__':
	print(is_palindrome('yobananaboy'))
	print(is_palindrome('abcdef'))






