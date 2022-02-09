from math import sqrt


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


def matches(vals_sum: int) -> bool:
    if vals_sum in {0, 1}:
        return True

    for num in range(2, int(sqrt(vals_sum))+1):
        power = 2
        while num ** power <= vals_sum:
            if num ** power == vals_sum:
                print(num, power, num**power)
                return True
            power += 1

    return False


def check_condition(lst1: list, lst2: list, total_length: int) -> bool:
    if len(lst1) + len(lst2) < total_length:
        return False

    part_1_length = min(len(lst1), total_length)
    part_2_length = max(total_length - len(lst1), 0)

    while part_1_length > 0 and part_2_length <= len(lst2):
        # Sum values of the lst1 part
        part1_part_sum = 0
        for i in range(part_1_length):
            part1_part_sum += lst1[i]

        # Sum values of the lst2 part
        part2_part_sum = 0
        for j in range(part_2_length):
            part2_part_sum += lst2[j]

        # Move in the lst1 list with the segment of a current part_1_length
        for i in range(part_1_length, len(lst1)):

            if part_2_length > 0:
                # Move in the lst2 with the segment of a current part_2_length
                for j in range(part_2_length, len(lst2)):
                    if matches(part1_part_sum + part2_part_sum):
                        return True
                    part2_part_sum += (lst2[j] - lst2[j-part_2_length])
            else:
                if matches(part1_part_sum):
                    return True

            part1_part_sum += (lst1[i] - lst1[i-part_1_length])

        # If couldn't have found appropriate sum, decrease part size of the lst1 and increase part sie of lst2
        part_1_length -= 1
        part_2_length += 1

    return False


if __name__ == '__main__':
    total_length = 24

    N = int(input('(N) > '))
    t1 = [0] * N
    t2 = [0] * N
    fill_list_ints(t1)
    fill_list_ints(t2)
    print(check_condition(t1, t2, total_length))

'''
16
14
58
2
45
48
43
14
3
59
35
24
56
82
15
86
65
51
36
70
65
4
6
75
56
81
67
98
79
71
24
54
62



 34
33
24
5
69
40
64
23
38
83
82
85
74
67
12
76
51
27
59
99
1
33
36
74
69
15
35
85
58
20
85
60
80
57
19
28
51
64
92
66
33
41
21
68
43
91
34
17
28
93
93
53
11
27
48
85
91
68
57
78
25
32
2
33
28
24
71
63
34



63
99
58
44
38
98
22
85
37
67
26
77
61
45
37
84
26
12
40
83
90
68
48
25
31
76
45
87
2
21
66
80
80
23
66
93
99
45
26
73
63
100
17
30
92
50
71
73
97
57
66
12
48
93
1
49
100
96
71
57
70
74
31
66
36
21
76
67
66
81
20
13
45
77
58
7
52
37
8
84
75
80
1
53
55
3
100
40
15
87
28
10
1
44
52
96
59
55
77
47
52
12
7
50
99
51
27
65
63
20
1
25
94
73
72
8
29
91
64
71
67
28
96
59
36
39
27
'''
