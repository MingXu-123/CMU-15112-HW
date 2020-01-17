def checkStr(s):
    stack = []
    for char in s:
        if char in ['(']:
            stack.append(char)
        else:
            if stack == []:
                return False
            top = stack.pop()
            if (top == "(" and char != ")"):
                return False
    return True


def permutations(a):
    if (len(a) == 0):
        return [ [] ]
    else:
        allPerms = [ ]
        for i in range(len(a)):
            partialPermutations = permutations(a[:i] + a[i+1:])
            for subPermutation in partialPermutations:
                allPerms.append([ a[i] ] + subPermutation)
        return allPerms


def generateValidParentheses(n):
    res = set()
    if n == 0:
        return set()
    elif n % 2 != 0:
        return set()
    numOfleft = int(n / 2)
    numOfRight = int(n / 2)
    s = []
    for i in range(numOfleft):
        s += ["("]
    for j in range(numOfRight):
        s += [")"]
    allPerms = permutations(s)
    allPermsStr = []
    for lst in allPerms:
        string = ""
        for char in lst:
            string += char
        allPermsStr += [string]
    for parent in allPermsStr:
        if checkStr(parent):
            res.add(parent)
    return res


def testGenerateValidParentheses():
    print("Testing generateValidParentheses...", end="")
    assert(generateValidParentheses(4) == { "(())", "()()" })
    assert(generateValidParentheses(6) == { "((()))", "()(())", "(())()", "(()())", "()()()" })
    assert(generateValidParentheses(5) == set())
    assert(generateValidParentheses(0) == set())
    print("Passed!")

# print(checkStr("(())"))
# print(checkStr("())("))
# print(checkStr(")()("))
print(generateValidParentheses(4))
print(generateValidParentheses(6))
print(generateValidParentheses(5))
print(generateValidParentheses(0))

def checkStr(s):
    stack = []
    for char in s:
        if char in ['(']:
            stack.append(char)
        else:
            if stack == []:
                return False
            top = stack.pop()
            if (top == "(" and char != ")"):
                return False
    return True


def permutations(a):
    if (len(a) == 0):
        return [ [] ]
    else:
        allPerms = [ ]
        for i in range(len(a)):
            partialPermutations = permutations(a[:i] + a[i+1:])
            for subPermutation in partialPermutations:
                allPerms.append([ a[i] ] + subPermutation)
        return allPerms


def generateValidParentheses(n):
    res = set()
    if n == 0:
        return set()
    elif n % 2 != 0:
        return set()
    numOfleft = int(n / 2)
    numOfRight = int(n / 2)
    s = []
    for i in range(numOfleft):
        s += ["("]
    for j in range(numOfRight):
        s += [")"]
    allPerms = permutations(s)
    allPermsStr = []
    for lst in allPerms:
        string = ""
        for char in lst:
            string += char
        allPermsStr += [string]
    for parent in allPermsStr:
        if checkStr(parent):
            res.add(parent)
    return res
