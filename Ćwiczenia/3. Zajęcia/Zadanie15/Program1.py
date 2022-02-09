def generate_fib() -> int:
    """Returns subsequent values of the Fibonacci sequence"""
    a = 1
    b = 1
    while True:
        yield a
        a, b = b, a + b


def is_prime(num: int) -> bool:
    """Assesses whether a number 'num' is prime or not"""
    if num <= 1: return True
    for div in range(2, int(num**.5)+1):
        if num % div == 0:
            return False
    return True


if __name__ == '__main__':
    t = [x for x in range(2, 1000, 2)]
    fib = generate_fib()

    prime_found = False
    all_fibs_composite = True

    next_fib = next(fib)
    for idx, val in enumerate(t):
        if idx == next_fib:
            if is_prime(val):
                all_fibs_composite = False
                break
            next_fib = next(fib)
        elif not prime_found and is_prime(val):
            prime_found = True

    print(all_fibs_composite and prime_found)
