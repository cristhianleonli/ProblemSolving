import math


def locate_opponents(opponents, r_q, c_q):
    memo = {
        "t": [], "b": [], "r": [], "l": [],
        "tr": [], "br": [], "bl": [], "tl": []
    }

    for opponent in opponents:
        if opponent[1] == c_q and opponent[0] > r_q:
            memo["t"].append(opponent)

        if opponent[1] == c_q and opponent[0] < r_q:
            memo["b"].append(opponent)

        if opponent[0] == r_q and opponent[1] > c_q:
            memo["r"].append(opponent)

        if opponent[0] == r_q and opponent[1] < c_q:
            memo["l"].append(opponent)

        diff_r = opponent[0] - r_q
        diff_c = opponent[1] - c_q

        if abs(diff_r) == abs(diff_c):
            if diff_r >= 0 and diff_c >= 0:
                memo["tr"].append(opponent)

            if diff_r >= 0 and diff_c < 0:
                memo["tl"].append(opponent)

            if diff_r < 0 and diff_c >= 0:
                memo["br"].append(opponent)

            if diff_r < 0 and diff_c < 0:
                memo["bl"].append(opponent)

    return memo


def filter_repeated(opponents, r_q, c_q):
    for key in ["tr", "br", "bl", "tl"]:
        value = opponents[key]
        if len(value) > 1:
            minor = value[0]
            for point in value:
                diff = abs(point[0] - r_q)
                diff_minor = abs(minor[0] - r_q)
                if diff < diff_minor:
                    minor = point
            opponents[key] = [minor]

    for key in ["t", "r", "b", "l"]:
        value = opponents[key]
        if len(value) > 1:
            minor = value[0]
            for point in value:
                if key == "t":
                    if point[0] < minor[0]:
                        minor = point
                if key == "r":
                    if point[1] < minor[1]:
                        minor = point
                if key == "b":
                    if point[0] > minor[0]:
                        minor = point
                if key == "l":
                    if point[1] > minor[1]:
                        minor = point
            opponents[key] = [minor]

    return opponents


def queensAttack(n, k, r_q, c_q, obstacles):
    opponents = locate_opponents(obstacles, r_q, c_q)
    for i in opponents.keys():
        print(i, opponents[i])
    # opponents = filter_repeated(opponents, r_q, c_q)

    r = []
    for l in opponents.values():
        for i in l:
            r.append(i)

    print(r)
    pp(100, r, [r_q, c_q])

    empty = []
    counter = 0

    for key in opponents:
        value = opponents[key]
        if len(value) == 0:
            empty.append(key)
        else:
            for point in value:
                counter += abs(point[0] - r_q) + abs(point[1] - c_q) - 1

    # print(counter)
    # counter += count_by_empty(empty, n, r_q, c_q)
    return counter


def count_by_empty(empty, n, r_q, c_q):
    counter = 0

    for i in empty:
        if i == "t":
            counter += n - r_q
        if i == "b":
            counter += r_q - 1
        if i == "r":
            counter += n - c_q
        if i == "l":
            counter += c_q - 1
        if i == "tr":
            counter += min(n - r_q, n - c_q)
        if i == "br":
            counter += min(n - c_q, r_q - 1)
        if i == "bl":
            counter += min(r_q - 1, c_q - 1)
        if i == "tl":
            counter += min(n - r_q, c_q - 1)

    return counter


obstacles = [
    [54, 87], [64, 97], [42, 75], [32, 65], [42, 87], [32, 97], [54, 75],
    [64, 65], [48, 87], [48, 75], [54, 81], [42, 81], [45, 17], [14, 24],
    [35, 15], [95, 64], [63, 87], [25, 72], [71, 38], [96, 97], [16, 30],
    [60, 34], [31, 67], [26, 82], [20, 93], [81, 38], [51, 94], [75, 41],
    [79, 84], [79, 65], [76, 80], [52, 87], [81, 54], [89, 52], [20, 31],
    [10, 41], [32, 73], [83, 98], [87, 61], [82, 52], [80, 64], [82, 46],
    [49, 21], [73, 86], [37, 70], [43, 12], [94, 28], [10, 93], [52, 25],
    [50, 61], [52, 68], [52, 23], [60, 91], [79, 17], [93, 82], [12, 18],
    [75, 64], [69, 69], [94, 74], [61, 61], [46, 57], [67, 45], [96, 64],
    [83, 89], [58, 87], [76, 53], [79, 21], [94, 70], [16, 10], [50, 82],
    [92, 20], [40, 51], [49, 28], [51, 82], [35, 16], [15, 86], [78, 89],
    [41, 98], [70, 46], [79, 79], [24, 40], [91, 13], [59, 73], [35, 32],
    [40, 31], [14, 31], [71, 35], [96, 18], [27, 39], [28, 38], [41, 36],
    [31, 63], [52, 48], [81, 25], [49, 90], [32, 65], [25, 45], [63, 94],
    [89, 50], [43, 41]
]


def pp(n, abss, queen):
    l = []
    for i in range(n):
        r = []
        for j in range(n):
            r.append("-")
        l.append(r)

    for i in abss:
        x = i[0]
        y = i[1]
        a = -1 * (x - n)
        b = y - 1
        l[a][b] = "o"

    qa = -1 * (queen[0] - n)
    qb = queen[1] - 1
    l[a][b] = "q"

    with open('some.txt', 'w') as f:
        for i in l:
            s = "".join(i) + "\n"
            f.write(s)


print(queensAttack(100, 100, 48, 81, obstacles))


# pp(obstacles)
