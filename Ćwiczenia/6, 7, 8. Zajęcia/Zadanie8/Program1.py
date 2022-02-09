def can_weigh(mass: int, weights: [int]) -> bool:

    def recur(idx=0, remaining_mass=mass):
        if remaining_mass == 0:
            return True
        if idx == len(weights):
            return False

        return recur(idx+1, remaining_mass-weights[idx])\
            or recur(idx+1, remaining_mass+weights[idx])\
            or recur(idx+1, remaining_mass)

    return recur()


if __name__ == '__main__':
    mass = 15
    weights = [2, 7, 8, 3]
    print(can_weigh(mass, weights))
