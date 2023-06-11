import unittest
from queue_main import Queue


class TestQueue(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def test_eq(self):
        q = Queue()

        q.enqueue(1)
        q.enqueue(2)
        q.enqueue(3)

        self.assertEqual([i for i in q.queue], [1, 2, 3])
        self.assertEqual(q.size(), 3)

    def test_deq(self):
        q = Queue()

        q.enqueue(1)
        q.enqueue(2)
        q.enqueue(3)

        a = q.dequeue()

        self.assertEqual([i for i in q.queue], [2, 3])
        self.assertEqual(q.size(), 2)
        self.assertEqual(a, 1)

    def test_deq_empty(self):
        q = Queue()

        a = q.dequeue()

        self.assertEqual([i for i in q.queue], [])
        self.assertEqual(q.size(), 0)
        self.assertEqual(a, None)

    def test_deq_one_el(self):
        q = Queue()

        q.enqueue(2)
        a = q.dequeue()

        self.assertEqual([i for i in q.queue], [])
        self.assertEqual(q.size(), 0)
        self.assertEqual(a, 2)

    def test_rotate(self):
        q = Queue()
        q.enqueue(1)
        q.enqueue(2)
        q.enqueue(3)
        q.enqueue(4)
        q.enqueue(5)

        q.rotate(7)

        self.assertEqual([i for i in q.queue], [4, 5, 1, 2, 3])
        self.assertEqual(q.size(), 5)


if __name__ == "__main__":
    unittest.main()
