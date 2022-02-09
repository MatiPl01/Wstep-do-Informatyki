from math import sqrt


a = 2
b = 5
prec = 1e-10

while abs(a-b) > 1e-10:
	a, b = sqrt(a * b), (a + b) / 2

print(a)
