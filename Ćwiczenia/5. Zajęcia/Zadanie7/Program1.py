from complex import Complex, as_degrees


def solve_quadratic_equation(a, b, c):
    if a:
        a, b, c = (Complex.as_complex(val) for val in (a, b, c))
        delta = b**2 - 4*a*c
        delta_sqrt = delta.root(2)[0]  # Take first of the two solutions
        x1 = (-b-delta_sqrt)/(2*a)
        x2 = (-b+delta_sqrt)/(2*a)
        return x1, x2
    elif b:
        return -c/b,
    else:
        return None


if __name__ == '__main__':
    # 6x^2 + 4x + 1 = 0
    results = solve_quadratic_equation(6, 4, 1)
    print(*results)
    print(*(res.as_trigonometric(as_fraction=True) for res in results))

    # -8x^2 + 5x -7 = 0
    results = solve_quadratic_equation(-8, 5, -7)
    print(*results)
    print(*(as_degrees(res.arg()) for res in results))

    #x^2 - 6x - 91 = 0
    results = solve_quadratic_equation(1, -6, -91)
    print(*results)
    print(*(as_degrees(res.arg()) for res in results))

    #  5x + 3 = 0
    results = solve_quadratic_equation(0, 5, 3)
    print(*results)

    # x^2 - 2x + 1 = 0
    results = solve_quadratic_equation(1, 2, 1)
    print(*results)

    # x^2 - 1 = 0
    results = solve_quadratic_equation(1, 0, -1)
    print(*results)

    # (4+i)*x^2 + (-6+8i)*x - 4 = 0
    results = solve_quadratic_equation(Complex('4+i'), Complex('-6+8i'), -4)
    print(*results)
