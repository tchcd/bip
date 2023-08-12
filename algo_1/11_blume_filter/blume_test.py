import unittest
from blume_main import BloomFilter


class TestPowerSet(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def test_string(self):
        f = BloomFilter(32)

        f.add('0123456789')
        f.add('1234567890')
        f.add('9012345678')
        f.add('8901234567')

        self.assertEqual(f.is_value('0123456789'), True)
        self.assertEqual(f.is_value('1234567890'), True)
        self.assertEqual(f.is_value('9012345678'), True)
        self.assertEqual(f.is_value('8901234567'), True)

        self.assertEqual(f.is_value('hakad'), False)

    def test_string_2(self):
        f = BloomFilter(32)

        f.add('haha')
        f.add('hoho')
        f.add('123')
        f.add('141414')

        self.assertEqual(f.is_value('haha'), True)
        self.assertEqual(f.is_value('hoho'), True)
        self.assertEqual(f.is_value('123'), True)
        self.assertEqual(f.is_value('141414'), True)

        self.assertEqual(f.is_value('ha'), False)

    def test_empty(self):
        f = BloomFilter(32)

        self.assertEqual(f.is_value('haha'), False)
        self.assertEqual(f.is_value('hoho'), False)
        self.assertEqual(f.is_value('123'), False)
        self.assertEqual(f.is_value('141414'), False)
        self.assertEqual(f.is_value('ha'), False)


if __name__ == "__main__":
    unittest.main()
