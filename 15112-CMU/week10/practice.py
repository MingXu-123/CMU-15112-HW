def notTrivialSol(sol):
    for item in sol:
        if len(item) > 1:
            return True
    return False


def palindromeHelper(s, sol):
    if len(s) == 0 and notTrivialSol(sol):
        return sol
    else:
        for i in range(len(s), 0, -1):
            currStr = s[:i]
            if currStr == currStr[::-1]:
                sol += [currStr]
                tmpSol = palindromeHelper(s[i:], sol)
                if tmpSol is not None:
                    return tmpSol
                sol.pop()
        return None


# print("racecar"[7:])


def palindromePartition(s):
    sol = []
    return palindromeHelper(s, sol)

print(palindromePartition("abc"))
print(palindromePartition("racecar"))
print(palindromePartition("geeks"))
print("")

def ct1(L, depth=0):
    print("\t" * depth + str(L))
    if len(L) == 1:
        result = L[0] ** 2
    elif isinstance(L[0], str):
        result = ct1(L[1:], depth + 1) + ct1([L[-1]], depth + 1)
    else:
        result = ct1(L[1:], depth + 1)
    print("\t" * depth + "->" + str(result))
    return result

ct1(["yeet", 112, "yo", 6])


from functools import reduce
L = [1,2,3,2,4,2]
def myCount(L, item):
    return reduce (lambda x,y: x+y, list(map(lambda x: 1 if x == item else 0, L)))

print(myCount(L, 2))


def ct2(d):
   for k in d:
       if k % 2 == 0:
           d[k + 1] = k + 1
   a = set()
   for k1 in d:
       for k2 in d:
           if k1 != k2 and d[k1] == d[k2]:
               a.add((k1,k2))
   return a

d = dict()
for i in range(6):
    d[i] = i + 1

print(ct2(d))


def findTripletsSlow(L):
    result = set()
    for i in range(len(L)):
        for j in range(len(L)):
            for k in range(len(L)):
                if L[j] != L[i]:
                    if L[k] != L[i] and L[k] != L[j]:
                        if L[i] + L[j] + L[k] == 0:
                            result.add((L[i], L[j], L[k]))
    if result != set():
        return result
    else:
        return None



def findTriplets(arr):
    result = set()
    n = len(arr)
    for i in range(n - 1):
        s = set()
        for j in range(i + 1, n):
            x = - (arr[i] + arr[j]) # represent the
            # third num you're looking for
            if x in s: # if x has been "seen" before
                result.add((x, arr[i], arr[j]))
            else:
                s.add(arr[j])
    return result
print(findTripletsSlow([1,0,-3,2,-1]))



def findTriplets2(lst):
    result = set()
    for i in range(len(lst) - 1):
        s = set()
        for j in range(i + 1, len(lst)):
            x = -(lst[i] + lst[j])
            if x in s:
                result.add((x, lst[i], lst[j]))
            else:
                s.add(lst[j])
    return result
print(findTriplets2([1,0,-3,2,-1]))


def findTripletsFast(arr):
    res = set()
    for i in range(len(arr)):
        for j in range(len(arr)):
            x = arr[i]
            if arr[j] != x:
                y = arr[j]
            else:
                continue
            z = - (x + y)
            if z in set(arr):
                res.add((x, y, z))
    return res


print(findTriplets([1,0]))
print(findTriplets([1,0,-3,2,-1]))
# print(findTripletsFast([1,0,-3,2,-1]))


def palindromePartition3(s, sol = []):
    if len(s) == 0 and notTrivialSol(sol):
        return sol
    else:
        for i in range(len(s), 0, -1):
             currStr = s[:i]
             if currStr == currStr[::-1]:
                 sol.append(currStr)
                 tmpSol = palindromeHelper(s[i:], sol)
                 if tmpSol is not None:
                     return tmpSol
                 sol.pop()

print(palindromePartition3("geeks",[]))
print(palindromePartition3("abcde",[]))
print(palindromePartition3("abbc",[]))