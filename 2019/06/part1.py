import os, functools
from collections import defaultdict
from itertools import chain

class Planet:
    def __init__(self, name):
        self.orbited_by = []
        self.all_orbiters_result = None
        self.name = name

    def is_orbited_by(self, planet):
        self.orbited_by.append(planet)

    #Memoize this as we'll use it a lot
    @functools.lru_cache(maxsize=None)
    def all_orbiters(self):
        #return a list of orbiters with the number of 'indirections'
        # one means it is a direct orbiter, 2 a direct of a direct, etc
        directs = [(p, 1) for p in self.orbited_by]
        indirects = []
        for planet in self.orbited_by:
            indirects.extend(planet.all_orbiters())
        updated_indirects = [(p, n+1) for p, n in indirects]
        return directs + updated_indirects

    def orbiter_count(self):
        return sum([n for p, n in self.all_orbiters()])

    def transfers_via_here(self, a, b):
        orbiters = dict([(p.name, n) for p, n in self.all_orbiters()])
        if not (a in orbiters and b in orbiters):
            return None
        return orbiters[a] + orbiters[b] - 2 # we care about orbited object, not a & b

    def min_transfers_between(self, a, b):
        transfer_counts = [p.transfers_via_here(a, b) for p, n in self.all_orbiters()]
        return min([c for c in transfer_counts if c is not None])

    def __repr__(self):
        return self.name

planets = {}
def planet(name):
    if not name in planets:
        planets[name] = Planet(name)
    return planets[name]

def process_input(lines):
    for line in lines:
        orbited, orbiter = line.strip().split(")")
        planet(orbited).is_orbited_by(planet(orbiter))
    planets

def part1():
    return planets["COM"].orbiter_count()

def part2():
    return planets["COM"].min_transfers_between("SAN", "YOU")

if __name__ == "__main__":
    input_loc = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'input')
    process_input(open(input_loc).readlines())
    print("part1: " + str(part1()))
    print("part2: " + str(part2()))
