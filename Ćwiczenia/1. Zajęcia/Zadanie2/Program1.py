# Brute force solution

def num_in_fib(checked_value: int, a: '1st value of a sequence' = 1, b: '2nd value of a sequence' = 1) -> bool:
	if a == checked_value or b == checked_value: return True
	while b < checked_value:
		a, b = b, a + b
	return b == checked_value


def get_inital_fib_values(num: int) -> tuple:
	lowest = num, num
	for a in range(1, num+1):
		for b in range(a, num+1):
			if a*2 > sum(lowest):
				break
			if num_in_fib(num, a, b) and a + b < sum(lowest):
				lowest = a, b
	return lowest


if __name__ == '__main__':
	num = 2020
	values = get_inital_fib_values(num)
	print(values)

	# Testing
	a, b = values
	while a < num:
		print(a, end=' ')
		a, b = b, a + b
	print(a)
