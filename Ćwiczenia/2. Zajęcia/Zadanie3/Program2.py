dec_num = input('> ')

# Check if the specified decimal number is a palindrome
for i in range(len(dec_num) // 2):
    if dec_num[i] != dec_num[-i-1]:
        print(f'{dec_num} is not a palindrome')
        break
else:
    print(f'{dec_num} is a palindrome')

# Check if a binary representation of the specified number is a palindrome
# Convert decimal number to the binary system
dec_num = int(dec_num)

# Find the 2 ** n greater than dec_num that is closest to the value of the dec_num
n = 0
base = 2
while base ** n < dec_num:
    n += 1
n -= 1

# Store subsequent digits of the binary number representation
bin_num_digits = []

while n >= 0:
    if base ** n <= dec_num:
        dec_num -= base ** n
        bin_num_digits.append('1')
    else:
        bin_num_digits.append('0')
    n -= 1

bin_num = ''.join(bin_num_digits)

for i in range(len(bin_num) // 2):
    if bin_num[i] != bin_num[-i-1]:
        print(f'{bin_num} is not a palindrome')
        break
else:
    print(f'{bin_num} is a palindrome')
