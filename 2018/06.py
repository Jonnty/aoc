import sys
import string
from collections import defaultdict

class color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'

coordinates = [tuple(map(int, l.strip().split(', '))) for l in sys.stdin.readlines() if l.strip()]

maxX = 0
minX = 0

maxY = 0
minY = 0

for x, y in coordinates:
    assert x > 0 and y > 0
    maxX, maxY = max(maxX, x), max(maxY, y)
    minY, minY = min(minY, x), min(minY, y)

d = 30

maxX = maxX + d
maxY = maxY + d

minX = minX - d
minY = minY - d


def valid(coord):
    #return coord[0] >= 0 and coord[0] <= maxX and coord[1] >= 0 and coord[1] <= maxY
    return True

def neighbours(coord):
    x = coord[0]
    y = coord[1]
    ns = [
        (x+1, y),
        (x-1, y),
        (x, y+1),
        (x, y-1)]
    return filter(valid, ns)

def print_world(world):
    for y in xrange(-100, 100):
        for x in xrange(-100, 100):
            try:
                if (x, y) in coordinates:
                    sys.stdout.write(color.UNDERLINE)
                    sys.stdout.write(color.BOLD)
                    sys.stdout.write(color.RED)
                if world[(x,y)] == '.':
                    sys.stdout.write('.')
                else:
                    sys.stdout.write(string.ascii_letters[world[(x,y)]])
                sys.stdout.write(color.END)
            except KeyError:
                sys.stdout.write(' ')
        print


world = {}

all_fringe_sets = [set([coord]) for coord in coordinates]

def diff_with_world(fs, world):
    return [f for f in fs if f not in world]

new_claims = True

last_counts = [0 for _ in xrange(len(coordinates))]
new_counts = last_counts[:]
stabilised = set()

for _ in xrange(80):

    new_claims = set()
    new_fringe_sets = [set() for _ in range(len(all_fringe_sets))]
    for i, fringes in enumerate(all_fringe_sets):
        for fringe in fringes:
            if fringe in new_claims and world[fringe] != str(i):
                world[fringe] = '.'
            else:
                world[fringe] = i
                new_counts[i] += 1
            new_claims.add(fringe)
            new_fringe_sets[i].update(neighbours(fringe))

    all_fringe_sets = [set(diff_with_world(fringes, world)) for fringes in new_fringe_sets]

    for i, count in enumerate(last_counts):
        if count == new_counts[i]:
            stabilised.add(i)

    last_counts = new_counts[:]


    # print_world(world)
    # print "---"

infinite_areas = [i for i, s in enumerate(all_fringe_sets) if len(s) > 0]

# print_world(world)

counts = defaultdict(int)

for w in world.values():
    if w not in stabilised: continue
    counts[w] += 1

for key in counts.keys():
    print key, counts[key]

print stabilised
print
print max(counts.values())
