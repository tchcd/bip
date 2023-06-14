import unittest
from deque_main import Deque


class TestDeque(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def test_add_front(self):
        deque = Deque()
        deque.addFront(1)
        deque.addFront(2)
        deque.addFront(3)
        self.assertEqual(deque.deque, [3, 2, 1])
        self.assertEqual(deque.size(), 3)

    def test_add_tail(self):
        deque = Deque()
        deque.addTail(1)
        deque.addTail(2)
        deque.addTail(3)
        self.assertEqual(deque.deque, [1, 2, 3])
        self.assertEqual(deque.size(), 3)

    def test_remove_tail(self):
        deque = Deque()
        deque.addTail(1)
        deque.addTail(2)
        deque.addTail(3)
        a = deque.removeTail()
        self.assertEqual(deque.deque, [1, 2])
        self.assertEqual(deque.size(), 2)
        self.assertEqual(a, 3)

    def test_remove_front(self):
        deque = Deque()
        deque.addTail(1)
        deque.addTail(2)
        deque.addTail(3)
        a = deque.removeFront()
        self.assertEqual(deque.deque, [2, 3])
        self.assertEqual(deque.size(), 2)
        self.assertEqual(a, 1)

    def test_remove_front_empty(self):
        deque = Deque()
        a = deque.removeFront()
        self.assertEqual(deque.deque, [])
        self.assertEqual(deque.size(), 0)
        self.assertEqual(a, None)

    def test_remove_tail_empty(self):
        deque = Deque()
        a = deque.removeTail()
        self.assertEqual(deque.deque, [])
        self.assertEqual(deque.size(), 0)
        self.assertEqual(a, None)


    def test_remove_front_one(self):
        deque = Deque()
        deque.addTail('t2')
        a = deque.removeTail()
        self.assertEqual(deque.deque, [])
        self.assertEqual(deque.size(), 0)
        self.assertEqual(a, 't2')


if __name__ == "__main__":
    unittest.main()