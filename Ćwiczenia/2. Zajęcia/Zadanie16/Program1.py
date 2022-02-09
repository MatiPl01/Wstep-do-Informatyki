limit = 1000

for num in range(2, limit):
    digits_sum = 0
    for digit in str(num):
        digits_sum += int(digit)

    factors_digits_sum = 0
    num_cp = num
    for div in range(2, num):
        while num_cp > 1 and factors_digits_sum <= digits_sum and num_cp % div == 0:
            num_cp //= div
            if div < 10:
                factors_digits_sum += div
            else:
                for factor_digit in str(div):
                    factors_digits_sum += int(factor_digit)

    if digits_sum == factors_digits_sum:
        print(num)
