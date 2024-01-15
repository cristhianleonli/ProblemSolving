
def birthdayCakeCandles(n, password):
    min_chars = 6
    numbers = "0123456789"
    lower_case = "abcdefghijklmnopqrstuvwxyz"
    upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    special_characters = "!@#$%^&*()-+"

    data = {"n": 0, "l": 0, "u": 0, "s": 0}
    for i in password:
        if i in numbers:
            data["n"] += 1
        if i in lower_case:
            data["l"] += 1
        if i in upper_case:
            data["u"] += 1
        if i in special_characters:
            data["s"] += 1

    mini = 0
    for i in data.keys():
        if data[i] == 0:
            mini += 1

    if mini == 0:
        return 0 if min_chars - len(password) < 0 else min_chars - len(password)

    if mini + len(password) >= min_chars:
        return mini

    return min_chars - len(password)


assert(birthdayCakeCandles(3, "Ab1") == 3)
assert(birthdayCakeCandles(3, "11111") == 3)
assert(birthdayCakeCandles(3, "Ab%1") == 2)
assert(birthdayCakeCandles(3, "Abb%") == 2)
assert(birthdayCakeCandles(3, "Ab$1er") == 0)
