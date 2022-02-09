def to_base(num: int, base: int) -> int:
    result = 0
    mul = 1
    while num:
        num, digit = divmod(num, base)
        result += mul * digit
        mul *= 10
    return result

# We will search for a non-increasing subsequence starting from back
# (it is the same as looking for a non-decreasing subsequence from the beginning)
def longest_non_decreasing_subsequence_length(num: int) -> int:
    max_length = curr_length = 1
    dgt = num % 10

    while num:
        prev_dgt = dgt
        num, dgt = divmod(num, 10)
        if dgt <= prev_dgt:
            curr_length += 1
            if curr_length > max_length:
                max_length = curr_length
        else:
            curr_length = 1

    return max_length if max_length > 1 else 0


def func(num: int, bases: tuple, searched_length: int) -> int:
    for base in range(bases[0], bases[1]+1):
        num_conv = to_base(num, base)
        curr_length = longest_non_decreasing_subsequence_length(num_conv)
        if curr_length == searched_length:
            # print(base, num_conv)
            return True

    return False


if __name__ == '__main__':
    bases = 2, 8
    searched_length = 4
    print(func(286, bases, searched_length))
