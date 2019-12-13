import unittest

from part2 import part2, angle, r, recentre, decentre

class PartTwoTest(unittest.TestCase):

    def test_angle(self):
        self.assertEqual(0, angle((0, -1)))
        self.assertEqual(90, angle((1, 0)))
        self.assertEqual(180, angle((0, 1)))
        self.assertEqual(270, angle((-1, 0)))

        self.assertEqual(45, angle((1, -1)))
        self.assertEqual(135, angle((1, 1)))
        self.assertEqual(315, angle((-1, -1)))

    def test_r(self):
        self.assertEqual(1, r((0, 1)))
        self.assertEqual(1, r((0, -1)))
        self.assertEqual(5, r((3, 4)))

    def test_recentre(self):
        self.assertEqual((0, 0), recentre((5, 3), (5, 3)))
        self.assertEqual((1, 1), recentre((5, 5), (4, 4)))
        self.assertEqual((10, 11), recentre((5, 5), (-5, -6)))

    def test_decentre(self):
        self.assertEqual((5, 3), decentre((0, 0), (5, 3)))
        self.assertEqual((5, 5), decentre((1, 1), (4, 4)))
        self.assertEqual((5, 5), decentre((10, 11), (-5, -6)))

if __name__ == '__main__':
    unittest.main()
