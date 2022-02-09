def get_divs(n: int) -> list:
	"""Returns all divisors of the number 'n'"""
	divs = []
	i = 1
	while i*i < n:
		if n % i == 0:
			divs.extend((i, int(n/i)))
		i += 1
	return divs


if __name__ == '__main__':
	max_num = 1_000_000
	for n in range(1, max_num+1):
		sum_divs = sum(get_divs(n)) - n
		if sum_divs == n:
			print(n, end=' ')
