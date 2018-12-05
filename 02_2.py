from collections import defaultdict
import sys

two_count = 0
three_count = 0

bids = [line.strip().lower() for line in sys.stdin.readlines() if line.strip()]

for i, left in enumerate(bids):
	for right in bids[i+1:]:
		overlap = [ l for i, l in enumerate(left) if l == right[i]]
		if len(overlap) == len(left) - 1:
			print left
			print right
			print
			print "".join(overlap)
