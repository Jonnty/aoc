import sys
import string
import itertools
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

def neighbours(coord):
    x = coord[0]
    y = coord[1]
    ns = [
        (x+1, y),
        (x-1, y),
        (x, y+1),
        (x, y-1)]
    return ns
max_distance = 10000
regions = None

distances = defaultdict(int)
visited = defaultdict(int)
for coord in coordinates:
    region = set([coord])
    last_added = set([coord])
    visited[coord] += 1
    for i in xrange(1, max_distance):
        last_added = set(itertools.chain(*[neighbours(c) for c in last_added]))
        last_added = last_added.difference(region)
        if not coord == coordinates[0]:
            last_added = last_added.intersection(distances.keys()) #not required but maybe an optimisation??
        region.update(last_added)
        for add in last_added:
            distances[add] += i
            visited[add] += 1

# print distances
# print visited
# print len(coordinates)
# print distances[(4,4)], visited[(4,4)]

print len([dist[1] for dist in distances.iteritems() if dist[1] < max_distance and visited[dist[0]] == len(coordinates) ])
