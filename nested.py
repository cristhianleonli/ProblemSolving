if __name__ == '__main__':
    scores = {}

    for _ in range(int(input())):
        name = input()
        score = float(input())

        if score not in scores:
            scores[score] = []
        scores[score].append(name)

    result = sorted(scores[sorted(scores.keys())[1]])
    print("\n".join(result))
