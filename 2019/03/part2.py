import os


def part2(lines):
    return closest_intersection(lines[0], lines[1])

def movement(((X, Y), D), movement):
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
        x = X + (direction[0] * i)
        y = Y + (direction[1] * i)
        d = D + i

        points.append(((x, y), d))
    return points

def paths(*wire_movements):
    movements_list = [[move for move in moves.split(",")] for moves in wire_movements]
    paths = [[((0, 0), 0)] for _ in movements_list]

    for i, movements in enumerate(movements_list):
        for move in movements:
            paths[i].extend(movement(paths[i][-1], move))

    return [dict(path) for path in paths]

def closest_intersection(wire1, wire2):
    path1, path2 = paths(wire1, wire2)
    locs1, locs2 = path1.keys(), path2.keys()
    crossovers = set(locs1).intersection(set(locs2))
    crossovers.remove((0,0))
    sums = [path1[crossover] + path2[crossover] for crossover in crossovers]
    return min(sums)

if __name__ == "__main__":
    input_loc = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'input')
    print(part2(open(input_loc).readlines()))
