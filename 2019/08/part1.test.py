import unittest

from part1 import part1

class PartOneTest(unittest.TestCase):

    def test_provided(self):
        self.assertEqual(1, part1("123456789012", (3, 2)))

if __name__ == '__main__':
    unittest.main()
