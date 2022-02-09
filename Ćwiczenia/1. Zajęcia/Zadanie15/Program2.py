import math


def calc_pi(prec: int = 10**6) -> float:
	value = 1
	multiplier = math.sqrt(.5)
	for _ in range(prec):
		value *= multiplier
		multiplier = math.sqrt(.5 + .5 * multiplier)

	return 2 / value


if __name__ == '__main__':
	pi = calc_pi()
	print(pi)
