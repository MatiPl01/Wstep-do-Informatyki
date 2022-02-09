# Using Maclaurin sequence we are able to represent the cos() function using a formula written below:
# cos(x) = 1 - x^2/2! + x^4/4! - x^6/6! + x^8/8! - ...
# We are summing up an infinite sequence made up of values every of which is calculated using this formlua:
# x_n = (-1)^n * x^(2n)/(2n)!
import math


def cos(x: 'value in radians', *, rounding: int = 6) -> float:
	result = 0
	n = 0
	while True:
		try:
			result += (-1) ** n * (x ** (n*2) / math.factorial(n*2))
			n += 1
		except OverflowError:
			return round(result, rounding)


if __name__ == '__main__':
	angle = 0
	print(cos(angle))
