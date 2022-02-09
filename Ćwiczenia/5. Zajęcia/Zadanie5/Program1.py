def func(coords: list) -> bool:
    for (x1, y1) in coords:
        for (x2, y2) in coords:
            # We check if both points are placed on a line sloped at an 45 degrees angle
            if x2-x1 == y2-y1 and (x1 != x2 or y1 != y2):
                top_left_corner_found = bottom_right_corner_found = False
                for (x, y) in coords:
                    if (x != x1 or y != y1) and (x != x2 or y != y2):
                        if x == x1 and y == y2:
                            top_left_corner_found = True
                        elif x == x2 and y == y1:
                            bottom_right_corner_found = True
                        elif (x1 <= x <= x2 and y1 <= y <= y2) or (x1 >= x >= x2 and y1 >= y >= y2):
                            break
                else:
                    if top_left_corner_found and bottom_right_corner_found:
                        return True
    return False


if __name__ == '__main__':
    data = [(1, 1), (1, 5), (5, 1), (5, 5), (2, 3)]
    print(func(data))
