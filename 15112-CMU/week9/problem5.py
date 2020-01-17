def loadBalance(lst):
    lstA = []
    lstB = []
    items = sorted(lst)
    for item in reversed(items):
        if sum(lstA) < sum(lstB):
            lstA += [item]
        else:
            lstB += [item]
    return (lstA, lstB)

print(loadBalance([3, 6, 1, 7, 9, 8, 22, 3]))


# subsets
def powerset(a):
    if len(a) == 0:
        return [[]]
    else:
        partial = powerset(a[1:])
        allSubsets = []
        for subset in partial:
            allSubsets.append(subset)
            allSubsets.append([a[0]] + subset)
            # print(allSubsets)
        return allSubsets
print(powerset([1,2,3]))


def permutations(a):
    if len(a) == 1:
        return [a]
    else:
        partial = permutations(a[1:])
        allPerms = []
        for subPerm in partial:
            for i in range(len(subPerm) + 1):
                allPerms.append(subPerm[:i]+[a[0]]+subPerm[i:])
        return allPerms
print(permutations([1,2,3]))