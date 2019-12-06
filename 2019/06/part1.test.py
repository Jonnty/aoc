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

test_input_2 = """
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
K)YOU
I)SAN
""".strip().split("\n")

class PartOneTest(unittest.TestCase):

    def test_part1(self):
         process_input(test_input_1)
         self.assertEqual(42, part1())

    def test_part2(self):
        process_input(test_input_2)
        self.assertEqual(4, part2())

if __name__ == '__main__':
    unittest.main()
