def binarySearch1(alist, item):
    first = 0
    last = len(alist) - 1
    found = False
    while first <= last and not found:
        midpoint = (first + last) // 2
        if alist[midpoint] == item:
            found = True
        else:
            if item < alist[midpoint]:
                last = midpoint - 1
            else:
                first = midpoint + 1
    return found
# print(binarySearch1([0, 1, 2, 8, 13, 17, 19, 32, 42,], 3))
# print(binarySearch1([0, 1, 2, 8, 13, 17, 19, 32, 42,], 13))
# print(binarySearch1([1,3,4,5],3))
# print(binarySearch1([1,3,4,5,6],7))


def binarySearchRecur(alist, first, last, item, lstTuple):
    if first > last:
        return lstTuple
    midpoint = (first + last) // 2
    lstTuple.append((midpoint, alist[midpoint]))
    if alist[midpoint] == item:
        return lstTuple
    else:
        if item < alist[midpoint]:
            return binarySearchRecur(alist, first, midpoint - 1, item, lstTuple)
        else:
            return binarySearchRecur(alist, midpoint + 1, last, item, lstTuple)


def binarySearch(lst, item):
    first = 0
    last = len(lst) - 1
    lstTuple = []
    return binarySearchRecur(lst, first, last, item, lstTuple)


testlist = [0, 1, 2, 8, 13, 17, 19, 32, 42,]
testlist2 = ['a', 'c', 'f', 'g', 'm', 'q']
# print(binarySearch(testlist, 3))
# print(binarySearch(testlist, 13))
print(binarySearch(testlist2, "c"))
print("")
print(binarySearch(testlist2, "n"))
print(binarySearch(testlist2, "m"))
print(binarySearch(['a', 'b', 'c', 'd', 'e'], 'a'))