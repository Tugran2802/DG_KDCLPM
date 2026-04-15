import unittest
from Lab1 import check_even_odd

class TestStatementCoverage(unittest.TestCase):

    def test_even(self):
        result = check_even_odd(1, [2])
        self.assertEqual(result, ["2 là số chẵn"])

    def test_odd(self):
        result = check_even_odd(1, [3])
        self.assertEqual(result, ["3 là số lẻ"])

    def test_multiple(self):
        result = check_even_odd(3, [1, 2, 3])
        self.assertEqual(result, [
            "1 là số lẻ",
            "2 là số chẵn",
            "3 là số lẻ"
        ])

if __name__ == "__main__":
    unittest.main()