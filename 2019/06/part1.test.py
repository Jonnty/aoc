import unittest

from part1 import part1, part2, process_input

test_input_1 = """
COM)B
B)C
C)D
D)E
E)F
B)G
G)H
D)I
E)J
J)K
K)L
""".strip().split("\n")

class PartOneTest(unittest.TestCase):

    def test_provided(self):

        self.assertEqual(42, part1(test_input_1))

if __name__ == '__main__':
    unittest.main()
