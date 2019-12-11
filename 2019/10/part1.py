import os, itertools, sys
from collections import defaultdict

from math import gcd

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
        if los[pair] is not None: return
        los[pair] = is_los
        if is_los:
            los_count[p] += 1
            los_count[q] += 1

    for pair in pairs:
        if los[pair] is not None: continue
        (x1, y1), (x2, y2) = pair
        dx, dy = x2 - x1, y2 - y1
        d = gcd(dx, dy)
        dx, dy = dx / d, dy / d #minimum whole number steps

        x, y = x1 + dx, y1 + dy
        asteroid_seen = False
        while x <= x2 and y <= y2:
            if (x, y) in asteroids:
                has_los((x1, y1), (x, y), not asteroid_seen)
                asteroid_seen = True
            x, y = x + dx, y + dy
    los_count = defaultdict(int)


    for p, q in los.keys():
        if los[(p, q)]:
            los_count[p] += 1
            los_count[q] += 1
    print(los_count)

    for y in range(maxX):
        for x in range(maxY):
            if (x, y) in 
            sys.stdout.write(str(los_count.get((x, y), ".")))
        print()

    return max(los_count.items(), key=lambda i: i[1])








    # get ordered pairs and make LOS dict


if __name__ == "__main__":
    input_loc = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'input')
    print(part1(open(input_loc).readlines()))
