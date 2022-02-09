def is_prime_init(primes):
    def is_prime(num: int):
        return num in primes
    return is_prime


is_prime = is_prime_init({2, 3, 5, 7})


def all_possible_distributions(initial_lst: list, nums: set):

    def recur(lst, remaining_nums):
        # print(lst, remaining_nums)
        if not remaining_nums:
            yield lst
        else:
            for num in remaining_nums:
                if not (is_prime(num) and is_prime(lst[-1])) and abs(num - lst[-1]) >= 2:
                    remaining_copy = remaining_nums.copy()
                    remaining_copy.remove(num)
                    yield from recur(lst + [num], remaining_copy)

    return recur(initial_lst.copy(), nums)


if __name__ == '__main__':
    numbers = set(range(2, 10))
    t = [1]
    print(*all_possible_distributions(t, numbers), sep='\n')
