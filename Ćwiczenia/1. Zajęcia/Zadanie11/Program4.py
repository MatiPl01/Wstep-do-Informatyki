# Elapsed time: 472.9509643s

def prime_eratosthenes(n):
	checked = set()
	primes = {}
	for i in range(2, n+1):
		if i not in checked:
			primes[i] = True
			checked.update(range(i*i, n+1, i))
	return primes


def get_prime_factors(n: int) -> dict:
	"""Calculates prime factor of the number given and returns a dictionary
	containing all prime factor and their max possible counts
	"""
	prime_divs = {}
	for prime_div in primes:
		if prime_div > n: break
		while n % prime_div == 0:
			prime_divs.setdefault(prime_div, 0)
			prime_divs[prime_div] += 1
			n //= prime_div
	return prime_divs


def calc_all_factors(prime_factors: dict) -> list:
	"""Basing on values of prime factors of the number function calculates
	all possible factors of this number
	"""
	divs = [1]
	for div, count in prime_factors.items():
		for i in range(1, count + 1):
			if i > 1:
				new_divs = [existing_div * div for existing_div in divs[-len(new_divs):]]
			else:
				new_divs = [existing_div * div for existing_div in divs]
			divs.extend(new_divs)
	return divs


def get_factors_sum(n: int) -> int:
	"""Calculates a sum of all the number's factors (excluding a number itself)"""
	prime_factors = get_prime_factors(n)
	all_factors = calc_all_factors(prime_factors)  # Returned factor are in an ascending order
	return sum(all_factors[:-1])


if __name__ == '__main__':
	import time
	start_time = time.perf_counter()

	checked_range = (2, 1_000_000)
	primes = prime_eratosthenes(checked_range[1])

	friendly_pairs = {}
	for num in range(1, checked_range[-1]+1):
		if num in primes or num in friendly_pairs: continue

		friendly_num = get_factors_sum(num)
		if checked_range[0] < friendly_num < checked_range[1] and get_factors_sum(friendly_num) == num:
			friendly_pairs[num] = friendly_num
			friendly_pairs[friendly_num] = num
			print(num, friendly_num)

	end_time = time.perf_counter()
	print(f'Elapsed time: {end_time - start_time}s')
