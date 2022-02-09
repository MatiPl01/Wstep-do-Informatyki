def is_odd(num: int) -> bool:
    return num % 2 == 1


def are_odd_and_equal(num1: int, num2: int) -> bool:
    return num1 == num2 and is_odd(num1) and is_odd(num2)


def odd_palindrome_length(lst: list, left_idx: int, right_idx: int) -> int:
    while 0 <= left_idx and right_idx < len(lst) and are_odd_and_equal(lst[left_idx], lst[right_idx]):
        left_idx -= 1
        right_idx += 1
    return right_idx - left_idx - 1


def longest_odd_palindrome(lst: list) -> int:
    max_length = 0
    start_idx = 0

    # Loop only while it is still possible to find the longest subsequence
    while len(lst)-start_idx-1 > max_length//2:
        # For palindromes of odd elements counts
        odd_length = odd_palindrome_length(lst, start_idx, start_idx)
        # For palindromes of even elements counts
        even_length = odd_palindrome_length(lst, start_idx, start_idx+1)

        curr_length = max(odd_length, even_length)

        if curr_length > max_length:
            max_length = curr_length

        start_idx += 1

    return max_length


if __name__ == '__main__':
    n = int(input())  # Number of elements
    t = [int(input()) for _ in range(n)]

    print(longest_odd_palindrome(t))

'''
16
1
3
1
8
9
2
3
2
1
8
0
1
7
9
7
1
'''
