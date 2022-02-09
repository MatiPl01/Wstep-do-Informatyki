# Elapsed time: 217.88072499999998s

def get_divs(n: int) -> list:
	i = 1
	divs = []
	while i*i < n:
		if n % i == 0:
			divs.extend((i, n//i))
		i += 1
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
