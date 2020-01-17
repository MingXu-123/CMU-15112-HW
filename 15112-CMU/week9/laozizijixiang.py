def generate(left, right, string, res):
    if left == 0 and right == 0:
        res.add(string)
        return res
    else:
        if left > 0:
            generate(left - 1, right, string + '(', res)
        if right > left:
            generate(left, right - 1, string + ')', res)


def generateValidParentheses(n):
    res = set()
    if n == 0:
        return set()
    elif n % 2 != 0:
        return set()
    left, right = (n / 2), (n / 2)
    generate(left, right, "", res)
    return res


def testGenerateValidParentheses():
    print("Testing generateValidParentheses...", end="")
    assert(generateValidParentheses(4) == { "(())", "()()" })
    assert(generateValidParentheses(6) == { "((()))", "()(())", "(())()", "(()())", "()()()" })
    assert(generateValidParentheses(5) == set())
    assert(generateValidParentheses(0) == set())
    print("Passed!")

# print(generateValidParentheses(4))
# print(generateValidParentheses(6))
# print(generateValidParentheses(2))

def generateparentheses(n):
    res = set()
    if n == 0:
        return set()
    elif n % 2 != 0:
        return set()
    left, right = 0, 0
    n = n / 2
    generator(left, right, n, "", res)
    return res

def generator(left, right, n, string, res):
    if right == n:
        res.add(string)
        return res
    else:
        print(string)
        if left < n:
            generator(left + 1, right, n, string + "(", res)
        if right < left:
            generator(left, right + 1, n, string + ")", res)

print(generateparentheses(6))
print(generateparentheses(4))
