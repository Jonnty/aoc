import unittest

from part2 import part2

class PartOneTest(unittest.TestCase):

    def test_provided(self):
        self.assertEqual(3500, run_program([1,9,10,3,2,3,11,0,99,30,40,50]))
        self.assertEqual(2, run_program([1,0,0,0,99]))
        self.assertEqual(2, run_program([2,3,0,3,99]))
        self.assertEqual(2, run_program([2,4,4,5,99,0]))
        self.assertEqual(30, run_program([1,1,1,4,99,5,6,0,99]))

if __name__ == '__main__':
    unittest.main()
