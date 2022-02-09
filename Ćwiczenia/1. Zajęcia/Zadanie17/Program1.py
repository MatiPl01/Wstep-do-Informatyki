# Precision is being limited by the number of repetitions

def fib_quotient(reps: 'how many values will be calculated', *, f1: int = 1, f2: int = 1) -> float:
	for _ in range(reps):
		f1, f2 = f2, f1 + f2
	return f2 / f1


if __name__ == '__main__':
	q = fib_quotient(10 ** 5)
	print(q)
