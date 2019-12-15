import os, intcode

from copy import deepcopy

directions = {
    1: (0, 1),
    2: (0, -1),
    3: (1, 0),
    4: (-1, 0)
}

class Robot:
    visited = set()
    def __init__(self, code):
        self.instance = intcode.Intcode(code)
        self.loc = (0,0)
        self.distance = 0

    def split(self):
        splitted = [self, deepcopy(self), deepcopy(self), deepcopy(self)]
        for i, s in enumerate(splitted):
            s.move( i + 1)
        added = [s for s in splitted if s.status != 0 and not s.loc in self.visited]
        for r in added:
            self.visited.add(r.loc)
        return added


    def move(self, direction):
        self.distance += 1
        x, y = self.loc
        dx, dy = directions[direction]
        self.loc = (x + dx, y + dy)
        self.status = self.instance.run(direction)[0]

    def __repr__(self):
        return "%s" % (str(self.loc))


def part1(lines):
    code = [int(e) for e in lines[0].split(',')]

    queue = [Robot(code)]
    while True:
        edges = queue.pop(0).split()
        print(edges)
        for edge in edges:
            if edge.status == 2: return edge.distance
        queue.extend(edges)


if __name__ == "__main__":
    input_loc = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'input')
    print(part1(open(input_loc).readlines()))
