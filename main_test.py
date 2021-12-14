import unittest
from main import print_hi_stephen, print_hi_Kyanna, print_hi_Cindy  # , print_hi_

class MyTestCase(unittest.TestCase):
    def test_print_hi_stephen(self):
        self.assertEqual(print_hi_stephen(), f"Hi, Stephen")

    def test_print_hi_you(self):
        self.assertEqual(print_hi_Kyanna(), f"Hi, the most beautiful girl!!!!")

    def test_print_hi_Cindy(self):
        self.assertEqual(print_hi_Cindy(), f"Hi, Cindybb!!")


if __name__ == '__main__':
    unittest.main()
