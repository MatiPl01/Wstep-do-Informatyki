# First approach: calculate all possible primes which have appropriate digits count
from math import sqrt

num1 = input('> ')  # 67
num2 = input('> ')  # 21

bounds = int(num1 + num2), int(num2 + num1)

num_primes = 0
for num in range(min(bounds), max(bounds)+1):
    for i in range(2, int(sqrt(num))+1):
        if num % i == 0:
            break
    else:
        prime_str = str(num)
        # print(prime_str)
        num1_dgt_idx = num2_dgt_idx = 0
        for prime_dgt in prime_str:
            if num1_dgt_idx < len(num1) and num1[num1_dgt_idx] == prime_dgt:
                num1_dgt_idx += 1
            elif num2_dgt_idx < len(num2) and num2[num2_dgt_idx] == prime_dgt:
                num2_dgt_idx += 1
            else:
                break
        else:
            num_primes += 1
            print(prime_str)

print(f'We can create {num_primes} primes.')
