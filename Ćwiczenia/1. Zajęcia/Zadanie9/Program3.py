# Very efficient using simple LinkedList
from math import sqrt


class Node:
	def __init__(self, value):
		self.value = value
		self.next = None
		self.prev = None


class LinkedList:
	def __init__(self):
		self.head = None
		self.tail = self.head
		self.length = 0

	def __repr__(self):
		return f'{self.__class__.__name__}()'

	def __str__(self):
		return str(self.to_list())

	def __len__(self):
		return self.length

	def to_list(self):
		values = []
		current_node = self.head
		while True:
			if not current_node:
				break
			values.append(current_node.value)
			current_node = current_node.next
		return values

	def append(self, value):
		if self.length == 0:
			self.__create_first_node(value)
		else:
			new_node = Node(value)
			new_node.prev = self.tail
			self.tail.next = new_node
			self.tail = new_node
		self.length += 1

	def prepend(self, value):
		if self.length == 0:
			self.__create_first_node(value)
		else:
			new_node = Node(value)
			new_node.next = self.head
			self.head.prev = new_node
			self.head = new_node
		self.length += 1

	def __create_first_node(self, value):
		self.head = Node(value)
		self.tail = self.head


def get_divs(n: int) -> list:
	"""Returns all divisors of the number 'n'"""
	divs = LinkedList()
	i = int(sqrt(n))
	while i >= 1:
		if n % i == 0:
			divs.prepend(i)
			divs.append(int(n / i))
		i -= 1
	return divs.to_list()


if __name__ == '__main__':
	num = 28
	print(get_divs(num))
