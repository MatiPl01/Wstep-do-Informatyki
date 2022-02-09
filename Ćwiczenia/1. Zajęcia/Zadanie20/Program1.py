import math

a_n = 3
b_n = 5
delta = 1e-10

while abs(a_n - b_n) > delta:
	a_n_cp = a_n
	a_n = math.sqrt(a_n * b_n)  # A_n+1 = sqrt(A_n) * B_n
	b_n = (a_n_cp + b_n) / 2    # B_n+1 = (A_n + B_n) / 2.0

print(a_n)
