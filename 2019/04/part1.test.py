import unittest

from part1 import valid

from part1_quicker import valid as valid2

class PartOneTest(unittest.TestCase):

    def check_f(self, f):
        self.assertTrue(f(122345))
        self.assertTrue(f(111123))
        self.assertTrue(f(111111))

        self.assertFalse(f(135679))
        self.assertFalse(f(223450))
        self.assertFalse(f(123789))
        self.assertFalse(f(12335))

    def test_original(self):
        self.check_f(valid)

    def test_new(self):
        self.check_f(valid2)


if __name__ == '__main__':
    unittest.main()
