import math


def cos(value: 'radians') -> float:
	"""Calculates cos(value) using Maclaurin Series"""
	result = 0.
	for i in range(10):
		result += ((-1) ** i) * (value ** (2*i)) / math.factorial(2*i)
	result = round(result, 10)
	return result if result != 0 else 0.


if __name__ == '__main__':
	angle = math.pi / 3
	res = cos(angle)
	print(res)
