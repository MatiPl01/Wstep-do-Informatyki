def print_fib(n: int):
	a = b = 1
	for _ in range(n-1):
		print(a)
		a, b = b, a + b
	print(a)


if __name__ == '__main__':
	nums_count = 10
	print_fib(nums_count)
