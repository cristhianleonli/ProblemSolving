def getMoneySpent(keyboards, drives, b):
    result = -1

    for keyboard in keyboards:
        for drive in drives:

            total = keyboard + drive

            if total <= b and total > result:
                result = total
    
    return result

assert(getMoneySpent([3, 1], [5, 2, 8], 10) == 9)
assert(getMoneySpent([4], [5], 5) == -1)
