from math import sqrt
import random
from functools import wraps
import time


random_num = lambda digits_count: random.randint(10 ** (digits_count-1), 10 ** digits_count - 1)


def performance(reps: int = 1_000):
	def decorator(fn):
		@wraps(fn)
		def inner(*args, **kwargs):
			total_t = 0
			for _ in range(reps):
				start_t = time.perf_counter()
				res = fn(*args, **kwargs)
				end_t = time.perf_counter()
				total_t += (end_t - start_t)
			print(f'In average it took {total_t/reps:.4f}s to run a function')
			return res
		return inner
	return decorator


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


# Using i*i and traditional list
def get_divs1(n: int) -> list:
	"""Returns all divisors of the number 'n'"""
	divs = []
	i = 1
	while i*i < n:
		if n % i == 0:
			divs.extend((i, int(n/i)))
		i += 1
	return sorted(divs)


# Using sqrt() and traditional list
def get_divs2(n: int) -> list:
	"""Returns all divisors of the number 'n'"""
	divs = []
	i = int(sqrt(n))
	while i >= 1:
		if n % i == 0:
			divs.insert(0, i)
			divs.append(int(n / i))
		i -= 1
	return divs


# Using sqrt() and LinkedList
def get_divs3(n: int) -> list:
	"""Returns all divisors of the number 'n'"""
	divs = LinkedList()
	i = int(sqrt(n))
	while i >= 1:
		if n % i == 0:
			divs.prepend(i)
			divs.append(int(n / i))
		i -= 1
	return divs.to_list()


def get_divs_4(n: int) -> list:
	if n == 0: return [...]  # 0 is divisible by everything except for 0

	divs = {1, n}
	for d in range(2, int(sqrt(n))):
		if n % d == 0 and d not in divs:
			# d is prime so we check any multiplier of this number
			div = d
			while n % div == 0 and div not in divs:
				divs.update({div, int(n / div)})
				div *= d

	return sorted(divs)


if __name__ == '__main__':
	digits_count = 100
	repetitions = 10
	fn_name_begin = 'get_divs'
	globals_ = dict(globals())
	functions = (globals_[var_name] for var_name in globals_ if var_name.startswith(fn_name_begin))

	random.seed(0)  # Every time a random number will be the same
	rand_num = random_num(digits_count)
	functions = [performance(repetitions)(fn) for fn in functions]

	for fn in functions:
		print(fn)
		res = fn(rand_num)
		print(res, end='\n\n')
