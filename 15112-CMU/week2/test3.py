
def isKaprekarNumber(n):
    if n < 1:
        return False
    lenOfNum = len(str(n))
    A = n**2 // 10**lenOfNum
    B = n**2 % 10**lenOfNum
    if A + B == n:
        return True
    else:
        return False


def nthKaprekarNumber(n):
    found = -1  # !!!!!
    guess = 0
    while (found < n):
        guess += 1
        if (isKaprekarNumber(guess)):
            found += 1
    return guess


def nearestKaprekarNumber(n):
    if n <= 1:
        return 1
    count = 1
    if type(n) == int:
        if isKaprekarNumber(n):
            return n
        while not isKaprekarNumber(n):
            a = n - count
            if isKaprekarNumber(a):
                return a
            b = n + count
            if isKaprekarNumber(b):
                return b
            count += 1

    if type(n) == float:
        import math
        rawnum = n
        count = 1
        if (n - int(n)) <= 0.5:
            if isKaprekarNumber(int(n)):
                return int(n)
            while not isKaprekarNumber(int(n)):
                a = int(n) - count
                if isKaprekarNumber(a):
                    targeta = a
                    break
                count += 1
            count = 1
            while not isKaprekarNumber(int(n)):
                b = int(n) + count
                if isKaprekarNumber(b):
                    targetb = b
                    break
                count += 1
            if abs(rawnum - targeta) <= abs(targetb - rawnum):
                return targeta
            if abs(rawnum - targeta) > abs(targetb - rawnum):
                return targetb

        if (n - int(n)) > 0.5:
            if isKaprekarNumber(math.ceil(n)):
                return math.ceil(n)
            while not isKaprekarNumber(math.ceil(n)):
                a = math.ceil(n) - count
                if isKaprekarNumber(a):
                    targeta = a
                    # print(targeta)
                    break
                count += 1
            count = 1
            while not isKaprekarNumber(math.ceil(n)):
                b = math.ceil(n) + count
                if isKaprekarNumber(b):
                    targetb = b
                    # print(targetb)
                    break
                count += 1
            if abs(rawnum - targeta) <= abs(targetb - rawnum):
                return targeta
            if abs(rawnum - targeta) > abs(targetb - rawnum):
                return targetb










print(nearestKaprekarNumber(9376543))
# print(nearestKaprekarNumber(2475.51))
# print(nearestKaprekarNumber(4.99999999))
print("")
print(nearestKaprekarNumber(5.51))


def testNearestKaprekarNumber():
    print("Testing nearestKaprekarNumber()...", end="")
    print("Testing nearestKaprekarNumber()...", end="")
    assert(nearestKaprekarNumber(1) == 1)
    assert(nearestKaprekarNumber(0) == 1)
    assert(nearestKaprekarNumber(-1) == 1)
    assert(nearestKaprekarNumber(-2) == 1)
    assert(nearestKaprekarNumber(-12345) == 1)
    assert(nearestKaprekarNumber(1.234) == 1)
    assert(nearestKaprekarNumber(4.99999999) == 1)
    assert(nearestKaprekarNumber(100.99999999) == 99)
    assert(nearestKaprekarNumber(5) == 1)
    assert(nearestKaprekarNumber(5.00000001) == 9)
    assert(nearestKaprekarNumber(27) == 9)
    assert(nearestKaprekarNumber(28) == 45)
    assert(nearestKaprekarNumber(45) == 45)
    assert(nearestKaprekarNumber(50) == 45)
    assert(nearestKaprekarNumber(51) == 55)
    assert(nearestKaprekarNumber(1611) == 999)
    assert(nearestKaprekarNumber(1612) == 2223)
    assert(nearestKaprekarNumber(2475.4) == 2223)
    assert(nearestKaprekarNumber(2475.5) == 2223)
    assert(nearestKaprekarNumber(2475.51) == 2728)
    assert(nearestKaprekarNumber(2475.6) == 2728)
    assert(nearestKaprekarNumber(995123) == 994708)
    assert(nearestKaprekarNumber(9376543) == 9372385)
    assert(nearestKaprekarNumber(13641234) == 13641364)
    print("Passed.")


testNearestKaprekarNumber()