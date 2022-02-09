import random

if __name__ == '__main__':
    n = int(input('(number of elements) > '))
    t = [random.randint(1, 1000) for _ in range(n)]

    for num in t:
        # num_cp = num
        while num > 0:
            num, digit = divmod(num, 10)
            if digit % 2 == 1:
                # print(num_cp, digit)
                break
        else:
            # print('not', num_cp, digit)
            print(False)
            break
    else:
        print(True)

'''
String loop:
0.013210599999996298
0.016015900000003747
0.010466300000008921 

for dgt in str(num):
    if int(dgt) % 2 == 1:
        break


String with conversion to set:
0.007883699999994498
0.019844199999996093
0.006683400000001782

even_digits = {'0', '2', '4', '6', '8'}

if set(str(num)) - even_digits:
    print(num)
    continue


Modulo:
0.009640600000013322
0.006672200000004125
0.008323799999998549
0.0049712999999931284

while num > 0:
    num, digit = divmod(num, 10)
    if digit % 2 == 1:
        break
'''
