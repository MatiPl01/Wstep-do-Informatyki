n = int(input('> '))

# Generate Fibonacci numbers not greater than n
fibs = [1, 1]
while True:
    next_fib = fibs[-1] + fibs[-2]
    if next_fib > n:
        break
    fibs.append(next_fib)

# Find next matching number
is_found = False
next_num = n + 1

while not is_found:
    j = 0
    k = 1

    while True:
        subsequence_sum = 0
        for i in range(j, k):
            subsequence_sum += fibs[i]
        if subsequence_sum == next_num:
            break
        if subsequence_sum < next_num:
            k += 1
            if k > len(fibs):
                fibs.append(fibs[-1] + fibs[-2])
        else:
            j += 1
        if k == j:
            print(next_num)
            is_found = True
            break
    next_num += 1
