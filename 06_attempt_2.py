import sys

def dist(x1, y1, x2, y2):
    return abs(x1 - x2) + abs(y1 - y2)

distance_limit = 10000

coordinates = [tuple(map(int, l.strip().split(', '))) for l in sys.stdin.readlines() if l.strip()]

minX, minY = min([p[0] for p in coordinates]), min([p[1] for p in coordinates])
maxX, maxY = max([p[0] for p in coordinates]), max([p[1] for p in coordinates])

region = {}

region_limit = distance_limit / len(coordinates)

for i in xrange(minX - region_limit, maxX + region_limit):
    for j in xrange(minY - region_limit, maxY + region_limit):
        region[(i,j)] = 0

for x, y in coordinates:
    for i, j in region.keys():
        region[(i, j)] += dist(x, y, i, j)
        if region[(i, j)] >= distance_limit:
            del region[(i, j)]

print len(region)
