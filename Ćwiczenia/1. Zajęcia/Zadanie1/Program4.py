# One of the simplest solutions
n = 10

a = 1
b = 1
for _ in range(n):
	print(a)
	temp = a
	a = b
	b = a + temp
