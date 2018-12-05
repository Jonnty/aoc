from collections import defaultdict
import sys

two_count = 0
three_count = 0

for line in sys.stdin.readlines():
	line = line.strip().lower()
	if not line: continue

	letter_counts = defaultdict(int)
	for c in line:
		letter_counts[c] += 1
	if 2 in letter_counts.values():
		two_count += 1
	if 3 in letter_counts.values():
		three_count += 1

print two_count
print three_count
print
print two_count * three_count
