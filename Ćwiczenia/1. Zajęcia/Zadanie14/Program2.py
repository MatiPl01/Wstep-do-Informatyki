from functools import lru_cache


PI = 3.141592653589793


@lru_cache(maxsize=2**10)
def factorial(n: int) -> int:
	"""Calculates factorial of the number given"""
	return 1 if n <= 1 else n * factorial(n-1)


def cos(value: 'radians') -> float:
	"""Calculates cos(value) using Maclaurin Series"""
	result = 0.
	for i in range(10):
		result += ((-1) ** i) * (value ** (2*i)) / factorial(2*i)
	result = round(result, 10)
	return result if result != 0 else 0.


if __name__ == '__main__':
	angle = PI / 2
	print(cos(angle))
