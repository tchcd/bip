import unittest
from am_main import NativeDictionary

class TestDeque(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def test_hash(self):
        size = 7
        t = NativeDictionary(size)
        self.assertEqual(t.hash_fun('privet'), 1)

    def test_put(self):
        size = 5
        t = NativeDictionary(size)

        str1 = 'Hela'
        str2 = 'Helaa'
        str3 = 'Helaaa'

        t.put(str1, 1)
        t.put(str2, 2)
        t.put(str3, 3)

        self.assertEqual(t.values, ['Helaa', None, 'Helaaa', 'Hela', None])
        self.assertEqual(t.slots, [2, None, 3, 1, None])

    def test_get(self):
        size = 5
        t = NativeDictionary(size)

        str1 = 'Hela'
        str2 = 'Helaa'
        str3 = 'Helaaa'

        t.put(str1, 1)
        t.put(str2, 2)
        t.put(str3, 3)

        str_find1 = t.get(str1)
        str_find2 = t.get(str2)
        str_find3 = t.get(str3)
        str_find4 = t.get('Nonee')

        self.assertEqual(str_find1, 1)
        self.assertEqual(str_find2, 2)
        self.assertEqual(str_find3, 3)
        self.assertEqual(str_find4, None)

    def test_is_key(self):
        size = 5
        t = NativeDictionary(size)

        str1 = 'Hela'
        str2 = 'Helaa'
        str3 = 'Helaaa'

        t.put(str1, 1)
        t.put(str2, 2)
        t.put(str3, 3)

        self.assertEqual(t.is_key('Helaa'), True)
        self.assertEqual(t.is_key('Helicopter'), False)

    def test_put_max(self):
        size = 5
        t = NativeDictionary(size)

        str1 = 'Hela'
        str2 = 'Helaa'
        str3 = 'Helaaa'
        str4 = 'Helaaaa'
        str5 = 'Helaaaa'

        t.put(str1, 1)
        t.put(str2, 2)
        t.put(str3, 3)
        t.put(str4, 4)
        t.put(str5, 5)

        self.assertEqual(t.values, ['Helaa', 'Helaaaa', 'Helaaa', 'Hela', 'Helaaaa'])
        self.assertEqual(t.slots, [2, 5, 3, 1, 4])


if __name__ == "__main__":
    unittest.main()
