# In this exercise we use Newton-Raphson frmula
def sqrt(num, *, eps: float = .000001) -> float:
	a = num
	b = 1
	while abs(a - b) > eps:
		a = (a + b) / 2
		b = num / a  # Num is equal to the field of the rectangle a * b = num
	return a


if __name__ == '__main__':
	num = 3
	print(sqrt(num))
