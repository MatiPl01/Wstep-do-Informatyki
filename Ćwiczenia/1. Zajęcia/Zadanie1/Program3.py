# One variable solution using Golden Ratio approximation
def fib(n: int) -> int:
	return int((((1 + 5 ** .5) / 2) ** n) / (5 ** .5) + .5)


def print_fibs(n: int):
	for v in range(1, n+1):
		print(fib(v))


if __name__ == '__main__':
	nums_count = 10
	print_fibs(nums_count)
