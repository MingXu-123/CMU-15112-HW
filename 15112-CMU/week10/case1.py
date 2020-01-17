def helper(n, lst):
    if 0 not in lst:
        return lst
    for i in range(len(lst)):
        if i + n + 1 <= len(lst):
            if lst[i] == 0 and lst[i + n + 1] == 0:
                lst[i] = n
                lst[i + n + 1] = n
                tmp = helper(n - 1, lst)
                if tmp is not None:
                    return tmp
                lst[i] = 0
                lst[i + n + 1] = 0
    return None


def distList(n):
    lenOflst = 2*n
    lst = [0]*lenOflst
    return helper(n, lst)

print(distList(4))



def HelperCount(lst, d):
    if len(lst) == 0:
        return d
    else:
        if lst[0] not in d:
            d[lst[0]] = 1
            return HelperCount(lst[1:], d)
        else:
            d[lst[0]] += 1
            return HelperCount(lst[1:], d)


def getItemCounts(lst):
    d = dict()
    return HelperCount(lst, d)
print(getItemCounts(["a", "b", "c", "a", "a", "c"]))


def packHelper(items, bagSizes, res):
    if len(items) == 0:
        return res

def packItem(items, bagSizes):
    res = []
    return packHelper(items, bagSizes, res)

print(packItem([4,8,1,4,3], [12,9]))
print(packItem([4,8,1,4,3], [10,10]))

def loadBalance(a, b, L):
    if len(L) == 0:
        return a, b
    item = L.pop(0)
    try1Box1, try1Box2 = loadBalance(a + [item], b, L)
    try2Box1, try2Box2 = loadBalance(a, b + [item], L)
    diff1 = abs(sum(try1Box1) - sum(try1Box2))
    diff2 = abs(sum(try2Box1) - sum(try2Box2))
    if diff1 > diff2:
        return try1Box1, try1Box2
    else:
        return try2Box1, try2Box2



def visualizeRecursion(f):
    depth = 0
    def g(*args, **kwargs):
        nonlocal depth
        depth += 1
        res = f(*args, **kwargs)
        depth -= 1
        s = "\t" * depth + "recursion depth: " \
            + str(depth) + ', result: ' + str(res)
        print(s)
        return res
    return g


@visualizeRecursion
def fact(n):
    if n == 0: return 1
    return n * fact(n-1)
fact(4)

