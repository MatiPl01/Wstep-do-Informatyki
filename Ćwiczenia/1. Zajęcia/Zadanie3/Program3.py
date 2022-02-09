# Fastest and clean code solution

def generate_fib(n: int) -> list:
    """Generates Fibonacci sequence containing all the Fibonacci numbers that aren't greater than 'n'"""
    fibs = [0, 1]
    while True:
        new_fib = fibs[-1] + fibs[-2]
        if new_fib > n:
            break
        fibs.append(new_fib)
    return fibs


def get_matching_subseq(fibs: list, sum_: int) -> list:
    """
    Searches for the subsequence of the Fibonacci sequence provided in which the sum of all
    the numbers is equal to the value 'sum_'
    """
    current_sum = fibs[0]
    i = j = 0
    while i <= j < len(fibs):
        if current_sum == sum_:
            return fibs[i:j+1]
        elif current_sum < sum_:
            j += 1
            current_sum += fibs[j]
        else:
            current_sum -= fibs[i]
            i += 1
    return []


if __name__ == '__main__':
    given_sum = 123
    fib_seq = generate_fib(given_sum)
    matching_subseq = get_matching_subseq(fib_seq, given_sum)
    print(bool(matching_subseq), matching_subseq)
