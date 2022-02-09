def sieve_of_eratosthenes(max_num: int) -> list:
    to_skip = set()
    primes = []
    for num in range(2, max_num+1):
        if num not in to_skip:
            to_skip.update(range(num*num, max_num+1, num))
            primes.append(num)
    return primes


if __name__ == '__main__':
    n = int(input('> '))

    # Sieve of Eratosthenes
    print(*sieve_of_eratosthenes(n))
