serial_number = 5791

def power_level(x, y):
	rack_id = x + 10
	power_level = rack_id * y
	power_level += serial_number
	power_level *= rack_id
	power_level = (power_level / 100) % 10
	power_level -= 5
	return power_level

square_sums = {}

def square_sum(x, y, size):

    if not square_sums.has_key((x, y, size)):
        if size == 1:
            square_sums[(x, y, size)] = power_level(x, y)
        else:
            square_sums[(x, y, size)] = \
            sum (power_level(i,y) for i in xrange(x, x + size)) + \
            sum (power_level(x,j) for j in xrange(y, y + size)) + \
            square_sum(x+1, y+1, size-1)
    return square_sums[(x, y, size)]


def squares():
	for x in xrange(300, 0, -1):
		print x
		for y in xrange(300, 0, -1):
			for size in xrange(1, min(301-x, 301-y)):
				params = (x, y, size)
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
