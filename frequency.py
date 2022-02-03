def check_equal(arr):
    last = arr[0]

    for item in arr:
        if item != last:
            return False
        
        last = item
    
    return True

def isValid(s):
    # calculate the frequency dictionary
    dic = {}

    for char in s:
        if char not in dic:
            dic[char] = 0
        dic[char] += 1

    frequencies = list(dic.values())

    if check_equal(frequencies):
        return 'YES'
    
    # subtracting 1 to the ith element, check if 
    # the array contains the same frequency values
    for key in list(dic.keys()):
        dic[key] -= 1
        if dic[key] == 0:
            del dic[key]

        frequencies = list(dic.values())

        if check_equal(frequencies):
            return 'YES'
        
        if key not in dic:
            dic[key] = 0

        dic[key] += 1

    return 'NO'

assert(isValid('abc') == 'YES')
assert(isValid('abcc') == 'YES')
assert(isValid('abccc') == 'NO')
assert(isValid('aabbccddeefghi') == 'NO')
assert(isValid('abcdefghhgfedecba') == 'YES')
assert(isValid('aaa') == 'YES')
assert(isValid('aabbc') == 'YES')
