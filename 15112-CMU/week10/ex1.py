def isNotTrivialSol(L):
    for c in L:
        if len(c) != 1:
            return True
    return False

def palinidromePartitionHelper(res, s):
    if len(s) == 0 and isNotTrivialSol(res):
        return res
    if len(s) == 0:
        return None
    else:
        for i in range(len(s), 0, -1):
            if s[:i] == s[:i][::-1]:
                res.append(s[:i])
                tmp = palinidromePartitionHelper(res, s[i:])
                if tmp is not None:
                    return tmp
                res.pop()
        return None


def palinidromePartition(s):
    res = []
    return palinidromePartitionHelper(res, s)

print(palinidromePartition("geeks"))
print(palinidromePartition("abc"))
print(palinidromePartition("racecar"))
print(palinidromePartition("abba"))
print(palinidromePartition("abbc"))


def findTriplets(arr):
    result = set()
    n = len(arr)
    for i in range(n-1):
        s = set()
        for j in range(i+1, n):
            x = - (arr[i] + arr[j]) # represent the
            # third num you're looking for
            if x in s: # if x has been "seen" before
                result.add((x, arr[i], arr[j]))
            else:
                s.add(arr[j])
    return result

print(findTriplets([1, 0, -3, 2, -1]))

