import sys, re

state_pattern = re.compile(R"initial state: ([#.]+)")
transform_pattern = re.compile(R"([#.]{5}) => ([.#])")

state = {}
transforms = {}

for line in sys.stdin.readlines():
	state_match = state_pattern.match(line.strip())

	if state_match:
		for i, e in enumerate(state_match.group(1)):
			state[i] = e

	transform_match = transform_pattern.match(line.strip())

	if transform_match:
		transforms[transform_match.group(1)] = transform_match.group(2)


for generation in xrange(50000000000):

	next_state = {}
	lo, hi = min(state.keys()), max(state.keys())
	for i in xrange(lo-5, lo):
		state[i] = '.'
	for i in xrange(hi+1, hi+5):
		state[i] = '.'


	next_state = {}
	for i in state.keys():
		context = []
		for j in xrange(i-2, i+3):
			context.append(state.get(j, '.'))
		#print "".join(context), transforms.get("".join(context), state[i])
		next_state[i] = transforms.get("".join(context), '.')
	state = next_state
	print str(generation+1).rjust(2), "".join([state[i] for i in xrange( -3, max(state.keys()) +1)])

print sum([k for k, v in state.iteritems() if v == '#'])
