N = int(input('> '))

digits_powers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
last_power = 1
for num in range(1, N+1):
    num_str = str(num)

    # If number of digits of the checked number increases, multiply powers of appropriate digits
    if len(num_str) > last_power:
        last_power += 1
        for i in range(2, len(digits_powers)):
            digits_powers[i] *= i

    powers_sum = 0
    for digit in num_str:
        powers_sum += digits_powers[int(digit)]
        if powers_sum > num:
            break
    else:
        if powers_sum == num:
            print(num)
