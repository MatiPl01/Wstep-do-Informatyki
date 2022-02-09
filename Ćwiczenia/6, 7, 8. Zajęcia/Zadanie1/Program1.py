from math import sqrt


def is_prime(num: int) -> bool:
    if num == 2:
        return True
    if not num % 2 or num < 2:
        return False

    for div in range(3, int(sqrt(num))+1):
        if not num % div:
            return False

    return True


def all_primes_from_digits(num: int) -> set:
    num = abs(num)  # If got a negative integer, make it positive (cross out a minus sing)
    result = set()

    def recur(n, inner_num=0, mul=1):
        if inner_num not in result and inner_num >= 10 and inner_num != num and is_prime(inner_num):
            result.add(inner_num)
        if n > 0:
            n, digit = divmod(n, 10)
            recur(n, digit * mul + inner_num, mul*10)
            recur(n, inner_num, mul)

    recur(num)

    return result


if __name__ == '__main__':
    print(all_primes_from_digits(137))
