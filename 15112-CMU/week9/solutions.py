def loadBalance(lst):
    pass

import os
def printFiles(path):
    # Base Case: a file. Print the path name directly.
    if os.path.isfile(path):
        print(path)
    else:
        # Recursive Case: a directory. Iterate through its files and directories.
        # Note that we have to update the path name to access the inner files!
        for filename in os.listdir(path):
            printFiles(path + "/" + filename)



def generateValidParentheses(n):
    if n == 0 or n % 2 != 0:
        return set()
    return gvpr(n, set())

def gvpr(n, parens):
    if n == 0:
        return parens
    if parens == set():
        return gvpr(n - 1, {"("})
    else:
        newParens = set()
        for s in parens:
            openP = s.count("(")
            closedP = s.count(")")
            if openP > closedP:
                newParens.add(s + ")")
            if openP - closedP < n:
                newParens.add(s + "(")
    return gvpr(n - 1, newParens)

print(generateValidParentheses(4))



a = ["wow", [ [ ] ], [True, 'gosh']]
b = ['a', ['b'], ['c',['d','e'],'f']]
def flattenString(lst):
    res = []
    for item in lst:
        if not (isinstance(item, str) or isinstance(item, list)):
            continue
        elif isinstance(item, str):
            res += [item]
        elif isinstance(item, list):
            res += (flattenString(item))
    return res


# return flatten integers
def flatten(lst):
    res = []
    for i in lst:
        if not lst:
            return []
        if not (isinstance(i, int) or isinstance(i, list)):
            continue
        if type(i) == int:
            res += [i]
        elif isinstance(i, list):
            res += flatten(i)
    return res


print(flatten([[[[]]],[["1"]],"1",[[True]],2,[[2],[3]]]))
print(flatten([True]))
print(flattenString(a))
print(flattenString(b))
print(flattenString(([[[[]]],[["1"]],"1",[[True]],2,[[2],[3]]])))
print(type(True))
print(isinstance(True, int))
print(hash(True))
print(hash(112))
