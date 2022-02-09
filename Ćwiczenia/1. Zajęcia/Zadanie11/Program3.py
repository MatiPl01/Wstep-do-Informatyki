from itertools import chain, cycle, accumulate  # last of which is Python 3 only
# Elapsed time: 22.088574100000002s


def factors(n):
	def prime_powers(n):
		# c goes through 2, 3, 5, then the infinite (6n+1, 6n+5) series
		for c in accumulate(chain([2, 1, 2], cycle([2, 4]))):
			if c * c > n: break
			if n % c: continue
			d, p = (), c
			while not n % c:
				n, p, d = n // c, p * c, d + (p,)
			yield d
		if n > 1: yield n,

	r = [1]
	for e in prime_powers(n):
		r += [a * b for a in r for b in e]
	return r


if __name__ == '__main__':
	import time
	start_time = time.perf_counter()

	range_ = (2, 1_000_000)

	results = {}
	for n in range(2, range_[1]):
		if n not in results:
			acq_num = sum(factors(n)) - n
			if not (range_[0] <= acq_num <= range_[1]):
				continue
			acq_divs_sum = sum(factors(acq_num)) - acq_num
			if n == acq_divs_sum and n != acq_num:
				results[n] = acq_num
				results[acq_num] = n

	for pair in results.items():
		print(*pair)

	end_time = time.perf_counter()
	print(f'Elapsed time: {end_time - start_time}s')
