import unittest

from part1 import valid

class PartOneTest(unittest.TestCase):

    def test_provided(self):
        self.assertTrue(valid(122345))
        self.assertTrue(valid(111123))
        self.assertTrue(valid(111111))

        self.assertFalse(valid(135679))
        self.assertFalse(valid(223450))
        self.assertFalse(valid(123789))
        self.assertFalse(valid(12335))

if __name__ == '__main__':
    unittest.main()
