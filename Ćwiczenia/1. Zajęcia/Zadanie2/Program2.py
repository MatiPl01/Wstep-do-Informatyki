# Much faster solution

def num_in_fib(checked_value: int, a: '1st value of a sequence' = 1, b: '2nd value of a sequence' = 1) -> bool:
	if a == checked_value or b == checked_value: return True
	while b < checked_value:
		a, b = b, a + b
	return b == checked_value


def get_inital_fib_values(num: int) -> tuple:
	sum_ = 3  # a + b
	while True:
		a = 1  # Reset the value of a in every loop
		while a < int(sum_/2):  # a has to be lower than or equal to sum_/2 (as b >= a)
			b = sum_ - a  # a + b == sum_ <=> b = sum_ - a
			if num_in_fib(num, a, b):
				return a, b
			a += 1
		sum_ += 1


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
