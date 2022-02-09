from itertools import combinations


if __name__ == '__main__':
    num = input('number > ')
    div = int(input('divisor > '))

    nums_count = 0
    for digits_count in range(len(str(div)), len(num)+1):
        for combination in combinations(num, digits_count):
            current_sub_num = int(''.join(combination))
            if current_sub_num % div == 0:
                nums_count += 1
                print(current_sub_num)
    print(f'Numbers {nums_count} numbers')
