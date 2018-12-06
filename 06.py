import sys

coordinates = [map(int, l.strip().split(', ')) for l in sys.stdin.readlines() if l.strip()]

maxX = 0
maxY = 0

for x, y in coordinates:
    assert x > 0 and y > 0
    maxX, maxY = max(maxX, x), max(maxY, y)

d = 20
grid = [[None] * (x + d)] * (y + d)


progress_made = True

while progress_made:
    for y, row in enumerate(grid):
        for
