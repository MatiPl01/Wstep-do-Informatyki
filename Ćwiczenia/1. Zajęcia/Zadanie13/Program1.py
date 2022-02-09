def nwd(a: int, b: int) -> int:
	return a if not b else nwd(b, a % b)


def _nww(a: int, b: int) -> int:
	return int(a * b / nwd(a, b))


def nww(*numbers) -> int:
	result = numbers[0]
	for num in numbers[1:]:
		result = _nww(result, num)
	return result


if __name__ == '__main__':
	a = 21
	b = -7
	c = -49
	res = nww(a, b, c)
	print(res)
