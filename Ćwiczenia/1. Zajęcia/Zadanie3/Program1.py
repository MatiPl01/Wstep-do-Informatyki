# Simplest solution

given_sum = 123

# Generate the Fibonacci sequence
fibs = [0, 1]
while fibs[-1] + fibs[-2] < given_sum:
	fibs.append(fibs[-1] + fibs[-2])

# Look for the matching subsequence
i = current_sum = 0
j = 1
while i < j < len(fibs) and current_sum != given_sum:
	current_sum = sum(fibs[i:j])
	if current_sum == given_sum:
		print(True, fibs[i:j])
		break
	elif current_sum < given_sum:
		j += 1
	else:
		i += 1
