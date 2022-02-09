import math


precision = 10 ** 6

value = 1
multiplier = math.sqrt(.5)
for _ in range(precision):
	value *= multiplier
	multiplier = math.sqrt(.5 + .5 * multiplier)

pi = 2 / value
print(pi)
