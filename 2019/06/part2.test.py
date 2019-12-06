import unittest

from part2 import part2

class PartTwoTest(unittest.TestCase):

    def test_provided(self):
        self.assertEqual(1, part2(1))

if __name__ == '__main__':
    unittest.main()
