class Deque:
    """ addHead/removeHead - O(n) complexity, because we have to reindex our massive
        addTail/removeTail - O(1) complexity
    """
    def __init__(self):
        self.deque = []

    def addFront(self, item):
        self.deque = [item] + self.deque

    def addTail(self, item):
        self.deque = self.deque + [item]

    def removeFront(self):
        if self.deque:
            front_element = self.deque[0]
            self.deque = self.deque[1:]
            return front_element
        return None

    def removeTail(self):
        if self.deque:
            tail_element = self.deque[-1]
            self.deque = self.deque[:-1]
            return tail_element
        return None

    def size(self):
        return len(self.deque)


'''
def is_palindrome(word):
    deque = Deque()

    for c in word:
        if c != ' ':
            deque.addTail(c)

    while deque.size() > 1:
        front_char = deque.removeFront()
        tail_char = deque.removeTail()
        if front_char != tail_char:
            return False
    return True
print(is_palindrome('never odd or even'))
'''
