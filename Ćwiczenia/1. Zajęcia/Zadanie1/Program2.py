def print_fib(n: int):
	fibs = [1, 1]
	for _ in range(n-1):
		print(fibs[0])
		fibs[0], fibs[1] = fibs[1], sum(fibs)
	print(fibs[0])


if __name__ == '__main__':
	nums_count = 10
	print_fib(nums_count)
