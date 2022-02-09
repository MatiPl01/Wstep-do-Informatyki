def _NWD(a: int, b: int) -> int:
	return a if not b else NWD(b, a % b)


def NWD(*numbers) -> int:
	result = numbers[0]
	for num in numbers[1:]:
		result = _NWD(num, result)
	return result


if __name__ == '__main__':
	a = 466
	b = 231
	c = 34
	res = NWD(a, b, c)
	print(res)
