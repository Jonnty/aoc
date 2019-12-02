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

# class DoublyLinkedList:
# 	class Node:
# 		def

# 	def __init__(self,

def print_game(player, current_loc, game):
	print "[%d]" % (player + 1),
	for i, e in enumerate(game):
		if i == current_loc:
			sys.stdout.write(" ")
			sys.stdout.write(color.UNDERLINE)
		print e,
		if i == current_loc:
			sys.stdout.write(color.END)
			sys.stdout.write(" ")
	print

def get_max_score(players, final_points):
	scores = [0 for _ in xrange(players)]

	# set up fiddly initial bit
	game = [0, 1]
	next_marble = 2
	current_loc = 1
	while next_marble <= final_points:
		player = ((next_marble - 1) % players)
		if next_marble % 23:
			current_loc = (current_loc + 2) % len(game)
			if current_loc == 0:
				#list is circular so end and start are "same place", but this keeps output same as in task spec
				current_loc = len(game)
			game.insert(current_loc, next_marble)
		else:
			#divisible by 23 so *something entirely different happens*
			scores[player] += next_marble
			remove_loc = (current_loc - 7) % len(game)
			scores[player] += game.pop(remove_loc)
			current_loc = remove_loc % len(game)

		next_marble += 1
		#print_game(player, current_loc, game)
	return max(scores)


pattern = re.compile(R'(?P<players>\d+) players; last marble is worth (?P<final_points>\d+) points')

for line in sys.stdin.readlines():
	if not line.strip(): continue
	match = pattern.match(line.strip())
	players, final_points = int(match.group("players")), int(match.group("final_points"))
	print get_max_score(players, final_points)
