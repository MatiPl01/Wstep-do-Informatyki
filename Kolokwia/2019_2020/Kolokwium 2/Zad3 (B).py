def fill_list(lst: list):
    print(f'Please provide {len(lst)} integers separated by newline.')
    for i in range(len(lst)):
        user_input = input(f'{i+1}. value > ')
        lst[i] = user_input


def remove_shortest_constant_subsequence(lst: list) -> int:
    curr_count = 1
    prev_value = lst[0]
    value_to_remove = None
    one_shortest_found = False
    min_count = len(lst)

    for i in range(1, len(lst)):
        if prev_value == lst[i]:
            curr_count += 1
        else:
            if 1 < curr_count < min_count:
                value_to_remove = lst[i-1]
                one_shortest_found = True
                min_count = curr_count
            elif curr_count == min_count:
                one_shortest_found = False

            curr_count = 1
            prev_value = lst[i]

    if one_shortest_found:
        for i in range(len(lst)):
            if lst[i] == value_to_remove:
                break
        # Shift values to the left
        for i in range(i, len(lst)-min_count):
            lst[i] = lst[i+min_count]

        # Pop remaining values
        for _ in range(min_count):
            lst.pop()

    return min_count


if __name__ == '__main__':
    N = int(input('(N) > '))
    lst = [None]*N
    fill_list(lst)

    print(lst)
    print(remove_shortest_constant_subsequence(lst))
    print(lst)


'''
17
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
13 
1 
2 
2 
2 
3
'''
