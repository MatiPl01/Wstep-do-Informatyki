def can_weigh(mass: int, weights: [int]) -> ([int], [int]):

    def recur(idx=0, remaining_mass=mass, scale_pan1=[], scale_pan2=[]):
        if remaining_mass == 0:
            return scale_pan1, scale_pan2
        if idx == len(weights):
            return ()

        return recur(idx+1, remaining_mass+weights[idx], scale_pan1+[weights[idx]], scale_pan2)\
            or recur(idx+1, remaining_mass-weights[idx], scale_pan1, scale_pan2+[weights[idx]])\
            or recur(idx+1, remaining_mass, scale_pan1, scale_pan2)

    return recur()


if __name__ == '__main__':
    mass = 3
    weights = [2, 7, 8, 3]
    print(can_weigh(mass, weights))  # The first one scale pan is the one with our mass placed on
