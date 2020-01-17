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


