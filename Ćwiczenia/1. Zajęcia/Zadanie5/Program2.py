# In this exercise we use Newton-Raphson frmula
# More precise solution using Decimal class
from decimal import Decimal


def sqrt(num, *, eps: Decimal = Decimal('.000000000000001')) -> Decimal:
	a = Decimal(num)
	b = 1
	while abs(a - b) > eps:
		a = (a + b) / 2
		b = num / a  # Num is equal to the field of the rectangle a * b = num
	return a


if __name__ == '__main__':
	num = 3
	print(repr(sqrt(num)))
