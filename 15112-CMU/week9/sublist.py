def perm(lst):
    if len(lst) == 0:
        return []
    elif len(lst) == 1:
        return [lst]
    else:
        result = []
        for i in range(len(lst)):
            x = lst[i]
            xs = lst[:i] + lst[i + 1:]
            for p in perm(xs):
                result.append([x] + p)
        return result


# def getSubLists(lst):
#     outPut = [[]]
#     for i in range(len(lst)):
#         for j in range(len(outPut)):
#             outPut.append(outPut[j] + [lst[i]])
#     outPut.remove([])
#     return outPut

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
    print(allSubsets)
    for left in allSubsets:
        otherPart = getOtherPart(lst, left)
        res.append((left, otherPart))
    return res


print(divideAlistIntoTwoParts([0,1,2]))


