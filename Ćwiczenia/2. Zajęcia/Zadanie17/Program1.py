"""
Zadanie 17. Napisac program wyliczajacy pierwiastek równania x**x = 2020 metoda stycznych.

Szczegółowe wyjaśnienie algorytmu poniżej:
https://www.youtube.com/watch?v=vxI8dp3itMc
"""
from math import log

# Prepare useful formulas to perform ongoing calculations
ln = lambda x: log(x)
f = lambda x: x**x - 2020
first_order_derivative = lambda x: x**x * (1 + ln(x))
second_order_derivative = lambda x: x**x * (1 + ln(x) + ln(x)**2) + x**(x-1)

# Determine a range that contains a solution and choose a starting (x0) number
for x in range(1, 2020):
	if f(x) >= 2020:
		if f(x) * second_order_derivative(x) < 0:
			x -= 1
		break

# Calculate a solution up to the specified precision
while True:
	prev_x = x
	x -= f(x) / first_order_derivative(x)
	if prev_x == x:
		break

print(x)
