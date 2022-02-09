from math import sqrt
# Elapsed time: 107.7061254s


def get_divs(n: int) -> set:
	divs = {1, n}
	for d in range(2, int(sqrt(n))+1):
		if n % d == 0 and d not in divs:
			# d is prime so we check any multiplier of this number
			div = d
			while n % div == 0 and div not in divs:
				divs.update({div, n//div})
				div *= d

	return divs


if __name__ == '__main__':
	import time
	start_time = time.perf_counter()

	range_ = (2, 1_000_000)

	results = {}
	for n in range(2, range_[1]):
		if n not in results:
			acq_num = sum(get_divs(n)) - n
			if not (range_[0] <= acq_num <= range_[1]):
				continue
			acq_divs_sum = sum(get_divs(acq_num)) - acq_num
			if n == acq_divs_sum and n != acq_num:
				results[n] = acq_num
				results[acq_num] = n

	for pair in results.items():
		print(*pair)

	end_time = time.perf_counter()
	print(f'Elapsed time: {end_time - start_time}s')
