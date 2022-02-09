# Using closure
def seq_A(a1: 'initial value of a sequence'):
	val = a1
	formula = lambda v: (v % 2) * (3 * v + 1) + (1 - v % 2) * v / 2

	def next_A():
		nonlocal val
		val = formula(val)
		return val

	return next_A


def calc_num_steps_to_get_target(target: 'target value', start: 'starting value') -> int:
	steps = 0
	next_elem = seq_A(start)
	while True:
		steps += 1
		if next_elem() == target: return steps


if __name__ == '__main__':
	range_ = range(2, 10001)
	target = 1
	a1 = 0
	max_steps_count = 0
	for i in range_:
		steps_count = calc_num_steps_to_get_target(target, i)
		if steps_count > max_steps_count:
			max_steps_count = steps_count
			a1 = i
	print(a1)
