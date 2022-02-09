def fill_list_ints(lst: list):
    print(f'Please provide {len(lst)} integers separated by newline.')
    for i in range(len(lst)):
        while True:
            try:
                user_input = int(input(f'{i+1}. value > '))
                break
            except ValueError:
                print('Wrong value passed. Please try again.')
        lst[i] = user_input


def check_subset(lst: list) -> bool:

    def recur(count1=0, count2=0, sum1=0, sum2=0, checked_count=0):
        # Return result of searching if all values were checked
        if checked_count == len(lst):
            if sum1 and sum1 == sum2 and count1 == count2:
                return True
            return False

        # Else, search recursively. We have 3 possibilities (either we take a value and place in the first subset
        # or we take a value and place it in the second subset or we simply skip a value and move on to the next one)
        return recur(count1+1, count2, sum1+lst[checked_count], sum2, checked_count+1)\
            or recur(count1, count2+1, sum1, sum2+lst[checked_count], checked_count+1)\
            or recur(count1, count2, sum1, sum2, checked_count+1)

    return recur()


if __name__ == '__main__':
    N = int(input('(N) > '))
    t = [0] * N
    fill_list_ints(t)
    print(check_subset(t))

'''
10
0
0
1
2
2
1
0
0
3
5
'''
