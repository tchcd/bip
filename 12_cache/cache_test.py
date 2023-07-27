import unittest
from cache_main import NativeCache

class TestCache(unittest.TestCase):
    def setUp(self) -> None:
        self.c = NativeCache(6)

        for _ in range(7):
            self.c.add_item(f'jojopa{_}', f'absc{_}')

        for y in range(7):
            g = 1
            for i in range(y):
                self.c.get_value(f'jojopa{y}')
                g += 1

    def test_cache1(self):
        self.c.add_item(f'new', f'new')

        self.assertEqual(self.c.slots, ['jojopa6', 'new', 'jojopa1', 'jojopa2', 'jojopa3', 'jojopa4'])

    def test_cache2(self):
        self.c.add_item(f'new', f'new')
        self.c.get_value(f'new')
        self.c.get_value(f'new')
        self.c.get_value(f'new')
        self.c.add_item(f'new2', f'new2')
        self.assertEqual(self.c.slots, ['jojopa6', 'new', 'new2', 'jojopa2', 'jojopa3', 'jojopa4'])


if __name__ == "__main__":
    unittest.main()
