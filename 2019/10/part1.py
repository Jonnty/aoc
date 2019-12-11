import os, itertools, sys
from collections import defaultdict

from math import gcd

def is_whole(n):
    return n % 1 < 0.0001 or n % 1 > 0.999

def part1(lines):
    asteroids = set()
    maxX, maxY = len(lines[0]), len(lines)
    for y, line in enumerate(lines):
        for x, e in enumerate(line.strip()):
            assert e in ["#", "."], e
            if e == "#":
                asteroids.add((x, y))

    pairs = [tuple(sorted(pair)) for pair in itertools.combinations(asteroids, 2)]
    # line of sight pairs - True, False or None for don't know yet
    los = dict(zip(pairs, itertools.repeat(None)))
    los_count = defaultdict(int)

    def has_los(p, q, is_los):
        pair = tuple(sorted((p, q)))
        if (5, 8) in pair:
            print(pair, is_los)
        los[pair] = is_los

    for pair in pairs:
        if los[pair] is not None: continue
        #(5, 8), (8, 6)
        # m = -2 / 3
        # c = 11 1/3
        (x1, y1), (x2, y2) = pair
        try:
            m = (y2 - y1)/(x2 - x1)
            c = y1 - m * x1
            f = lambda x: m * x + c
            points = [(x, round(f(x))) for x in range(x1 + 1, x2 + 1) if is_whole(f(x))]
        except ZeroDivisionError:
            points = [(x1, y) for y in range(y1 + 1, y2 + 1)]

        asteroid_seen = False
        for x, y in points:

            if (x, y) in asteroids:
                has_los((x1, y1), (x, y), not asteroid_seen)
                asteroid_seen = True

    los_count = defaultdict(int)


    for p, q in los.keys():
        if los[(p, q)]:
            los_count[p] += 1
            los_count[q] += 1

    inn = []
    out = []
    for pair in los:
        if (5, 8) in pair:
            if los[pair]:
                inn.append(pair)
            else:
                out.append(pair)


    return max(los_count.items(), key=lambda i: i[1])

if __name__ == "__main__":
    input_loc = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'input')
    print(part1(open(input_loc).readlines()))
