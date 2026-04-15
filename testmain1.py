import unittest
from Lab1 import check_even_odd

class TestPathCoverage(unittest.TestCase):

    def test_all_even(self):
        self.assertEqual(
            check_even_odd(3, [2, 4, 6]),
            ["2 là số chẵn", "4 là số chẵn", "6 là số chẵn"]
        )

    def test_all_odd(self):
        self.assertEqual(
            check_even_odd(3, [1, 3, 5]),
            ["1 là số lẻ", "3 là số lẻ", "5 là số lẻ"]
        )

    def test_mixed(self):
        self.assertEqual(
            check_even_odd(3, [1, 2, 3]),
            ["1 là số lẻ", "2 là số chẵn", "3 là số lẻ"]
        )

    def test_no_loop(self):
        self.assertEqual(check_even_odd(0, []), [])


if __name__ == "__main__":
    unittest.main()