import os


def part1(lines):
    return closest_intersection(lines[0], lines[1])

def dist(p, q):
    return abs(p[0] - q[0]) + abs(p[1] - q[1])

def movement(p, movement):
    directions = {
        'R': (1, 0),
        'D': (0, -1),
        'L': (-1, 0),
        'U': (0, 1)
    }
    direction = directions[movement[0]]
    distance = int(movement[1:])
    points = []
    for i in range(1, distance + 1):
        points.append((p[0] + (direction[0] * i), p[1] + (direction[1] * i)))
    return points

def paths(*wire_movements):
    movements_list = [[move for move in moves.split(",")] for moves in wire_movements]
    paths = [[(0, 0)] for _ in movements_list]

    for i, movements in enumerate(movements_list):
        for move in movements:
            paths[i].extend(movement(paths[i][-1], move))

    return paths

def closest_intersection(wire1, wire2):
    path1, path2 = paths(wire1, wire2)
    crossovers = set(path1).intersection(set(path2))
    crossovers.remove((0,0)) # we know about that one already
    mini =  min(crossovers, key=lambda p: dist(p, (0,0)))
    return dist(mini, (0,0))

if __name__ == "__main__":
    input_loc = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'input')
    print(part1(open(input_loc).readlines()))
