import random
from pprint import pprint as pp


def random_squares(count: int, min_x: int, max_x: int, min_y: int, max_y: int) -> [(int, int, int, int)]:
    res = []
    for _ in range(count):
        x1 = random.randint(min_x, max_x-1)
        x2 = random.randint(x1, max_x)
        side_length = x2 - x1
        y1 = random.randint(min_y, max_y - side_length)
        y2 = y1 + side_length
        res.append((x1, x2, y1, y2))
    return res


def square_field(side_length) -> int:
    return side_length**2


def get_fields_sum(squares) -> int:
    return sum(square_field(sq[1] - sq[0]) for sq in squares)


def are_overlapping(sq1: '(x1, x2, y1, y2)', sq2: '(x1, x2, y1, y2)') -> bool:
    return (sq2[0] <= sq1[0] <= sq2[1] or sq1[0] <= sq2[0] <= sq1[1])\
       and (sq2[2] <= sq1[2] <= sq2[3] or sq1[2] <= sq2[2] <= sq1[3])


def are_all_disjoint(curr_sq: '(x1, x2, y1, y2)', squares: '[(x1, x2, y1, y2)]') -> bool:
    for square in squares:
        if are_overlapping(curr_sq, square):
            return False
    return True


def can_find_matching_squares(seq, squares_count, fields_sum) -> bool:

    def recur(idx=0, found_squares=()):
        if len(found_squares) == squares_count:
            return get_fields_sum(found_squares) == fields_sum
            # if get_fields_sum(found_squares) == fields_sum:
            #     print(*found_squares, sep='\n')
            #     return True
        if idx == len(seq):
            return False

        curr_square = seq[idx]
        if are_all_disjoint(curr_square, found_squares):
            return recur(idx+1, found_squares + (curr_square,)) or recur(idx+1, found_squares)
        else:
            return recur(idx+1, found_squares)

    return recur()


if __name__ == '__main__':
    random.seed(0)
    N = 50
    T = random_squares(N, -40, 40, -40, 40)
    # T = [
    #     (3, 6, 3, 6),
    #     (7, 8, 7, 8),
    #     (-3, -1, -3, -1),
    #     (-10, -5, -10, -5),
    #     (10, 12, 10, 12)
    # ]
    pp(T)
    print(can_find_matching_squares(T, 13, 2012))
