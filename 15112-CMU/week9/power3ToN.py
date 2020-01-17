def powerHelper(n, count, lst):
    if n < 1:
        return lst
    else:
        n = n//3
        count += 1
        num = 3
        return powerHelper(n, count, lst + [num**count])


# this is the main function for powersOf3toN(n)
def powersOf3ToN(n):
    if n <= 0:
        return []
    lst = []
    count = -1
    return powerHelper(n, count, lst)

def testPowersOf3ToN():
    print("Testing powersOf3ToN...", end="")
    assert(powersOf3ToN(10.5) == [1, 3, 9])
    assert(powersOf3ToN(9) == [1, 3, 9])
    assert(powersOf3ToN(0) == [])
    assert(powersOf3ToN(0.9876) == [])
    assert(powersOf3ToN(1) == [1])
    assert(powersOf3ToN(-10.5) == [])
    assert(powersOf3ToN(-43) == [])
    assert(powersOf3ToN(2186.5) == [1,3,9,27,81,243,729])
    assert(powersOf3ToN(2187) == [1,3,9,27,81,243,729,2187])
    print("Passed!")

print(powersOf3ToN(10.5))
testPowersOf3ToN()