if __name__ == '__main__':
    k = int(input())
    n = 1

    a_n = 1
    b_n = 2

    min_dist = abs(k - a_n)  # Placeholder value
    min_dist_n = 1
    min_dist_seq_name = 'a'

    while True:
        dist_a = abs(k - a_n)
        dist_b = abs(k - b_n)

        # print(n, a_n, dist_a, b_n, dist_b)

        if dist_a > min_dist and dist_b > min_dist:
            break  # Because both sequences are increasing we have to stop loop when a distance increases
        elif dist_a < dist_b < min_dist:
            min_dist = dist_a
            min_dist_n = n
            min_dist_seq_name = 'a'
        elif dist_b < min_dist:
            min_dist = dist_b
            min_dist_n = n
            min_dist_seq_name = 'b'

        n += 1
        b_n = a_n + b_n
        a_n = a_n + b_n / 3

    print(f"{min_dist_seq_name}{min_dist_n}")
