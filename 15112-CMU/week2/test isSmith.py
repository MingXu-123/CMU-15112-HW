def isPrime(n):
    if (n < 2):
        return False
    maxFactor = round(n**0.5)
    for factor in range(2, maxFactor+1):
        if (n % factor == 0):
            return False
    return True


def sum_digits(n):
    sum = 0
    while n:
        sum += n % 10
        n //= 10
    return sum


def isSmithNumber(n):
    if isPrime(n):
        return False
    sumofdigit = sum_digits(n)
    sumOfPrimeFactor = 0
    for factor in range(2, n + 1):
        if isPrime(factor):
            while n % factor == 0:
                sumOfPrimeFactor += sum_digits(factor)
                n = n / factor
    if sumOfPrimeFactor == sumofdigit:
        return True
    else:
        return False


def testIsSmithNumber():
    print("Testing isSmithNumber()...", end="")
    assert(isSmithNumber(22) == True)
    assert(isSmithNumber(21) == False)
    assert(isSmithNumber(4) == True)
    assert(isSmithNumber(378) == True)
    assert(isSmithNumber(1) == False)
    assert(isSmithNumber(27) == True)
    assert(isSmithNumber(9) == False)
    assert(isSmithNumber(7) == False)
    print("Passed.")


testIsSmithNumber()
# print(sum_digits(456))