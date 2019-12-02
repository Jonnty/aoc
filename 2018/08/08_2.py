definition = list(reversed([int(n) for n in raw_input().split()]))

class Node:
	def __init__(self, num_children, num_fields):
		self.is_leaf = num_children == 0
		self.children_left = num_children
		self.fields_left = num_fields
		self.children = []
		self.value = 0

	def add_field(self, n):
		self.fields_left -= 1

		if self.is_leaf:
			self.value += n
		else:
			try:
				self.value += self.children[n-1].value
			except IndexError:
				pass

	def create_child(self, num_children, num_fields):
		self.children_left -= 1

		child = Node(num_children, num_fields)
		self.children.append(child)
		return child

root = Node(definition.pop(), definition.pop())
nodes = [root]

fields_sum = 0
while nodes:
	top = nodes[-1]
	if top.children_left:
		nodes.append(top.create_child(definition.pop(), definition.pop()))
	elif top.fields_left:
		top.add_field(definition.pop())
	else:
		#nothing left! let's move on to next node. this comment is dedicated to Rory James Munro, love you lots rory xxx
		nodes.pop()


assert len(definition) == 0
print root.value
