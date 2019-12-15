import os, re, itertools

pattern = re.compile("<x=(-?\d+), y=(-?\d+), z=(-?\d+)>")

def sign(n):
    if n == 0 :
        return 0
    return int(n / abs(n))

class Moon:
    def __init__(self, x, y, z):
        self.position = (int(x), int(y), int(z))
        self.velocity = (0, 0, 0)

    def gravitate(self, moon):
        x, y, z = self.position
        X, Y, Z = moon.position
        vx, vy, vz = self.velocity
        dx, dy, dz = sign(X-x), sign(Y-y), sign(Z-z)
        self.velocity = vx + dx, vy + dy, vz + dz

    def step(self):
        x, y, z = self.position
        vx, vy, vz = self.velocity
        self.position = x + vx, y + vy, z + vz

    def tuples(self):
        return (self.position, self.velocity)

    def energy(self):
        x, y, z = self.position
        vx, vy, vz = self.velocity
        pot = abs(x) + abs(y) + abs(z)
        kin = abs(vx) + abs(vy) + abs(vz)
        return pot * kin

    def __repr__(self):
        return "pos=<x=%d, y=%d, z=%d>, vel=<x=%d, y=%d, z=%d>" % (*self.position, *self.velocity)

def part1(lines, steps=1000):
    moons = [Moon(*pattern.match(l).groups()) for l in lines]
    for _ in range(steps):
        for a, b in itertools.permutations(moons, 2):
            a.gravitate(b)
        for m in moons:
            m.step()
    return sum([m.energy() for m in moons])

if __name__ == "__main__":
    input_loc = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'input')
    print(part1(open(input_loc).readlines()))
