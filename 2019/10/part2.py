import os
import numpy as np
from math import pi



def angle(p):
    x, y = p
    a = np.degrees(np.arctan2(y, x)) + 90
    if a < 0:
         a += 360
    return a

def r(p):
    x, y = p
    return np.sqrt(x**2 + y**2)

def recentre(p, to):
    x, y = p
    tx, ty = to
    return (x - tx, y - ty)

def decentre(p, fromm):
    x, y = p
    fx, fy = fromm
    return (x + fx, y + fy)


def part2(lines, station=(11, 19)):
    asteroids = set()

    for y, line in enumerate(lines):
        for x, e in enumerate(line.strip()):
            assert e in ["#", "."], e
            if e == "#":
                asteroids.add((x, y))
    asteroids.remove(station)

    #station at 0, 0
    asteroids = [recentre(a, station) for a in asteroids]
    vapourized = []
    theta = -1
    while len(vapourized) < 200 and len(asteroids) > 0:
        print(asteroids, angle(asteroids[0]))
        targets = [a for a in asteroids if angle(a) > theta]
        if len(targets) == 0:
            #we've gone all the way around
            theta = -1
            continue
        target = min(targets, key=lambda a: (angle(a), r(a))) # sort by angle then closeness
        print(target, angle(target))
        asteroids.remove(target)
        vapourized.append(target)
        theta = angle(target)

    for v in vapourized:
        absolute = decentre(v, station)
        print(absolute)
    print()
    print(decentre(vapourized[199], station))







if __name__ == "__main__":
    input_loc = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'input')
    print(part2(open(input_loc).readlines()))
