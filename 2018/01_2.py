import sys

seen_frequencies = set()

frequency = 0

changes = [int(l) for l in sys.stdin.readlines() if l.strip()]

while True:
	for change in changes:
		if frequency in seen_frequencies:
			print frequency
			sys.exit()
		seen_frequencies.add(frequency)
		frequency += change

if frequency in seen_frequencies:
		print frequency

print seen_frequencies
