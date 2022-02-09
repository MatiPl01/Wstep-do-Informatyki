import random

seq_length = int(input('(length of a sequence) > '))
lst = [random.randint(-1000, 1000) for _ in range(seq_length)]
sorted_lst = sorted(lst, reverse=True)

print('Sorted sequence:', ' '.join(str(v) for v in sorted_lst), sep='\n')
print('10th element:', sorted_lst[9], end='\n\n')
print('Original sequence:', '\n'.join(str(v) for v in lst), sep='\n')
