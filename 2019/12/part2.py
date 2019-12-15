import os, re, itertools

from functools import reduce

pattern = re.compile("<x=(-?\d+), y=(-?\d+), z=(-?\d+)>")

#https://stackoverflow.com/questions/147515/least-common-multiple-for-3-or-more-numbers
def gcd(a, b):
    """Return greatest common divisor using Euclid's Algorithm."""
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    """Return lowest common multiple."""
    return a * b // gcd(a, b)

def lcmm(*args):
    """Return lcm of args."""
    return reduce(lcm, args)

def sign(n):
    if n == 0 :
        return 0
    return int(n / abs(n))

class MoonDim:
    def __init__(self, p):
        self.position = int(p)
        self.velocity = 0

    def gravitate(self, moon):
        self.velocity += sign(moon.position - self.position)

    def step(self):
        self.position += self.velocity

    def pos_vel(self):
        return (self.position, self.velocity)

    def __repr__(self):
        return "pos=%d, vel=%d" % (self.position, self.velocity)

def find_repeat(dims):
    initial = [dim.pos_vel() for dim in dims]
    curr = None
    steps = 0
    while initial != curr:
        for a, b in itertools.permutations(dims, 2):
            a.gravitate(b)
        for d in dims:
            d.step()
        curr = [d.pos_vel() for d in dims]
        steps += 1
    return steps


def part2(lines, steps=1000):
    moons = [pattern.match(l).groups() for l in lines]

    xs = [MoonDim(m[0]) for m in moons]
    ys = [MoonDim(m[1]) for m in moons]
    zs = [MoonDim(m[2]) for m in moons]

    return lcmm(find_repeat(xs), find_repeat(ys), find_repeat(zs))

if __name__ == "__main__":
    input_loc = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'input')
    print(part2(open(input_loc).readlines()))
