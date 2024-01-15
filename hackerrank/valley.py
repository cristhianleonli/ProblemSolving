
def counting_valleys(steps, path):
    val = 0
    count = 0

    for char in path:
        step = 1 if char == 'U' else -1
        val += step

        if val == 0 and step == 1:
            count += 1
    
    return count

if __name__ == '__main__':

    cases = [
        ('DUDUDUDUDU', 5),
        ('UDDDUDUU', 1),
        ('UDDDUDUU', 1)
    ]

    for (test, expected) in cases:
        result = counting_valleys(8, test)
        print(result, expected)