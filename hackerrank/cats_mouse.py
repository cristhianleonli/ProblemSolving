def catAndMouse(x, y, z):
    if abs(z - y) > abs(z - x):
        return 'Cat A'

    if abs(z - y) < abs(z - x):
        return 'Cat B'

    return 'Mouse C'

assert(catAndMouse(2, 5, 4) == 'Cat B')
assert(catAndMouse(1, 2, 3) == 'Cat B')
assert(catAndMouse(1, 3, 2) == 'Mouse C')
assert(catAndMouse(1, 4, 2) == 'Cat A')