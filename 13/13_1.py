import sys

turns = [-90, 0, 90]

carts = {}

class Cart:

	def __init__(self, location, heading):
		self.location = location
		self.next_turn = 0
		self.heading = heading

	def track(self):
		if self.heading in (0, 180):
			return "|"
		else:
			return  "-"

	def move(self, tracks):
		if tracks[self.location] == "+":
			self.heading = (self.heading + turns[self.next_turn]) % 360
			self.next_turn = (self.next_turn + 1) % len(turns)

		if tracks[self.location] == "/":
			if self.heading == 0:
				self.heading = 90
			elif self.heading == 90:
				self.heading = 0
			elif self.heading == 180:
				self.heading = 270
			elif self.heading == 270:
				self.heading = 180
			else:
				raise Exception("oops")


		if tracks[self.location] == "\\":
			if self.heading == 0:
				self.heading = 270
			elif self.heading == 90:
				self.heading = 180
			elif self.heading == 180:
				self.heading = 90
			elif self.heading == 270:
				self.heading = 0
			else:
				raise Exception("oops")

		prev_location = self.location

		if self.heading == 0:
			self.location = (self.location[0], self.location[1] - 1)
		elif self.heading == 90:
			self.location = (self.location[0] + 1, self.location[1])
		elif self.heading == 180:
			self.location = (self.location[0], self.location[1] + 1)
		elif self.heading == 270:
			self.location = (self.location[0] - 1, self.location[1])

		del carts[prev_location]

		if self.location in carts:
			del carts[self.location]
			print "CRASH at", self.location
		else:
			carts[self.location] = self


cart_symbols = {
	'^': lambda location: Cart( location, 0),
	'>': lambda location: Cart( location, 90),
	'v': lambda location: Cart( location, 180),
	'<': lambda location: Cart( location, 270),
}

tracks = {}

for y, line in enumerate( sys.stdin.readlines() ):
	for x, c in enumerate( line ):
		if c.isspace(): continue
		if c in cart_symbols.keys():
			cart = cart_symbols[c]((x, y))
			carts[x, y] = cart
			tracks[x, y] = cart.track()
		else:
			tracks[x, y] = c

while True:
	ordered = sorted(carts.keys(), key=lambda k: k[0] * k[1])
	for key in ordered:
		if key in carts: #might have been crashed into
			carts[key].move(tracks)
		if len(carts) <= 1:
			print carts.keys()
			sys.exit()
