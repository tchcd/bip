class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        """Time complexity O(1) - adding to tail"""
        self.queue = self.queue + [item]
        # OR
        # self.queue.append(item)

    def dequeue(self):
        """Time complexity O(1) - get element by index"""
        if self.size():
            head_element = self.queue[0]
            self.queue = self.queue[1:]
            # OR
            # head_element = self.queue.pop(0)
            return head_element
        return None

    def rotate(self, n):
        n = n % len(self.queue)
        self.queue = self.queue[-n:] + self.queue[:-n]

    def size(self):
        return len(self.queue)


class StackQueue:
    def __init__(self):
        self.enq = []
        self.deq = []

    def enqueue(self, item):
        self.enq.append(item)

    def dequeue(self):
        if not self.deq:
            while self.enq:
                self.deq.append(self.enq.pop())
        if self.deq:
            return self.deq.pop()
        return None

    def size(self):
        return len(self.deq) + len(self.enq)

    def queue(self):
        return self.deq[::-1] + self.enq
