# Smart and fast solution with nice code formatting
# Version 2 (using for loop and sqrt function)
from math import sqrt


def is_prime(n: int) -> bool:
	"""Assesses whether the number 'n' is prime or not"""
	if n <= 1: return False
	for i in range(2, int(sqrt(n))+1):
		if n % i == 0: return False
	return True


if __name__ == '__main__':
	num = 13
	print(is_prime(num))
