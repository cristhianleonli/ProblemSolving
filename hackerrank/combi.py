from itertools import combinations


def clean_grid(grid):
    memo = {0: [], 2: []}

    for i in range(len(grid)):
        line = list(grid[i])
        row = []
        for j in range(len(line)):
            if line[j] == ".":
                memo[2].append([i, j])
            else:
                memo[0].append([i, j])
    return memo


def neighbours(index):
    x = index[0]
    y = index[1]

    return [[x + 1, y], [x - 1, y], [x, y + 1], [x, y - 1]]


def bomber_man(n, grid):
    memo = clean_grid(grid)
    pp(memo)

    for i in range(3, n+1):
        to_explode = memo[0]

        for index in to_explode:
            new = neighbours(index)
            for ne in new:


def pp(m):
    for i in m.keys():
        print(i, ",", m[i])


grid = [
    ".......",
    "...O...",
    "....O..",
    ".......",
    "OO.....",
    "OO....."
]
print(bomber_man(3, grid))
# print(solve(204619, range(99994)))
