definition = list(reversed([int(n) for n in raw_input().split()]))

class Node:
	def __init__(self, num_children, num_fields):
		self.children_left = num_children
		self.fields_left = num_fields

nodes = [Node(definition.pop(), definition.pop())]

fields_sum = 0
while nodes:
	if nodes[-1].children_left:
		#next numbers must define a new node
		nodes[-1].children_left -= 1
		nodes.append(Node(definition.pop(), definition.pop()))
	elif nodes[-1].fields_left:
		#next number must be a field
		nodes[-1].fields_left -= 1
		fields_sum += definition.pop()
	else:
		#nothing left! let's process next node
		nodes.pop()


assert len(definition) == 0
print fields_sum
