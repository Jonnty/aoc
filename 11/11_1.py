serial_number = 5791

def power_level(x, y):
	rack_id = x + 10
	power_level = rack_id * y
	power_level += serial_number
	power_level *= rack_id
	power_level = (power_level / 100) % 10
	power_level -= 5
	return power_level


levels = []
for x in xrange(1, 299):
	for y in xrange(1, 299):
		levels.append(((x, y), sum((power_level(i,j) for i in [x, x+1, x+2] for j in [y, y+1, y+2]))))

print max(levels, key=lambda l: l[1])[0]
