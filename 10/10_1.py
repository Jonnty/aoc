import sys, re

def minmax(ns):
	mini, maxi = ns[0], ns[0]
	for n in ns:
		mini = min(n, mini)
		maxi = max(n, maxi)
	return mini, maxi

positions = []
velocities = []
seconds = 0

last_positions = None
last_area = None

pattern = re.compile(R"position=<(-?\d+),(-?\d+)> velocity=<(-?\d+),(-?\d+)>", re.VERBOSE)
for line in sys.stdin.readlines():
	if not line.strip(): continue
	match = pattern.match(line.replace(' ', ''))
	positions.append((int(match.group(1)), int(match.group(2))))
	velocities.append((int(match.group(3)), int(match.group(4))))

area = 0

def tick(positions):
	global seconds
	new_positions = []
	for i, p in enumerate(positions):
		v = velocities[i]
		new_positions.append((p[0] + v[0], p[1] + v[1]))
	seconds += 1
	return new_positions

def print_sky(positions, minX, minY, maxX, maxY):
	border = 2
	positions_set = set(positions)
	for y in xrange(minY - border, maxY + border):
		for x in xrange(minX - border, maxX + border):
			if (x, y) in positions_set:
				sys.stdout.write("#")
			else:
				sys.stdout.write(".")
		print
	print

while True:
	pass
	minX, maxX = minmax([x for x, y in positions])
	minY, maxY = minmax([y for x, y in positions])
	area = (maxX - minX) * (maxY - minY)

	if last_area is not None and area > last_area:
		print_sky(last_positions, minX, minY, maxX, maxY)
		break

	last_area = area
	last_positions = positions

	positions = tick(positions)

print seconds - 1
