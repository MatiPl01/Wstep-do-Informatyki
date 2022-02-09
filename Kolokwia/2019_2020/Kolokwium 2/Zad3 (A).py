def fill_list(lst: list):
    print(f'Please provide {len(lst)} integers separated by newline.')
    for i in range(len(lst)):
        user_input = input(f'{i+1}. value > ')
        lst[i] = user_input


def remove_longest_constant_subsequence(lst: list) -> int:
    curr_count = 1
    prev_value = lst[0]
    value_to_remove = None
    one_longest_found = False
    max_count = 0

    for i in range(1, len(lst)):
        if prev_value == lst[i]:
            curr_count += 1
            if curr_count > max_count:
                max_count = curr_count
                value_to_remove = prev_value
                one_longest_found = True
            elif curr_count == max_count:
                one_longest_found = False
        else:
            curr_count = 1
            prev_value = lst[i]

    if one_longest_found:
        for i in range(len(lst)):
            if lst[i] == value_to_remove:
                break
        # Shift values to the left
        for i in range(i, len(lst)-max_count):
            lst[i] = lst[i+max_count]

        # Pop remaining values
        for _ in range(max_count):
            lst.pop()

    return max_count


if __name__ == '__main__':
    N = int(input('(N) > '))
    lst = [None]*N
    fill_list(lst)

    print(lst)
    print(remove_longest_constant_subsequence(lst))
    print(lst)


'''
15
1
3
3
3
5
7
11
13
13
1
2
2
2
2
3

16
1
3
3
3
3
5
7
11
13
13
1
2
2
2
2
3
'''
