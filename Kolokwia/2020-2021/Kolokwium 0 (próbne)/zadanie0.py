"""
Explanation of the method used is here: https://www.youtube.com/watch?v=zfzZ_PgSdbU
"""


def last_non_zero_factorial_digit_init():
    last_factorials_digits = 1, 2, 6, 4
    last_pow2_digits = 2, 4, 8, 6

    def last_non_zero_factorial_digit(num: int) -> int:
        if num < 5:
            return last_factorials_digits[max(num-1, 0)]

        remainder = num//5
        pow2 = last_pow2_digits[remainder % 4 - 1]
        mul = 1
        for n in range(remainder*5+1, num+1):
            mul = (mul * n) % 10

        return (last_non_zero_factorial_digit(remainder) * pow2 * mul) % 10

    return last_non_zero_factorial_digit


last_non_zero_factorial_digit = last_non_zero_factorial_digit_init()


if __name__ == '__main__':
    n = int(input())
    print(last_non_zero_factorial_digit(n))
