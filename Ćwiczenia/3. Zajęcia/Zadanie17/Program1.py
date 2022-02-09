def sieve_of_eratosthenes(max_num: int):
    to_skip = set()
    primes = []
    for num in range(2, max_num+1):
        if num not in to_skip:
            to_skip.update(range(num * num, max_num+1, num))
            primes.append(num)
    return primes


def recur(seq):
    if len(seq) == 1:
        yield from seq[0]
    else:
        for val in seq[0]:
            for next_val in recur(seq[1:]):
                yield val + next_val


def get_prime_sums(seq1, seq2) -> list:
    values_sums = []
    for v1, v2 in zip(seq1, seq2):
        values_sums.append((v1, v2, v1 + v2))

    possible_sums = set(recur(values_sums))
    primes = sieve_of_eratosthenes(max(possible_sums))

    prime_sums = []
    for prime in primes:
        if prime in possible_sums:
            prime_sums.append(prime)

    return prime_sums


if __name__ == '__main__':
    t1 = [1, 3, 2, 4]
    t2 = [9, 7, 4, 8]

    sums = get_prime_sums(t1, t2)
    print(*sums, sep=' ')
