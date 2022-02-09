# Smart, fast and clean solution

def get_divs(n: int) -> list:
	"""Returns all divisors of the number 'n'"""
	divs = []
	i = 1
	while i*i < n:
		if n % i == 0:
			divs.extend((i, int(n/i)))
		i += 1
	return sorted(divs)


if __name__ == '__main__':
	num = 28
	print(get_divs(num))
