num = input('> ')
print(f'Number {num} is {"not " if num != num[::-1] else ""}a palindrome')
bin_num = bin(int(num))[2:]
print(f'Binary representation of number {num} ({bin_num}) is {"not " if bin_num != bin_num[::-1] else ""}a palindrome')
