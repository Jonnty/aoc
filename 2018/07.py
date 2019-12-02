import sys, re
from collections import defaultdict

edges = defaultdict(set)
dependency_counts = defaultdict(int)
dependents = set()

pattern = re.compile(R"Step (.) must be finished before step (.) can begin\.")
for line in sys.stdin.readlines():
	line = line.strip()
	if not line: continue

	match = pattern.match(line)
	src = match.group(1)
	dest = match.group(2)

	edges[src].add(dest)

	dependents.add(dest)
	dependency_counts[dest] += 1

#if it doesn't depend on anything, it's ready to go
ready = set(edges.keys()).difference(dependents)

order = []
while ready:
	print ready
	next = min(ready)
	ready.remove(next)
	order.append(next)
	deps = edges[next]
	for dep in deps:
		dependency_counts[dep] -= 1
		if dependency_counts[dep] == 0:
			ready.add(dep)


print len(order)
print "".join(order)
