# The worst solution of many possible solutions
# I skipped using while loops, recursion (which will fail when calculating 1000000 fibonacci numbers) and so on
n = 10

a = 1
b = 1

i = 0
while i < n:
	print(a)
	temp = a
	a = b
	b = a + temp
	i += 1
