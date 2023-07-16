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

    def test_intersection(self):
        t = PowerSet()
        t.put('a')
        t.put('b')
        t.put('c')

        set1 = {'a', 'b'}
        set2 = {'d','g'}

        self.assertEqual(set(t.intersection(set1)), {'a', 'b'})
        self.assertEqual(t.intersection(set2), [])

    def test_intersection_empty_hash(self):
        t = PowerSet()
        set1 = {'a', 'b'}

        self.assertEqual(t.intersection(set1), [])

    def test_intersection_empty_param(self):
        t = PowerSet()
        t.put('a')
        t.put('b')
        t.put('c')

        set1 = set()

        self.assertEqual(t.intersection(set1), [])

    def test_union(self):
        t = PowerSet()
        t.put('a')
        t.put('b')
        t.put('c')

        set1 = {'a', 'g'}

        self.assertEqual(set(t.union(set1)), {'a','b','c','g'})


    def test_union_empty_hash(self):
        t = PowerSet()

        set1 = {'a', 'b'}

        self.assertEqual(set(t.union(set1)), {'a', 'b'})

    def test_union_empty_param(self):
        t = PowerSet()
        t.put('a')
        t.put('b')
        t.put('c')
        set1 = set()

        self.assertEqual(t.union(set1), ['a','b','c'])

    def test_difference(self):
        t = PowerSet()
        t.put('a')
        t.put('b')
        t.put('c')
        set1 = {'b','g'}

        self.assertEqual(t.difference(set1), ['a', 'c'])

    def test_difference_empty(self):
        t = PowerSet()
        t.put('a')
        t.put('b')
        t.put('c')
        set1 = {'b','c','a'}

        self.assertEqual(t.difference(set1), [])

    def test_issubset_all_params(self):
        t = PowerSet()
        t.put('a')
        t.put('b')
        t.put('c')
        set1 = {'b', 'c'}

        self.assertEqual(t.issubset(set1), True)

    def test_issubset_all_hash(self):
        t = PowerSet()
        t.put('a')
        t.put('b')
        t.put('c')
        set1 = {'b','c','a','g','h'}

        self.assertEqual(t.issubset(set1), False)

    def test_issubset_no_all(self):
        t = PowerSet()
        t.put('a')
        t.put('b')
        t.put('c')
        set1 = {'b','c','g'}

        self.assertEqual(t.issubset(set1), False)


if __name__ == "__main__":
    unittest.main()
