# def isKaprekarNumber(n):
#     if n < 1:
#         return False
#     if n == 1:
#         return True
#     lenOfNumsquare = len(str(n**2))
#     for i in range(1, lenOfNumsquare):
#         A = n**2 // 10 ** i
#         B = n**2 % 10 ** i
#         if B != 0 and A + B == n:
#             return True
#     return False

def isKaprekarNumber(n):
    originalnum = n
    if n <= 0:
        return False
    elif n == 1:
        return True
    for i in range(1, len(str(originalnum**2))):
        A = originalnum ** 2 // 10 ** i
        B = originalnum ** 2 % 10 ** i
        if A + B == originalnum:
            if B != 0:
                return True
    return False


def nthKaprekarNumber(n):
    found = 0
    guess = 0
    while (found <= n):
        guess += 1
        if (isKaprekarNumber(guess)):
            found += 1
    return guess

def testIsKaprekarNumber():
    print("Testing isKaprekarNumber()...", end="")
    assert(isKaprekarNumber(0) == False)
    assert(isKaprekarNumber(1) == True)
    assert(isKaprekarNumber(4) == False)
    assert(isKaprekarNumber(9) == True)
    assert(isKaprekarNumber(36) == False)
    assert(isKaprekarNumber(45) == True)
    assert(isKaprekarNumber(450) == False)
    assert(isKaprekarNumber(10) == False)
    assert (isKaprekarNumber(2223) == True)
    assert (isKaprekarNumber(22222) == True)
    assert (isKaprekarNumber(77778) == True)
    assert (isKaprekarNumber(82656) == True)
    assert (isKaprekarNumber(38962) == True)
    print("Passed.")

def testNthKaprekarNumber():
    print("Testing nthKaprekarNumber()...", end="")
    assert(nthKaprekarNumber(0) == 1)
    assert(nthKaprekarNumber(1) == 9)
    assert(nthKaprekarNumber(2) == 45)
    assert(nthKaprekarNumber(3) == 55)
    assert(nthKaprekarNumber(4) == 99)
    assert(nthKaprekarNumber(5) == 297)
    assert(nthKaprekarNumber(6) == 703)
    assert(nthKaprekarNumber(7) == 999)
    print('Passed.')


testNthKaprekarNumber()
testIsKaprekarNumber()