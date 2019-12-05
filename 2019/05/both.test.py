import unittest, io, sys, os

from both import read_instruction, both

class PartOneTest(unittest.TestCase):

    def test_read_instruction(self):
        self.assertEqual((2, [0, 1]), read_instruction(1002))

    def assert_last_stdout_line(self, f, test_in, expected_out):
        stdin, stdout = sys.stdin, sys.stdout
        sys.stdin = io.StringIO(test_in)
        sys.stdout = io.StringIO()
        try:
            f()
            real_out = sys.stdout.getvalue().split('\n')[-2]
        finally:
            sys.stdin, sys.stdout = stdin, stdout
        self.assertEqual(expected_out, real_out)


    def test_part1(self):
        f = lambda: both(self.initial_state())
        self.assert_last_stdout_line(f, "1\n", str(13787043))

    def test_part2(self):
        f = lambda: both(self.initial_state())
        self.assert_last_stdout_line(f, "5\n", str(3892695))

    def initial_state(self):
        input_loc = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'input')
        with open(input_loc) as f:
            return f.readlines()

if __name__ == '__main__':
    unittest.main()
