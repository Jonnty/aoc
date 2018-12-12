import numpy as np

serial_number = 5791

def power_level(i, j):
	rack_id = i + 10
	power_level = rack_id * j
	power_level += serial_number
	power_level *= rack_id
	power_level = (power_level / 100) % 10
	power_level -= 5
	return power_level

levels = np.zeros((300,300))
sums = np.zeros((300,300))

for i in xrange(300):
	for j in xrange(300):
		levels[i,j] = power_level(i,j)

for i in xrange(300):
	for j in xrange(300):
		sums[i,j] = levels[i:, j:].sum()

square_sums_set = np.zeros((300,300,300))

def square_sum(i, j, size):
	i -= 1
	j -= 1
	return sums[i, j] - sums[(i + size), j] - sums[i, (j + size)] + sums[(i + size), (j + size)]



def squares():
	for i in xrange(300, 0, -1):
		for j in xrange(300, 0, -1):
			for size in xrange(1, min(301-i, 301-j)):
				params = (i, j, size)
				yield params, square_sum(*params)

print max(squares(), key=lambda l: l[1])[0]





"""
Find the fuel cell's rack ID, which is its X coordinate plus 10
Begin with a power level of the rack ID times the Y coordinate.
Increase the power level by the value of the grid serial number (your puzzle input).
Set the power level to itself multiplied by the rack ID.
Keep only the hundreds digit of the power level (so 12345 becomes 3; numbers with no hundreds digit become 0).
Subtract 5 from the power level.
"""
