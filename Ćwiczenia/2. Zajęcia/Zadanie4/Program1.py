N = int(input('> '))

nums_found = 0
divs = (2, 3, 5)
for num in range(1, N+1):
    # Check if a number is divisible only by 2, 3 or 5
    num_cp = num
    for div in divs:
        while num % div == 0:
            num //= div

    if num == 1:
        nums_found += 1
        print(num_cp)

print(f'Found {nums_found} matching numbers in total')
