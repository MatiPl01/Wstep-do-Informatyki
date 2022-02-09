# Another fast solution
from math import sqrt
import random
from functools import wraps
import time


def performance(reps: int = 1_000):
	def decorator(fn):
		@wraps(fn)
		def inner(*args, **kwargs):
			total_t = 0
			for _ in range(reps):
				start_t = time.perf_counter()
				res = fn(*args, **kwargs)
				end_t = time.perf_counter()
				total_t += (end_t - start_t)
			print(f'In average it took {total_t/reps:.4f}s to run a function')
			return res
		return inner
	return decorator


@performance(100)
def get_divs(n: int) -> list:
	if n == 0: return [...]  # 0 is divisible by everything except for 0

	divs = {1, n}
	for d in range(2, int(sqrt(n))+1):
		if n % d == 0 and d not in divs:
			# d is prime so we check any multiplier of this number
			div = d
			while n % div == 0 and div not in divs:
				divs.update({div, int(n / div)})
				div *= d

	return sorted(divs)


random_num = lambda digits_count: random.randint(10 ** (digits_count-1), 10 ** digits_count - 1)


if __name__ == '__main__':
	random.seed(0)
	num = random_num(10)
	dvs = get_divs(num)
	print(num, dvs)
