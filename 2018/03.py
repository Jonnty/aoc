import sys, re
from collections import defaultdict
import operator

pattern = re.compile( R'#(?P<pid>\d+) @ (?P<x>\d+),(?P<y>\d+): (?P<w>\d+)x(?P<h>\d+)')

claims = defaultdict(list)

for line in sys.stdin.readlines():
	if not line.strip(): continue

	m = pattern.match(line)

	pid = int(m.group('pid'))
	x = int(m.group('x'))
	y = int(m.group('y'))
	w = int(m.group('w'))
	h = int(m.group('h'))

	for xx in xrange(x, x + w):
		for yy in xrange(y, y + h):
			claims[(xx, yy)].append(pid)

print claims

all_ids = set()
overlapping_ids = set()

for square in claims.keys():
	all_ids.update(claims[square])
	if len(claims[square]) > 1:
		overlapping_ids.update(claims[square])

print all_ids
print
print overlapping_ids
print all_ids.difference(overlapping_ids)
