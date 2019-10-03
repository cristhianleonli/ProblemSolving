def merge_the_tools(string, k):
    ratio = len(string) / k
    chunks = (string[i:i+k] for i in range(0, len(string), k))

    for chunk in chunks:
        res = ""
        for i in chunk:
            if i not in res:
                res += i

        print(res)
