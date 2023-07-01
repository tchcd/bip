import unittest
from hash_main import HashTable



class TestDeque(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def test_hash(self):
        step = 3
        size = 4
        t = HashTable(size, step)
        self.assertEqual(t.hash_fun('Hela'), 2)

    def test_put(self):
        step = 3
        size = 4
        t = HashTable(size, step)

        str1 = 'Hela'
        str2 = 'Hels'
        str3 = 'Helfh'
        str4 = 'Helg'
        str5 = 'Helhg'
        str6 = 'Helj'

        str_put1 = t.put(str1)
        str_put2 = t.put(str2)
        str_put3 = t.put(str3)
        str_put4 = t.put(str4)
        str_put5 = t.put(str5)

        self.assertEqual(str_put1, 2)
        self.assertEqual(str_put3, 3)
        self.assertEqual(str_put5, None)

    def test_find(self):
        step = 3
        size = 4
        t = HashTable(size, step)

        str1 = 'Hela'
        str2 = 'Hels'
        str3 = 'Helfh'
        str4 = 'Helg'
        str5 = 'Helhg'
        str6 = 'Helj'

        str_put1 = t.put(str1)
        str_put2 = t.put(str2)
        str_put3 = t.put(str3)
        str_put4 = t.put(str4)
        str_put5 = t.put(str5)

        str_find1 = t.find(str1)
        str_find3 = t.find(str3)
        str_find5 = t.find(str5)

        self.assertEqual(str_find1, 2)
        self.assertEqual(str_find3, 3)
        self.assertEqual(str_find5, None)


if __name__ == "__main__":
    unittest.main()