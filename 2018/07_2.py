import sys, re, string
from collections import defaultdict

edges = defaultdict(set)
dependency_counts = defaultdict(int)
dependents = set()

class Task:
	constant_factor = 60
	def __init__(self, name):
		self.name = name
		self.time_left = string.ascii_uppercase.index(name) + 1 + Task.constant_factor

	def tick(self):
		self.time_left -= 1

	def finished(self):
		return self.time_left <= 0

	def __repr__(self):
		return self.name + " " + str(self.time_left)

pattern = re.compile(R"Step (.) must be finished before step (.) can begin\.")
for line in sys.stdin.readlines():
	line = line.strip()
	if not line: continue

	match = pattern.match(line)
	src, dest = match.group(1), match.group(2)

	edges[src].add(dest)

	dependents.add(dest)
	dependency_counts[dest] += 1


#if it doesn't depend on anything, it's ready to go
ready = set(edges.keys()).difference(dependents)

tasks = {}
for name in ready.union(dependents):
	tasks[name] = Task(name)

in_progress = set()
workers = 5
order = []

duration = 0
while ready or in_progress:
	print in_progress, ready, tasks
	workers_idle = workers - len(in_progress)
	in_progress.update(sorted(ready)[:workers_idle])
	ready = ready.difference(in_progress)
	duration += 1
	for task in sorted(in_progress):
		tasks[task].tick()
		if tasks[task].finished():
			in_progress.remove(task)
			order.append(task)
			deps = edges[task]
			for dep in deps:
				dependency_counts[dep] -= 1
				if dependency_counts[dep] == 0:
					ready.add(dep)




print len(order)
print "".join(order)
print duration
