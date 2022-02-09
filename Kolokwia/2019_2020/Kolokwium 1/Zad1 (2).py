def sieve_of_eratosthenes(num: int) -> set:
    primes = set()
    to_skip = set()

    for n in range(2, num+1):
        if n not in to_skip:
            primes.add(n)
            to_skip.update(range(n*n, num+1, n))

    return primes


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


def matches(values_sum: int) -> bool:
    primes = sieve_of_eratosthenes(values_sum)

    for prime in primes:
        if values_sum / prime in primes:
            # print(values_sum, prime, values_sum/prime)
            # print(len(primes))
            return True

    return False


def check_condition(lst1: list, lst2: list) -> bool:
    max_length = min(len(lst1), len(lst2))  # I use max() function to ensure that function will work in every case
    for part_length in range(1, max_length+1):
        # Store initial sums of the starting part od the lists
        part_1_sum = part_2_sum = 0
        for idx in range(part_length):
            part_1_sum += lst1[idx]
            part_2_sum += lst2[idx]

        for idx in range(part_length, max_length):
            if matches(part_1_sum + part_2_sum):
                return True

            part_1_sum += (lst1[idx] - lst1[idx-part_length])
            part_2_sum += (lst2[idx] - lst2[idx-part_length])

    return False


if __name__ == '__main__':
    total_length = 24

    N = int(input('(N) > '))
    t1 = [0] * N
    t2 = [0] * N
    fill_list_ints(t1)
    fill_list_ints(t2)
    print(check_condition(t1, t2))

'''
52
80856
91005
22581
50343
68529
77885
5222
25779
90724
6363
26557
78580
53001
81667
34350
48490
45527
95233
48973
16774
63581
73009
21774
56212
60339
68409
62199
73266
6427
95906
86826
27395
29168
7079
74540
69743
4619
48626
64211
595
70194
97706
53569
67206
90800
27635
65597
38066
79045
31061
97109
59140
59737
33609
27396
40514
94836
53977
82707
47833
5284
55059
84912
94999
54597
59589
42463
22024
83624
44174
69889
3645
39527
37671
66274
20585
40175
51919
11909
12326
89674
43786
4950
65553
18847
58437
56713
21257
67389
63314
83519
46556
83639
66703
92063
50678
71200
40488
85171
57594
25484
92143
67425
23365
'''