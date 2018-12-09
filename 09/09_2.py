import re,sys

class color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'

class DLLNode:
	def __init__(self, data, prev=None, next=None):
		self.data = data
		if prev is None: prev = self
		if next is None: next = self
		self.prev = prev
		self.next = next

	def insert_after(self, value):
		new = DLLNode(value, self, self.next)
		self.next.prev = new
		self.next = new
		if self.prev == self:
			#deal with single-item list special case
			self.prev = new
		return new

	def pop(self):
		self.prev.next = self.next
		self.next.prev = self.prev
		return self.data

	def back(self, n):
		return self.prev.prev.prev.prev.prev.prev.prev
		# node = self
		# for _ in xrange(n):
		# 	node = node.prev
		# return node

	def __repr__(self):
		return "data: %d next: %d prev: %d" % (self.data, self.next.data, self.prev.data)

def print_node(node, current):
	if node.data == current.data:
		sys.stdout.write(" ")
		sys.stdout.write(color.UNDERLINE)
		sys.stdout.write(color.RED)
	print str(node.data),
	if node.data == current.data:
		sys.stdout.write(color.END)
		sys.stdout.write(" ")

def print_game(root, current, player):
	print "[%d]" % (player + 1),
	print_node(root, current)
	node = root.next
	limit = 100
	while node.data != root.data and limit > 0:
		print_node(node, current)
		node = node.next
		limit -= 1
	print

def get_max_score(players, final_points):
	scores = [0 for _ in xrange(players)]

	# set up fiddly initial bit

	root = DLLNode(0)
	current = root

	for next_marble in xrange(1, final_points + 1):
		player = (next_marble - 1) % players

		if next_marble % 23:
			current = current.next.insert_after(next_marble)
		else:
			#divisible by 23 so *something entirely different happens*
			scores[player] += next_marble
			to_be_removed = current.back(7)

			current = to_be_removed.next
			scores[player] += to_be_removed.pop()
		#print_game(root, current, player)
	return max(scores)


pattern = re.compile(R'(?P<players>\d+) players; last marble is worth (?P<final_points>\d+) points')

for line in sys.stdin.readlines():
	if not line.strip(): continue
	match = pattern.match(line.strip())
	players, final_points = int(match.group("players")), int(match.group("final_points"))
	print get_max_score(players, final_points * 100)
	print
