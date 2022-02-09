if __name__ == '__main__':
    n = int(input('(number of elements) > '))
    t = [int(input(f'({i}. element) > ')) for i in range(1, n+1)]

    lowest_val = greatest_val = t[0]
    lowest_val_count = greatest_val_count = 1
    for val in t[1:]:
        if val < lowest_val:
            lowest_val = val
            lowest_val_count = 1
        elif val > greatest_val:
            greatest_val = val
            greatest_val_count = 1
        else:
            if val == lowest_val:
                lowest_val_count += 1
            if val == greatest_val:
                greatest_val_count += 1

    print(lowest_val_count == greatest_val_count == 1)

''' e.g.
5
7
7
1
2
3
'''
