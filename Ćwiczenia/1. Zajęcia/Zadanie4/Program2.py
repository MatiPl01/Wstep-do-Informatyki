# Clean code solution
def int_sqrt(num: int) -> int:
	"""Calculates a square root of an integer.
	num must have an integer sqrt value in order to guarantee that function works properly"""
	a = 1
	r = 2
	values = [a]
	values_sum = a
	while values_sum < num:
		next_value = values[-1] + r
		values_sum += next_value
		values.append(next_value)

	center_idx = len(values) // 2
	if len(values) % 2 == 1:
		return values[center_idx]
	return sum(values[center_idx-1:center_idx+1]) // 2


if __name__ == '__main__':
	num = 81
	res = int_sqrt(num)
	print(res)
