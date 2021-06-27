# Задача 2. Написать тесты для домашних работ из курса «Python 1».
import unittest
from gnome_sort import gnome


class TestGnomeSort(unittest.TestCase):
    arr = [2, 5, 8, 2, 6, 7, 8, 6, 5, 4, 5]
    res = [2, 2, 4, 5, 5, 5, 6, 6, 7, 8, 8]

    def test_equal_arr(self):
        self.assertEqual(gnome(self.arr), self.res)

    def test_min_number(self):
        self.assertEqual(gnome(self.arr)[0], min(self.arr))

    def test_max_number(self):
        self.assertEqual(gnome(self.arr)[-1], max(self.arr))


if __name__ == '__main__':
    unittest.main()
