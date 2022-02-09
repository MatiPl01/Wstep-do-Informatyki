# In this exercise we use 3D interpretation of Newton-Raphson formula
def cbrt(num, *, eps: float = 1e-10, round_digits: int = 8) -> float:
	a = num
	b = 1
	c = 1
	while abs(a - b) > eps or abs(a - c) > eps or abs(b - c) > eps:
		a = (a + b) / 2
		b = (b + c) / 2
		c = num / (a * b)
	return round(a, round_digits)


if __name__ == '__main__':
	num = 27
	print(cbrt(num))
