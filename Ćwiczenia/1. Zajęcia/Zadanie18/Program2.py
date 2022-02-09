# In this exercise we use a proper Newton-Raphson method using derivation
"""
Explanation is here:
https://www.youtube.com/watch?v=nRbsfnUftT4
"""


class NotWorkingError(Exception):
	...


# ~ 100x slower than built-in log function in the math library
def log(number, base, *, eps: 'precision' = 1e-10) -> float:
	"""Returns log with specified base of the num number
	Result is calculated using bisection method
	"""
	# log_a(b) = c  <=>  a ** c = b
	a = base
	b = number

	# Check if specified numbers are correct
	if not (a > 0 and a != 1):
		raise ValueError('base must be greater than 0 and not equal to 1')
	if not (b > 0):
		raise ValueError('number must be greater than 0')
	if a == b:
		return 1.
	if b == 1:
		return 0.

	c1 = c2 = a_pow_c2 = 0
	reverse_bisection = False

	# Find nearest integer exponents to the searching c
	if b > a > 1:
		print(1)
		while True:
			c2 += 1
			a_pow_c2 = a ** c2
			if a_pow_c2 >= b:
				break
		c1 = c2 - 1

	elif a > 1 and a > b:
		print(2)
		if b < 1:
			reverse_bisection = True
			while True:
				c2 -= 1
				a_pow_c2 = a ** c2
				if a_pow_c2 <= b:
					break
			c1 = c2 + 1
		else:
			c1, c2 = 0, 1

	elif b < a < 1:
		print(3)
		reverse_bisection = True
		while True:
			c2 += 1
			a_pow_c2 = a ** c2
			if a_pow_c2 <= b:
				break
		c1 = c2 - 1

	elif a < 1 and a < b:
		print(4)
		if b > 1:
			while True:
				c2 -= 1
				a_pow_c2 = a ** c2
				if a_pow_c2 >= b:
					break
			c1 = c2 + 1
		else:
			reverse_bisection = True
			c1, c2 = 0, 1

	if a_pow_c2 == b:
		return float(c2)

	# Start searching for a proper c exponent using bisection
	# print('reversed', reverse_bisection)
	print(f'log{a}({b}) in ({c1}, {c2})')
	print(f'result in ({a ** c1}, {a ** c2})')

	while True:
		c = (c1 + c2) / 2
		a_pow_c = a ** c
		if abs(a_pow_c - b) <= eps:
			return c
		if a_pow_c > b:
			if reverse_bisection:
				c1 = c
			else:
				c2 = c
		else:
			if reverse_bisection:
				c2 = c
			else:
				c1 = c
		if c == c1 == c2:
			raise NotWorkingError('not working')
		print(c1, c2, c)
		print('b', a_pow_c)


def log10(num, *, eps: 'precision' = 1e-10) -> float:
	"""Returns log with specified base 10 of the num number"""
	return log(10, num, eps=eps)


def root(n: 'n-th root', num: 'a number which will be root calculated of', *, eps: 'precision' = 1e-10) -> float:
	"""Calculates n-th root of a given number num using Newton-Raphson method"""
	x = 1
	while abs(x**n - num) > eps:
		x -= (x**n - num) / (n * x ** (n-1))
	return round(x, int(abs(log10(eps))))


# print(root(3, 27))

# import math
#
# num = .42
# base = .3123
#
# print(math.log(num, base))
# print()
# print(log(num, base))



import math, time, random


def perf(fns=(), args=(), reps=10**5):
	passed = []

	for fn in fns:
		start = time.perf_counter()
		for _ in range(reps):
			res = fn(*args)
		end = time.perf_counter()
		print(fn)
		print(res)
		print('Total time:', end - start)
		print('Avg time:', (end - start) / reps)
		print()


# perf((math.log, log), (2, 3))

reps = 1000
max_num = 2
max_base = 2
tolerance = 1e-8
fns = log, math.log

passed = 0
checked = 0

random.seed(2)

for i in range(reps):
	number = random.uniform(0, max_num)
	base = random.uniform(0, max_base)
	args = number, base
	try:
		print('a', base, 'b', number, math.log(number, base))
		res1, res2 = map(lambda fn: fn(*args), fns)
		print()
		checked += 1
		if abs(res1 - res2) <= tolerance:
			passed += 1
	except NotWorkingError:
		print("!!!! ERROR !!!!")
		break
	except Exception as e:
		print(e)

print(passed, checked)
