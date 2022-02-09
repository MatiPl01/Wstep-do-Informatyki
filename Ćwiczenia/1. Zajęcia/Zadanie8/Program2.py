# Smart and fast solution with nice code formatting

def is_prime(n: int) -> bool:
	"""Assesses whether the number 'n' is prime or not"""
	if n <= 1: return False
	i = 2
	while i*i <= n:
		if n % i == 0: return False
		i += 1
	return True


if __name__ == '__main__':
	num = 13
	print(is_prime(num))
