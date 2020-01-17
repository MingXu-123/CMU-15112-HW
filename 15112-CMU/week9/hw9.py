#################################################################
# Hw9
# Your Name: Ming Xu
# Your Andrew ID:mxu2
# Your Section:2N
#################################################################
# this function return the Collaborator
def alternatingSumCollaborators():
    return "nobody"


# This is the helper function for alternatingSum(lst)
def doTheRecursion(lst, flag):
    if len(lst) == 0:
        return 0
    else:
        if flag:
            # transfer the flag == True to flag == False
            return lst[0] + doTheRecursion(lst[1:], False)
        else:
            # transfer the flag == False to flag == True
            return -lst[0] + doTheRecursion(lst[1:], True)


# This is the alternating sum main function
def alternatingSum(lst):
    flag = True
    return doTheRecursion(lst, flag)


# this function return the Collaborator
def binarySearchValuesCollaborators():
    return "xiaoqint"


# this is the helper function for binary search values
def binarySearchRecur(alist, first, last, item, lstTuple):
    if first > last:
        return lstTuple
    midpoint = (first + last) // 2
    lstTuple += [(midpoint, alist[midpoint])]
    if alist[midpoint] == item:
        return lstTuple
    else:
        if item < alist[midpoint]:
            newLast = midpoint - 1
            return binarySearchRecur(alist, first,
                                     newLast, item, lstTuple)
        else:
            newFirst = midpoint + 1
            return binarySearchRecur(alist, newFirst,
                                     last, item, lstTuple)


# this is the binary search values main function
def binarySearchValues(lst, item):
    first = 0
    last = len(lst) - 1
    lstTuple = []
    return binarySearchRecur(lst, first, last, item, lstTuple)


# this is the helper function for findCategoryPath
def recurFindPathHelper(d, value, lst):
    for key in d:
        if (type(d[key])) != dict:
            if d[key] == value:
                lst.append(key)
                return lst
        else:
            if recurFindPathHelper(d[key],
                                   value, lst + [key]) is None:
                continue
            else:
                return recurFindPathHelper(d[key],
                                           value, lst + [key])


# this is the main function for findCategoryPath
def findCategoryPath(d, value):
    lst = []
    return recurFindPathHelper(d, value, lst)


# this is the helper function for powersOf3ToN
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


# this is function returns all the possible subsets of a.
def powerset(a):
    # Base case: the only possible subset of
    # an empty list is the empty list.
    if (len(a) == 0):
        return [ [] ]
    else:
        # Recursive Case: remove the first element,
        # then find all subsets of the remaining list.
        # Then duplicate each subset into two versions:
        # one without the first element, and one with it.
        partialSubsets = powerset(a[1:])
        allSubsets = [ ]
        for subset in partialSubsets:
            allSubsets.append(subset)
            allSubsets.append([a[0]] + subset)
        return allSubsets


# get another part of the list
def getOtherPart(lst, left):
    import copy
    lfCopy = copy.deepcopy(left)
    res = []
    for c in lst:
        if c not in lfCopy:
            res += [c]
        else:
            lfCopy.remove(c)
    return res


# This function returns all outcomes of two different lists
def divideAlistIntoTwoParts(lst):
    res = []
    allSubsets = powerset(lst)
    for left in allSubsets:
        otherPart = getOtherPart(lst, left)
        res.append((left, otherPart))
    return res


# this is the loadBalance main function
def loadBalance(lst):
    res = None
    miniValue = sum(lst)
    allPossibleOutcomes = divideAlistIntoTwoParts(lst)
    for outcome in allPossibleOutcomes:
        if abs(sum(outcome[0]) - sum(outcome[1])) <= miniValue:
            miniValue = abs(sum(outcome[0]) - sum(outcome[1]))
            res = outcome
    return res


# this is the helper function for generateValidParentheses
def generate(left, right, string, res):
    if left == 0 and right == 0:
        res.add(string)
        return res
    else:
        if left > 0:
            generate(left - 1, right, string + '(', res)
        if right > left:
            generate(left, right - 1, string + ')', res)


# this is the main function for generateValidParentheses
def generateValidParentheses(n):
    res = set()
    if n == 0:
        return set()
    elif n % 2 != 0:
        return set()
    left, right = (n / 2), (n / 2)
    generate(left, right, "", res)
    return res

