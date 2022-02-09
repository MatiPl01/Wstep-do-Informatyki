def cacl_e(*, precision: int = 10**3) -> float:
	result = 0
	fact = 1
	for i in range(1, precision+1):
		result += 1 / fact
		fact *= i
	return result


if __name__ == '__main__':
	print(cacl_e())
