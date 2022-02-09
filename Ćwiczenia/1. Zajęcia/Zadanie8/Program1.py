# Simplest solution (brute force)

n = 13

if n <= 1:
	print(False)
else:
	for i in range(2, n):
		if n % i == 0:
			print(False)
			break
	else:
		print(True)
