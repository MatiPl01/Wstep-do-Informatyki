# Precision is being limited by the time specified to perform calculations
import time


def fib_quotient(time_limit: 'how long will the calculation last', *, f1: int = 1, f2: int = 1) -> float:
	start_time = time.time()
	reps = 0
	while time.time() - start_time < time_limit:
		f1, f2 = f2, f1 + f2
		reps += 1
	print(f'Calculated: fib({reps+2})/fib({reps+1})\t- {reps} repetitions')
	return f2 / f1


if __name__ == '__main__':
	q = fib_quotient(2)
	print(q)
