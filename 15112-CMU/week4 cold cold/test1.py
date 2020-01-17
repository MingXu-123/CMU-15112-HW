def destructiveRemoveRepeats(lst):
    for i in range(len(lst) - 1, -1, -1):
        if lst.count(lst[i]) > 1:
            lst.pop(i)

def destructiveRemoveRepeats1(lst):
    lst.reverse()
    index = 0
    while index < len(lst):
        print(len(lst))
        if lst.count(lst[index]) > 1:
            lst.pop(index)
        else:
            index += 1
    lst.reverse()

def destructiveRemoveRepeats2(lst):
    lst.reverse()
    for num in lst:
        if lst.count(num) > 1:
            lst.remove(num)
    lst.reverse()


def testDestructiveRemoveRepeats():
    print("Testing destructiveRemoveRepeats()", end="")
    a = [1,3,5,3,3,2,1,7,5]
    assert(destructiveRemoveRepeats(a) == None)
    assert(a == [1,3,5,2,7])
    b = [1,2,3,-2]
    assert(destructiveRemoveRepeats(b) == None)
    assert(b == [1,2,3,-2])
    print("Passed.")

testDestructiveRemoveRepeats()
# print(destructiveRemoveRepeats([1,3,5,3,3,2,1,7,5]))
# print(destructiveRemoveRepeats([1,2,3,-2]))