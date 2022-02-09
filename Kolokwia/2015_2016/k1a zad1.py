def is_prime_digit_init():
    primes = {2, 3, 5, 7}

    def is_prime_digit(num):
        return num in primes

    return is_prime_digit


is_prime_digit = is_prime_digit_init()


def all_prime_digits(num: int, base: int) -> bool:
    if not 2 <= base <= 16:
        raise ValueError(f'Wrong base passed. Expected integer from range 2 to 36, got {base}.)')

    while num:
        num, digit = divmod(num, base)
        if not is_prime_digit(digit):
            return False

    return True


def func(min_base, max_base):
    for base in range(min_base, max_base+1):
        if all_prime_digits(A, base):
            return True
    return False


if __name__ == '__main__':
    # A = 4324
    A = 42314
    bases = 2, 16
    print(func(*bases))
