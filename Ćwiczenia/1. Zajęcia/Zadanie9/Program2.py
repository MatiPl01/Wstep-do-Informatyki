# Another smart solution, this time without sorting
# Uses inserting (which is somehow slow)
from math import sqrt


def get_divs(n: int) -> list:
	"""Returns all divisors of the number 'n'"""
	divs = []
	i = int(sqrt(n))
	while i >= 1:
		if n % i == 0:
			divs.insert(0, i)
			divs.append(int(n / i))
		i -= 1
	return divs


if __name__ == '__main__':
	num = 28
	print(get_divs(num))
