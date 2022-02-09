from math import factorial


def cacl_e(*, precision: int = 10**3) -> float:
	result = 0
	for i in range(precision+1):
		result += 1 / factorial(i)
	return result


if __name__ == '__main__':
	print(cacl_e())
