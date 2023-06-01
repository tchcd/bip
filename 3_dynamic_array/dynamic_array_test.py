import unittest
from dynamic_array_main import DynArray

"""
+ вставка элемента, когда в итоге размер буфера не превышен (проверьте также размер буфера);
+ вставка элемента, когда в результате превышен размер буфера (проверьте также корректное изменение размера буфера);
+ попытка вставки элемента в недопустимую позицию;
+ удаление элемента, когда в результате размер буфера остаётся прежним (проверьте также размер буфера);
+ удаление элемента, когда в результате понижается размер буфера (проверьте также корректное изменение размера буфера);
-- попытка удаления элемента в недопустимой позиции.
"""
class TestDynArray(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def test_insert_to_normal_buffer_to_start(self):
        da = DynArray()
        for i in range(20):
            da.append(i)

        self.assertEqual(da.capacity, 32)
        self.assertEqual(da.count, 20)

        da.insert(0, 999)
        self.assertEqual([i for i in da], [999] + [i for i in range(20)])
        self.assertEqual(da.capacity, 32)
        self.assertEqual(da.count, 21)

    def test_insert_to_normal_buffer_to_last_pos(self):
        da = DynArray()
        for i in range(20):
            da.append(i)

        self.assertEqual(da.capacity, 32)
        self.assertEqual(da.count, 20)

        da.insert(20, 999)
        self.assertEqual([i for i in da], [i for i in range(20)] + [999])
        self.assertEqual(da.capacity, 32)
        self.assertEqual(da.count, 21)

    def test_insert_to_normal_buffer_to_middle_pos(self):
        da = DynArray()
        for i in range(20):
            da.append(i)

        self.assertEqual(da.capacity, 32)
        self.assertEqual(da.count, 20)

        da.insert(2, 999)
        self.assertEqual([i for i in da], [0, 1] + [999] + [i for i in range(2, 20)])
        self.assertEqual(da.capacity, 32)
        self.assertEqual(da.count, 21)

    def test_insert_to_extend_buffer_to_start(self):
        da = DynArray()
        for i in range(16):
            da.append(i)

        self.assertEqual(da.capacity, 16)
        self.assertEqual(da.count, 16)

        da.insert(0, 999)
        self.assertEqual([i for i in da], [999] + [i for i in range(16)])
        self.assertEqual(da.capacity, 32)
        self.assertEqual(da.count, 17)

    def test_insert_to_extend_buffer_to_last_pos(self):
        da = DynArray()
        for i in range(16):
            da.append(i)

        self.assertEqual(da.capacity, 16)
        self.assertEqual(da.count, 16)

        da.insert(16, 999)
        self.assertEqual([i for i in da], [i for i in range(16)] + [999])
        self.assertEqual(da.capacity, 32)
        self.assertEqual(da.count, 17)

    def test_insert_to_extend_buffer_to_middle_pos(self):
        da = DynArray()
        for i in range(16):
            da.append(i)

        self.assertEqual(da.capacity, 16)
        self.assertEqual(da.count, 16)

        da.insert(2, 999)
        self.assertEqual([i for i in da], [0, 1] + [999] + [i for i in range(2, 16)])
        self.assertEqual(da.capacity, 32)
        self.assertEqual(da.count, 17)

    def test_insert_to_incorrect_pos(self):
        da = DynArray()
        for i in range(8):
            da.append(i)
        self.assertEqual(da.capacity, 16)
        self.assertEqual(da.count, 8)

        self.assertRaises(IndexError, da.insert, 9, 999)
        self.assertRaises(IndexError, da.insert, -1, 999)

    def test_delete_from_normal_buffer_from_start(self):
        da = DynArray()
        for i in range(20):
            da.append(i)

        self.assertEqual(da.capacity, 32)
        self.assertEqual(da.count, 20)

        da.delete(0)
        self.assertEqual([i for i in da], [i for i in range(1, 20)])
        self.assertEqual(da.capacity, 32)
        self.assertEqual(da.count, 19)

    def test_delete_from_normal_buffer_from_last_pos(self):
        da = DynArray()
        for i in range(20):
            da.append(i)

        self.assertEqual(da.capacity, 32)
        self.assertEqual(da.count, 20)

        da.delete(19)
        self.assertEqual([i for i in da], [i for i in range(0, 19)])
        self.assertEqual(da.capacity, 32)
        self.assertEqual(da.count, 19)

    def test_delete_from_normal_buffer_from_middle_pos(self):
        da = DynArray()
        for i in range(20):
            da.append(i)

        self.assertEqual(da.capacity, 32)
        self.assertEqual(da.count, 20)

        da.delete(2)
        self.assertEqual([i for i in da], [0, 1] + [i for i in range(3, 20)])
        self.assertEqual(da.capacity, 32)
        self.assertEqual(da.count, 19)

    def test_delete_from_decreased_buffer_from_start(self):
        da = DynArray()
        for i in range(32):
            da.append(i)

        self.assertEqual(da.capacity, 32)
        self.assertEqual(da.count, 32)
        self.assertEqual([i for i in da], [i for i in range(32)])
        for _ in range(17):
            da.delete(0)

        self.assertEqual([i for i in da], [i for i in range(17, 32)])
        self.assertEqual(da.capacity, int(32/1.5))
        self.assertEqual(da.count, 15)

    def test_delete_from_decreased_buffer_from_last_pos(self):
        da = DynArray()
        for i in range(32):
            da.append(i)

        self.assertEqual(da.capacity, 32)
        self.assertEqual(da.count, 32)
        self.assertEqual([i for i in da], [i for i in range(32)])
        for _ in range(31, 14, -1):
            da.delete(_)


        self.assertEqual([i for i in da], [i for i in range(15)])
        self.assertEqual(da.capacity, int(32 / 1.5))
        self.assertEqual(da.count, 15)

    def test_delete_from_decreased_buffer_from_middle_pos(self):
        da = DynArray()
        for i in range(64):
            da.append(i)

        self.assertEqual(da.capacity, 64)
        self.assertEqual(da.count, 64)
        self.assertEqual([i for i in da], [i for i in range(64)])
        for _ in range(63, 30, -1):
            da.delete(_)

        self.assertEqual([i for i in da], [i for i in range(31)])
        self.assertEqual(da.capacity, int(64 / 1.5))
        self.assertEqual(da.count, 31)

    def test_delete_from_incorrect_pos(self):
        da = DynArray()
        for i in range(8):
            da.append(i)
        self.assertEqual(da.capacity, 16)
        self.assertEqual(da.count, 8)

        self.assertRaises(IndexError, da.delete, 9)
        self.assertRaises(IndexError, da.delete, -1)



if __name__ == "__main__":
    unittest.main()