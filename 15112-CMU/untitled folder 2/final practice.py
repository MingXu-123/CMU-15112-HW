def isConceitedNum(num):
    res = 0
    lenOfnum = len(str(num))
    for i in range(lenOfnum):
        res += int(str(num)[i])**lenOfnum
    return res == num


def nthConceitedNumber(n):
    count = 0
    num = 0
    while count < n:
        num += 1
        if isConceitedNum(num):
            count += 1
    return num

print(nthConceitedNumber(11))


def outOfBounds(currRow, currCol, L):
    return not (0 <= currRow <= len(L) and (0 <= currCol <= len(L[0])))


# 此题不会
def spiralJoin(L):
    direction = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    directionIndex = 0
    seen = set()
    result = ""
    location = (0, 0)
    while len(seen) != len(L)*len(L[0]):
        currRow, currCol = location
        drow = direction[directionIndex][0]  #0
        dcol = direction[directionIndex][1]  #1
        if location not in seen and not outOfBounds(currRow, currCol, L):
            seen.add(location)
            result += L[currRow][currCol]
            location = (drow + currRow, dcol + currCol)
        else:
            oldRow, oldCol = currRow - drow, currCol - dcol
            directionIndex = (directionIndex + 1) % 4
            drow = direction[directionIndex][0]
            dcol = direction[directionIndex][1]
            location = (oldRow + drow, oldCol + dcol)
        return result

L = [["a", "b", "c", "de"],
         ["fgh", "ijk", "lm", "n"],
         ["q", "rse", "t", "u"]]

def testSpiralJoin():
    print("Testing spiralJoin...")
    L = [["a", "b", "c", "de"],
         ["fgh", "ijk", "lm", "n"],
         ["q", "rse", "t", "u"]]
    L1 =[["18", "3"],
         ["gg", "qq"]]
    L2 = [["eat"]]
    assert(spiralJoin(L) == "abcdenutrseqfghijklm")
    assert(spiralJoin(L1) == "183qqgg")
    assert(spiralJoin(L2) == "eat")
    print("testing passed!")

# testSpiralJoin()
# print(spiralJoin(L))


def numberWooTriple(L):
    result = set()
    s = set(L)  # O(N)
    for i in range(len(L)):
        for j in range(len(L)):
            k = L[i] ** 2 % L[j]
            t = (L[i], L[j], k)
            t = tuple(sorted(t))
            if k in s: # O(1)
                result.add(t)
    return result

print(numberWooTriple([1,3,2]))

def check(L):
    if len(L) == 1:
        if int(L[0]**0.5) != L[0]**0.5:
            return False
    for i in range(len(L)):
        if i != len(L) - 1:
            if int((L[i] + L[i + 1]) ** 0.5) \
                    != (L[i] + L[i + 1]) ** 0.5:
                return False
    return True

def helper(L, result):
    if len(L) == 0 and check(L):
        return result
    if len(L) == 0:
        return None
    for elem in L:
        if check(result + [elem]):
            result.append(elem)
            L.remove(elem)
            tmp = helper(L, result)
            if tmp is not None:
                return tmp
    return None

def getSquarefulArrangement(L):
    return helper(L, [])

print(getSquarefulArrangement([1,17,8]))