#################################################
# Hw9 Test Functions
#################################################

def testAlternatingSum():
    print("Testing alternatingSum...", end="")
    assert(alternatingSum([1, 2, 3, 4, 5]) == 3)
    assert(alternatingSum([1, 2, 3, 4]) == - 2)
    assert(alternatingSum([]) == 0)
    assert(alternatingSum([1, 4, 6, 7, 4]) == 0)
    print("Passed!")


def testBinarySearchValues():
    print("Testing binarySearchValues...", end="")
    assert(binarySearchValues(['a', 'c', 'f', 'g', 'm', 'q'], 'c') ==
           [(2, 'f'), (0, 'a'), (1, 'c')])
    assert(binarySearchValues(['a', 'c', 'f', 'g', 'm', 'q'], 'n') ==
           [(2, 'f'), (4, 'm'), (5, 'q')])
    assert(binarySearchValues(['a', 'c', 'f', 'g', 'm', 'q'], 'f') ==
           [(2, 'f')])
    assert(binarySearchValues(['a', 'b', 'c', 'd'], 'e') ==
           [(1, 'b'), (2, 'c'), (3, 'd')])
    assert(binarySearchValues(['a', 'b', 'c', 'd'], 'a') ==
           [(1, 'b'), (0, 'a')])
    assert(binarySearchValues(['a', 'b', 'c', 'd', 'e'], 'a') ==
           [(2, 'c'), (0, 'a')])
    print("Passed!")


def testFindCategoryPath():
    print("Testing findCategoryPath...", end="")
    d = {"Sporting":
             {"Spaniel":
                  {"English Springer": "Betsy"},
              "Weimaraner": "Xeva",
              "Retriever":
                  {"Golden": "Sammo",
                   "Labrador": "Nya"}
              },
         "Working":
             {"Husky": "Stella",
              "Saint Bernard": "Rutherfurd",
              "Boxer": "Paximus"},
         "Herding":
             {"Corgi":
                  {"Welsh":
                       {"Cardigan": "Geb",
                        "Pembroke": "Niinja"}
                   },
              "Sheepdog":
                  {"Bergamasco": "Samur",
                   "Old English": "Duggy",
                   "Shetland": "Walker"}
              },
         "Other": "Kimchee"
         }
    value1 = "Samur"
    value2 = "Weimaraner"
    value3 = "Betsy"
    value4 = "Other"
    value5 = "Paximus"
    assert(findCategoryPath(d, value1) == ["Herding", "Sheepdog",
                                           "Bergamasco"])
    assert(findCategoryPath(d, value2) is None)
    assert(findCategoryPath(d, value3) == ["Sporting", "Spaniel",
                                           "English Springer"])
    assert(findCategoryPath(d, value4) is None)
    assert(findCategoryPath(d, value5) == ["Working", "Boxer"])
    print("Passed!")


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


def testLoadBalance():
    print("Testing loadBalance...", end="")
    assert(loadBalance([3, 6, 1, 7, 9, 8, 22, 3]) == ([3, 6, 1, 7, 9, 3], [8, 22]) or
           loadBalance([3, 6, 1, 7, 9, 8, 22, 3]) == ([3, 6, 9, 8, 3], [1, 7, 22]) or
           loadBalance([3, 6, 1, 7, 9, 8, 22, 3]) == ([9, 8, 7, 3, 3], [22, 6, 1]) or
           loadBalance([3, 6, 1, 7, 9, 8, 22, 3]) == ([3, 1, 22, 3], [6, 7, 9, 8])
           )
    assert(loadBalance([0, 1, 2]) == ([0, 2], [1]))
    print("Passed!")


def testGenerateValidParentheses():
    print("Testing generateValidParentheses...", end="")
    assert(generateValidParentheses(4) == { "(())", "()()" })
    assert(generateValidParentheses(6) == { "((()))", "()(())",
                                            "(())()", "(()())", "()()()" })
    assert(generateValidParentheses(5) == set())
    assert(generateValidParentheses(0) == set())
    print("Passed!")


def testAll():
    testAlternatingSum()
    testBinarySearchValues()
    testLoadBalance()
    testFindCategoryPath()
    testGenerateValidParentheses()
    testPowersOf3ToN()


def main():
    testAll()

if __name__ == '__main__':
    main()

