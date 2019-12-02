import unittest

from part2 import total_fuel

class PartTwoTest(unittest.TestCase):

    def test_provided(self):
        self.assertEqual(2, total_fuel(14))
        self.assertEqual(966, total_fuel(1969))
        self.assertEqual(50346, total_fuel(100756))

if __name__ == '__main__':
    unittest.main()
