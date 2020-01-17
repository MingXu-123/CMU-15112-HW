def numberWooTriple(L):
    s = set(L)
    res = set()
    for i in range(len(L)):
        for j in range(len(L)):
            c = L[i]**2 % L[j]
            t = (L[i], L[j], c)
            t = tuple(sorted(t))
            if c in s:
                res.add(t)
    return res

print(numberWooTriple([1,3,2]))


def check(L):
    if len(L) == 1:
        if int(L[0]**0.5) == L[0]**0.5:
            return True
        else:
            return False
    for i in range(len(L) - 1):
        if int((L[i] + L[i + 1])**0.5) != (L[i] + L[i + 1])**0.5:
            return False
    return True


def getSquarefulArrangeHelper(res, L):
    if len(L) == 0 and check(res):
        return res
    if len(L) == 0:
        return
    for elem in L:
        if check(res + [elem]):
            res.append(elem)
            L.remove(elem)
            tmp = getSquarefulArrangeHelper(res, L)
            if tmp is not None:
                return tmp
    return None


def getSquarefulArrange(L):
    return getSquarefulArrangeHelper([], L)


print(getSquarefulArrange([1,17,8]))
print(getSquarefulArrange([1,2,3]))


def readFile(path):
    with open(path, "rt") as f:
        return f.read()

def writeFile(path, contents):
    with open(path, "wt") as f:
        f.write(contents)

import os



def bestNameFile(path, name):
    if os.path.isfile(path):
        return path
    else:
        numOfOcurrance = 0
        res = ""
        for filename in os.listdir(path):
            if filename == '.DS_Store':
                continue
            tmpPath = bestNameFile(path + "/" + filename, name)
            contents = readFile(tmpPath)
            if contents.count(name) >= numOfOcurrance:
                numOfOcurrance = contents.count(name)
                res = tmpPath
        return res



def bestNameFileHelper(path, name):
    if os.path.isfile(path):
        contents = readFile(path).lower()
        occurance = contents.count(name)
        return path, occurance
    else:
        current = (path, 0)
        for filename in os.listdir(path):
            newPath = path + os.sep + filename
            temp = bestNameFileHelper(newPath, name)
            if current[1] <= temp[1]:
                current = temp
        return current


def bestNameFile2(path, name):
    name = name.lower()
    return bestNameFileHelper(path, name)[0]