import os
from collections import defaultdict
from itertools import chain

class Planet:
    def __init__(self, name):
        self.orbited_by = []
        self.name = name

    def is_orbited_by(self, planet):
        self.orbited_by.append(planet)

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

    def __repr__(self):
        return ",".join([self.name + ")" + p.name for p in self.orbited_by])


planets = {}
def planet(name):
    if not name in planets:
        planets[name] = Planet(name)
    return planets[name]

def process_input(lines):
    for line in lines:
        orbited, orbiter = line.strip().split(")")
        planet(orbited).is_orbited_by(planet(orbiter))

def part1():
    return planets["COM"].orbiter_count()

def part2():
    pass

if __name__ == "__main__":
    input_loc = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'input')
    process_input(open(input_loc).readlines())
    print("part1: " + str(part1()))
    print("part2: " + str(part2()))
