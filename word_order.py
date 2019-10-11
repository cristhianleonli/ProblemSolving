def order(words):
    keys = []
    mp = {}
    for i in words:
        if i not in mp:
            mp[i] = 0
            keys.append(i)
        mp[i] += 1

    print(len(keys))
    result = " ".join(str(mp[i]) for i in keys)
    print(result)


if __name__ == '__main__':
    words = []
    for _ in range(int(input())):
        words.append(str(raw_input().rstrip()))

    order(words)
