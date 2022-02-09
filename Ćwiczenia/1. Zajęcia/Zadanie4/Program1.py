# 1 + 3 + 5 + 7 + 9 = n^2  ->  n = 5
num = 625

a = 1
r = 2
values = [a]
values_sum = a
while values_sum < num:
	next_value = values[-1] + r
	values_sum += next_value
	values.append(next_value)

center_idx = len(values) // 2
if len(values) % 2 == 1:
	print(values[center_idx])
else:
	print((values[center_idx-1] + values[center_idx]) // 2)
