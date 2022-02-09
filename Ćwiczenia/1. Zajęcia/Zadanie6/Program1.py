from decimal import Decimal


if __name__ == '__main__':
	num = 2020

	eps = Decimal('.0000001')
	a = Decimal(0)
	b = Decimal(100)
	x = (a + b) / 2

	x_pow = x**x
	while abs(x_pow - num) > eps:
		if x_pow > 2020:  # That means the value of x is still to big -> we have to shrink the range to the left side
			b = x
		else:
			a = x
		x = (a + b) / 2
		x_pow = x**x
	# print(repr(x))
	print(x)
