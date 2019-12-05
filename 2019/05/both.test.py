import unittest

from part1 import read_instruction

class PartOneTest(unittest.TestCase):

    def test_read_instruction(self):
        self.assertEqual((2, [0, 1]), read_instruction(1002))

if __name__ == '__main__':
    unittest.main()
