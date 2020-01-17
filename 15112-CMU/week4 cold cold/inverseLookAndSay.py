import copy

def inverseLookAndSay(lst):
    result = []
    for element in lst:
        n = element[0]
        num = element[1]
        while n > 0:
            result.append(num)
            n -= 1
    return result


def _verifyInverseLookAndSayIsNondestructive():
    a = [(1,2), (2,3)]
    b = copy.copy(a)
    inverseLookAndSay(a) # ignore result, just checking for destructiveness here
    return (a == b)

def testInverseLookAndSay():
    print("Testing inverseLookAndSay()...", end="")
    assert(_verifyInverseLookAndSayIsNondestructive() == True)
    assert(inverseLookAndSay([]) == [])
    assert(inverseLookAndSay([(3,1)]) == [1,1,1])
    assert(inverseLookAndSay([(1,-1),(1,2),(1,7)]) == [-1,2,7])
    assert(inverseLookAndSay([(2,3),(1,8),(3,-10)]) == [3,3,8,-10,-10,-10])
    print("Passed.")

testInverseLookAndSay()
# print(inverseLookAndSay([(2,3),(1,8),(3,-10)]))