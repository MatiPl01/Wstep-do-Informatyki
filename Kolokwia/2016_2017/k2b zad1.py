def generate_valid_sums(seq1, seq2):
    if len(seq1) != len(seq2):
        raise ValueError("Sequences are of different lengths. Please make sure you passed equal-length sequences.")

    def recur(idx=0, sum_=0):
        if idx == len(seq1):
            print(sum_)
            return 1

        return recur(idx+1, sum_ + seq1[idx])\
               + recur(idx+1, sum_ + seq2[idx])\
               + recur(idx+1, sum_ + seq1[idx] + seq2[idx])

    return recur()


if __name__ == '__main__':
    t1 = [1, 3, 2, 4]
    t2 = [9, 7, 4, 8]
    sums_count = generate_valid_sums(t1, t2)
    print(f'\nCount:\n{sums_count}')
