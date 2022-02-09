# Clean code solution

def generate_fib(n: int) -> list:
	"""Generates Fibonacci sequence containing all the Fibonacci numbers that aren't greater than 'n'"""
	fibs = [0, 1]
	while fibs[-1] + fibs[-2] <= n:
		fibs.append(fibs[-1] + fibs[-2])
	return fibs


def get_matching_subseq(fibs: list, sum_: int) -> list:
	"""
	Searches for the subsequence of the Fibonacci sequence provided in which the sum of all
	the numbers is equal to the value 'sum_'
	"""
	i = current_sum = 0
	j = 1
	while i < j < len(fibs) and current_sum != sum_:
		current_sum = sum(fibs[i:j])
		if current_sum == sum_:
			return fibs[i:j]
		elif current_sum < sum_:
			j += 1
		else:
			i += 1
	return []


if __name__ == '__main__':
	given_sum = 123
	fib_seq = generate_fib(given_sum)
	matching_subseq = get_matching_subseq(fib_seq, given_sum)
	print(bool(matching_subseq), matching_subseq)
