import random
from math import sqrt


def is_prime(num: int) -> bool:
    if num in {2, 3}:
        return True
    if not num % 2 or not num % 3 or num < 2:
        return False
    for div in range(5, int(sqrt(num))+1, 6):
        if not num % div or not num % (div + 2):
            return False
    return True


def random_bin_seq(length: int) -> list:
    return [random.randint(0, 1) for _ in range(length)]


def can_split_bin_seq_to_primes(seq, max_length=30) -> bool:

    def recur(begin_idx=0):
        if begin_idx == len(seq):
            return True

        num = 0
        for i in range(begin_idx, min(begin_idx + max_length, len(seq))):
            num = num * 2 + seq[i]  # Shift values to the left in each iteration and add next digit in the end

            if is_prime(num) and recur(i+1):
                return True

        return False

    return recur()


if __name__ == '__main__':
    random.seed(0)
    # N = 100
    # T = random_bin_seq(N)
    T = [1, 1, 1, 0, 1, 1, 0, 1]
    # T = [1, 1, 0, 1, 0, 0]
    print(T)
    print(can_split_bin_seq_to_primes(T))
