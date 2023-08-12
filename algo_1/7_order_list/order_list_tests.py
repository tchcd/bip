import unittest
from order_list_main import OrderedList, Node


class TestDeque(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def test_to_empty(self):
        l = OrderedList(asc=True)
        l.add(1)

        self.assertEqual([n.value for n in l.get_all()], [1])
        self.assertEqual(l.head.value, 1)
        self.assertEqual(l.tail.value, 1)

    def test_to_empty_desc(self):
        l = OrderedList(asc=False)
        l.add(0)

        self.assertEqual([n.value for n in l.get_all()], [0])
        self.assertEqual(l.head.value, 0)
        self.assertEqual(l.tail.value, 0)

    def test_to_once_asc(self):
        l = OrderedList(asc=True)
        l.add(1)
        l.add(2)

        self.assertEqual([n.value for n in l.get_all()], [1, 2])
        self.assertEqual(l.head.value, 1)
        self.assertEqual(l.tail.value, 2)

    def test_to_once_asc_less(self):
        l = OrderedList(asc=True)
        l.add(1)
        l.add(0)

        self.assertEqual([n.value for n in l.get_all()], [0, 1])
        self.assertEqual(l.head.value, 0)
        self.assertEqual(l.tail.value, 1)

    def test_to_once_desc(self):
        l = OrderedList(asc=False)
        l.add(1)
        l.add(2)

        self.assertEqual([n.value for n in l.get_all()], [2, 1])
        self.assertEqual(l.head.value, 2)
        self.assertEqual(l.tail.value, 1)

    def test_to_once_desc_less(self):
        l = OrderedList(asc=False)
        l.add(1)
        l.add(0)

        self.assertEqual([n.value for n in l.get_all()], [1, 0])
        self.assertEqual(l.head.value, 1)
        self.assertEqual(l.tail.value, 0)

    def test_to_once_to_start(self):
        l = OrderedList(asc=True)
        l.add(1)
        l.add(0)
        l.add(2)
        l.add(-1)

        self.assertEqual([n.value for n in l.get_all()], [-1, 0, 1, 2])
        self.assertEqual(l.head.value, -1)
        self.assertEqual(l.tail.value, 2)

    def test_to_once_to_start_desc(self):
        l = OrderedList(asc=False)
        l.add(1)
        l.add(0)
        l.add(2)
        l.add(2)
        l.add(4)

        self.assertEqual([n.value for n in l.get_all()], [4, 2, 2, 1, 0])
        self.assertEqual(l.head.value, 4)
        self.assertEqual(l.tail.value, 0)

    def test_to_once_to_mid(self):
        l = OrderedList(asc=True)
        l.add(1)
        l.add(0)
        l.add(2)
        l.add(1.5)

        self.assertEqual([n.value for n in l.get_all()], [0, 1, 1.5, 2])
        self.assertEqual(l.head.value, 0)
        self.assertEqual(l.tail.value, 2)

    def test_to_once_to_mid_desc(self):
        l = OrderedList(asc=False)
        l.add(1)
        l.add(0)
        l.add(3)
        l.add(2)

        self.assertEqual([n.value for n in l.get_all()], [3, 2, 1, 0])
        self.assertEqual(l.head.value, 3)
        self.assertEqual(l.tail.value, 0)

    def test_to_once_to_end(self):
        l = OrderedList(asc=True)
        l.add(1)
        l.add(0)
        l.add(2)
        l.add(4)

        self.assertEqual([n.value for n in l.get_all()], [0, 1, 2, 4])
        self.assertEqual(l.head.value, 0)
        self.assertEqual(l.tail.value, 4)

    def test_to_once_to_end_desc(self):
        l = OrderedList(asc=False)
        l.add(1)
        l.add(0)
        l.add(3)
        l.add(2)
        l.add(-1)

        self.assertEqual([n.value for n in l.get_all()], [3, 2, 1, 0, -1])
        self.assertEqual(l.head.value, 3)
        self.assertEqual(l.tail.value, -1)

    def test_remove_from_empty(self):
        l = OrderedList(asc=False)
        l.delete(1)

        self.assertEqual([n.value for n in l.get_all()], [])
        self.assertEqual(l.head, None)
        self.assertEqual(l.tail, None)

    def test_remove_from_once(self):
        l = OrderedList(asc=True)
        l.add(0)

        l.delete(0)

        self.assertEqual([n.value for n in l.get_all()], [])
        self.assertEqual(l.head, None)
        self.assertEqual(l.tail, None)

    def test_remove_from_start(self):
        l = OrderedList(asc=True)
        l.add(0)
        l.add(2)
        l.add(1)
        l.add(4)

        l.delete(0)

        self.assertEqual([n.value for n in l.get_all()], [1, 2, 4])
        self.assertEqual(l.head.value, 1)
        self.assertEqual(l.tail.value, 4)

    def test_remove_from_start_desc(self):
        l = OrderedList(asc=False)
        l.add(0)
        l.add(2)
        l.add(1)
        l.add(4)

        l.delete(4)

        self.assertEqual([n.value for n in l.get_all()], [2, 1, 0])
        self.assertEqual(l.head.value, 2)
        self.assertEqual(l.tail.value, 0)

    def test_remove_from_start_2(self):
        l = OrderedList(asc=True)
        l.add(0)
        l.add(2)
        l.add(1)
        l.add(4)

        l.delete(0)
        l.delete(2)

        self.assertEqual([n.value for n in l.get_all()], [1, 4])
        self.assertEqual(l.head.value, 1)
        self.assertEqual(l.tail.value, 4)

    def test_remove_from_start_desc_2(self):
        l = OrderedList(asc=False)
        l.add(0)
        l.add(2)
        l.add(1)
        l.add(4)

        l.delete(4)
        l.delete(2)

        self.assertEqual([n.value for n in l.get_all()], [1, 0])
        self.assertEqual(l.head.value, 1)
        self.assertEqual(l.tail.value, 0)

    def test_remove_from_mid(self):
        l = OrderedList(asc=True)
        l.add(0)
        l.add(2)
        l.add(2)
        l.add(1)
        l.add(4)

        l.delete(2)

        self.assertEqual([n.value for n in l.get_all()], [0, 1, 2, 4])
        self.assertEqual(l.head.value, 0)
        self.assertEqual(l.tail.value, 4)

    def test_remove_from_mid_desc(self):
        l = OrderedList(asc=False)
        l.add(0)
        l.add(2)
        l.add(1)
        l.add(1)
        l.add(4)

        l.delete(1)
        l.delete(4)

        self.assertEqual([n.value for n in l.get_all()], [2, 1, 0])
        self.assertEqual(l.head.value, 2)
        self.assertEqual(l.tail.value, 0)

    def test_remove_from_end(self):
        l = OrderedList(asc=True)
        l.add(0)
        l.add(2)
        l.add(1)
        l.add(4)
        l.add(4)

        l.delete(4)

        self.assertEqual([n.value for n in l.get_all()], [0, 1, 2, 4])
        self.assertEqual(l.head.value, 0)
        self.assertEqual(l.tail.value, 4)

    def test_remove_from_end_desc(self):
        l = OrderedList(asc=False)
        l.add(0)
        l.add(2)
        l.add(1)
        l.add(1)
        l.add(4)

        l.delete(0)

        self.assertEqual([n.value for n in l.get_all()], [4, 2, 1, 1])
        self.assertEqual(l.head.value, 4)
        self.assertEqual(l.tail.value, 1)

    def test_find_asc(self):
        l = OrderedList(asc=True)
        l.add(0)
        l.add(2)
        l.add(1)
        l.add(1)
        l.add(4)

        a = l.find(2)
        c = l.find(10)

        self.assertEqual([n.value for n in l.get_all()], [0, 1, 1, 2, 4])
        self.assertEqual(l.head.value, 0)
        self.assertEqual(l.tail.value, 4)
        self.assertEqual(a.value, 2)
        self.assertEqual(c, None)

    def test_find_desc(self):
        l = OrderedList(asc=False)
        l.add(0)
        l.add(2)
        l.add(1)
        l.add(1)
        l.add(4)

        a = l.find(2)
        c = l.find(10)

        self.assertEqual([n.value for n in l.get_all()], [4, 2, 1, 1, 0])
        self.assertEqual(l.head.value, 4)
        self.assertEqual(l.tail.value, 0)
        self.assertEqual(a.value, 2)
        self.assertEqual(c, None)


if __name__ == "__main__":
    unittest.main()
