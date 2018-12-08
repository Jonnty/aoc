import sys

coordinates = [tuple(map(int, l.strip().split(', '))) for l in sys.stdin.readlines() if l.strip()]


region = {}

#set up search space with radius of 1000 from first item

def dist(x1, y1, x2, y2):
    return abs(x1 - x2) + abs(y1 - y2)


x, y = coordinates[0]

region_size = 10000

def all_within_radius((x, y), radius):
    for i in xrange(x - region_size, x + region_size):
        for j in xrange(y - (region_size - i), y + (region_size - i)):
            distance = dist(x, y, i, j)
            if distance >= radius:
                continue
            yield (i, j), distance

for coord, distance in all_within_radius(coordinates[0], region_size):
    region[coord] = distance

for x, y in coordinates[1:]:

    for i, j in region.keys():
        region[(i, j)] += dist(x, y, i, j)
        if region[(i, j)] >= region_size:
            del region[(i, j)]

print len(region)
