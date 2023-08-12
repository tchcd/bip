

class StacksQueue:
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

    def get_queue(self):
        return self.deq[::-1] + self.enq


if __name__ == "__main__":
    q = StacksQueue()

    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)

    print(q.size())
    print(q.get_queue())

    a = q.dequeue()
    print(a)
    print(q.get_queue())
    b = q.dequeue()
    print(b)

    c = q.dequeue()
    print(c)

    d = q.dequeue()
    print(d)
