import os
from collections import defaultdict

from intcode import Intcode, TerminatedException, ExitException

painted = defaultdict(int)

# clockwise from up
directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

class GridWalker:

    def __init__(self, position=(0,0), direction=0):
        self.position = position
        self.direction = direction
        self.values = defaultdict(int)

    def step(self, steps=1):
        x, y = self.position
        dx, dy = directions[self.direction]
        self.position = (x + (dx * steps), y + (dy * steps))

    def get_value(self):
        return self.values[self.position]

    def set_value(self, value):
        self.values[self.position] = value

    def turn_left(self):
        self.direction -= 1
        self.direction %= 4

    def turn_right(self):
        self.direction += 1
        self.direction %= 4

# The Intcode program will serve as the brain of the robot. The program uses input instructions to access the robot's camera: provide 0 if the robot is over a black panel or 1 if the robot is over a white panel. Then, the program will output two values:
#
# First, it will output a value indicating the color to paint the panel the robot is over: 0 means to paint the panel black, and 1 means to paint the panel white.
# Second, it will output a value indicating the direction the robot should turn: 0 means it should turn left 90 degrees, and 1 means it should turn right 90 degrees.
# After the robot turns, it should always move forward exactly one panel. The robot starts facing up.

def part1(lines):
    program = [int(e) for e in lines[0].split(',')]
    code = Intcode(program)
    robot = GridWalker()
    robot.values[(0,0)] = 1

    while True:
        try:
            colour, turn = code.run(robot.get_value())
        except ExitException:
            break
        robot.set_value(colour)
        if turn == 0:
            robot.turn_left()
        else:
            robot.turn_right()
        robot.step()


    return len(robot.values)



if __name__ == "__main__":
    input_loc = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'input')
    print(part1(open(input_loc).readlines()))
