import unittest
from set_main import PowerSet


class TestPowerSet(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def test_put_present_elem(self):
        t = PowerSet()
        t.put('a')
        t.put('b')
        t.put('c')

        t.put('c')
        self.assertEqual(set(t.slots), {'a', 'b', 'c'})

    def test_remove_elem(self):
        t = PowerSet()
        t.put('a')
        t.put('b')
        t.put('c')

        self.assertEqual(t.remove('c'), True)
        self.assertEqual(t.remove('d'), False)
        self.assertEqual(set(t.slots), {'a', 'b'})

    def test_exception_intersection(self):
        t1 = PowerSet()
        t2 = PowerSet()
        for i in range(1, 101):
            t1.put(i)
        for i in range(50, 151):
            t2.put(i)

        self.assertEqual(set(t1.intersection(t2)), set(i for i in range(50, 101)))
        self.assertEqual(t1.intersection(t2), [i for i in range(50, 101)])

    def test_intersection(self):
        t1 = PowerSet()
        t2 = PowerSet()
        t3 = PowerSet()
        t1.put('a')
        t1.put('b')
        t1.put('c')

        t2.put('a')
        t2.put('b')
        t3.put('d')
        t3.put('g')

        self.assertEqual(set(t1.intersection(t2)), {'a', 'b'})
        self.assertEqual(t1.intersection(t3), [])

    def test_intersection_empty_hash(self):
        t1 = PowerSet()
        t2 = PowerSet()

        t2.put('a')
        t2.put('b')
        self.assertEqual(t1.intersection(t2), [])

    def test_intersection_empty_param(self):
        t1 = PowerSet()
        t2 = PowerSet()
        t1.put('a')
        t1.put('b')
        t1.put('c')

        self.assertEqual(list(t1.intersection(t2).slots.keys()), [])

    def test_union(self):
        t1 = PowerSet()
        t2 = PowerSet()
        t1.put('a')
        t1.put('b')
        t1.put('c')
        t1.put(1)

        t2.put('a')
        t2.put('g')
        t2.put(1)

        self.assertEqual(set(t1.union(t2).slots.keys()), {'a', 'b', 'c', 'g', 1})

    def test_union_empty_hash(self):
        t1 = PowerSet()
        t2 = PowerSet()
        t2.put('a')
        t2.put('b')

        self.assertEqual(set(t1.union(t2).slots.keys()), {'a', 'b'})

    def test_union_empty_param(self):
        t1 = PowerSet()
        t2 = PowerSet()
        t1.put('a')
        t1.put('b')
        t1.put('c')

        self.assertEqual(t1.union(t2).slots.keys(), {'a', 'b', 'c'})

    def test_difference(self):
        t1 = PowerSet()
        t2 = PowerSet()
        t1.put('a')
        t1.put('b')
        t1.put('c')
        t1.put(1)

        t2.put('b')
        t2.put('g')

        self.assertEqual(t1.difference(t2), ['a', 'c', 1])

    def test_difference_empty(self):
        t1 = PowerSet()
        t2 = PowerSet()
        t1.put('a')
        t1.put('b')
        t1.put('c')

        t2.put('b')
        t2.put('c')
        t2.put('a')

        self.assertEqual(t1.difference(t2), [])

    def test_issubset_all_params(self):
        t1 = PowerSet()
        t2 = PowerSet()
        t1.put('a')
        t1.put('b')
        t1.put('c')
        t1.put(1)

        t2.put('b')
        t2.put('c')
        t2.put(1)

        self.assertEqual(t1.issubset(t2), True)

    def test_issubset_all_hash(self):
        t1 = PowerSet()
        t2 = PowerSet()
        t1.put('a')
        t1.put('b')
        t1.put('c')

        t2.put('b')
        t2.put('c')
        t2.put('a')
        t2.put('g')
        t2.put('h')

        self.assertEqual(t1.issubset(t2), False)

    def test_issubset_no_all(self):
        t1 = PowerSet()
        t2 = PowerSet()
        t1.put('a')
        t1.put('b')
        t1.put('c')

        t2.put('b')
        t2.put('c')
        t2.put('g')

        self.assertEqual(t1.issubset(t2), False)


if __name__ == "__main__":
    unittest.main()
