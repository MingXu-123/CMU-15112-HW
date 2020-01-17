import copy

def lookAndSay(lst):
    list_num = list(lst)
    result = []
    count = 1
    if list_num == []:
        return []
    elif list_num != []:
        for i in range(len(list_num)):
            if (i + 1) < len(list_num) and list_num[i + 1] == list_num[i]:
                count += 1
            else:
                if i == 0 and list_num[i + 1] != list_num[i]:
                    result.append((1, list_num[0]))
                elif i == 0 and list_num[i + 1] == list_num[i]:
                    continue
                elif i == len(list_num) - 1:
                    if list_num[i] == list_num[i - 1]:
                        result.append((count, list_num[i - 1]))
                    else:
                        result.append((1, list_num[i]))
                else:
                    if list_num[i] == list_num[i - 1]:
                        result.append((count, list_num[i - 1]))
                    elif list_num[i] != list_num[i - 1]:
                        result.append((1, list_num[i]))
                count = 1
    return result

# def lookAndSay(lst):
#     list_num = list(lst)
#     result = []
#     count = 1
#     if list_num == []:
#         return []
#     elif list_num != []:
#         for i in range(len(list_num)):
#             if list_num[i] == list_num[i - 1]:
#                 count += 1
#             else:
#                 count += 1
#                 result.append((count - len(list_num[:i]), list_num[i]))
#
#     return result




def _verifyLookAndSayIsNondestructive():
    a = [1,2,3]
    b = copy.copy(a)
    lookAndSay(a) # ignore result, just checking for destructiveness here
    return (a == b)


def testLookAndSay():
    print("Testing lookAndSay()...", end="")
    assert(_verifyLookAndSayIsNondestructive() == True)
    assert(lookAndSay([]) == [])
    assert(lookAndSay([1,1,1]) == [(3,1)])
    assert(lookAndSay([-1,2,7]) == [(1,-1),(1,2),(1,7)])
    assert(lookAndSay([3,3,8,-10,-10,-10]) == [(2,3),(1,8),(3,-10)])
    assert(lookAndSay([1, 1, 2, 2, 3, 7]) == [(2, 1), (2, 2), (1, 3), (1, 7)])
    assert(lookAndSay([-1, 2, 2, 2, 2, 3, -10, 7, 7]) == [(1, -1),(4, 2),(1, 3),(1,-10),(2, 7)])
    assert(lookAndSay([0,0,0])==[(3,0)])
    print("Passed.")

testLookAndSay()
# print(lookAndSay([1,1,,11]))
print(lookAndSay([-1,2,7,6,8,2]))
# print(lookAndSay([3,3,8,-10,-10,-10]))
# # print(lookAndSay([3,3,8,-10,-10,-10]))
# print(lookAndSay([1, 1, 2, 2, 3, 7]))
# print(lookAndSay([-1, 2, 2, 2, 2, 3, -10, 7, 7]))
