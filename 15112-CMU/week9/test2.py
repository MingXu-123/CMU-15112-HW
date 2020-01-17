# Problem: given a list, a, produce a list containing all the possible subsets of a.
def powerset(a):
    # Base case: the only possible subset of an empty list is the empty list.
    if (len(a) == 0):
        return [ [] ]
    else:
        # Recursive Case: remove the first element, then find all subsets of the remaining list.
        # Then duplicate each subset into two versions: one without the first element, and one with it.
        partialSubsets = powerset(a[1:])
        allSubsets = [ ]
        for subset in partialSubsets:
            allSubsets.append(subset)
            allSubsets.append([a[0]] + subset)
        return allSubsets


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


def divideAlistIntoTwoParts(lst):
    res = []
    allSubsets = powerset(lst)
    # print(allSubsets)
    for left in allSubsets:
        otherPart = getOtherPart(lst, left)
        res.append((left, otherPart))
    return res

def loadBalance(lst):
    res = None
    minivalue = sum(lst)
    allPossibleOutcomes = divideAlistIntoTwoParts(lst)
    for outcome in allPossibleOutcomes:
        if abs(sum(outcome[0]) - sum(outcome[1])) <= minivalue:
            minivalue = abs(sum(outcome[0]) - sum(outcome[1]))
            res = outcome
    return res

print(loadBalance([0, 1, 2]))
print(loadBalance([3, 6, 1, 7, 9, 8, 22, 3]))
print(loadBalance([]))
