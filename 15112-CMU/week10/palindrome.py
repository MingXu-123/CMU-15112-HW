def getSubStrings(s):
    res = []
    for i in range(len(s) + 1):
        for j in range(i, len(s)+1):
            currStr = s[i:j]
            print(currStr)
            if currStr == currStr[::-1]\
                    and len(currStr) != 1 \
                    and currStr != "":
                res.append(currStr)
    for c in s:
        res.append(c)
    return res

# print(getSubStrings("geeks"))
# print(getSubStrings("aaaa"))



def getSubStr(s):
    if len(s) == 1:
        return s
    else:
        partialStr = getSubStr(s[1:])
        res = []
        for subStr in partialStr:
            res.append(subStr)
            res.append(s[0] + subStr)
        return res

# print(getSubStr("aaaa"))
# print(getSubStr("geeks"))

def getSubStr(s):
    if len(s) == 1:
        return s
    else:
        partialStr = getSubStr(s[1:])
        res = []
        for subStr in partialStr:
            res.append(subStr)
            res.append(s[0] + subStr)
        return res

def isValid(char):
    if char == char[::-1]:
        return True

# Complete the substrCount function below.
def substrCount(n, s):
    res = []
    allSubStr = getSubStr(s)
    print(allSubStr)
    for char in allSubStr:
        if isValid(char):
            res.append(char)
    print(res)
    return len(res)

# print(substrCount(5, 'asasd'))
# print(getSubStr("asasd"))

def is_palindrome(s):
    if s == s[:: -1]:
        return True

def partition(s):
    res = []
    # Generate all the combination
    for i in range(1, len(s)):
        head = s[:i]
        if is_palindrome(head):
            rest = partition(s[i:])
            # print(rest)
            for elem in rest:
                res.append([head] + elem)
    if is_palindrome(s):
        res.append([s])
    return res


print(partition("geeks"))
print(partition("geeksabccbaabc"))


