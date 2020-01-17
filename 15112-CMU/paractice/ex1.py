def substrCount(n, s):
    counter = 0
    # following code count palindrome len of Palindrome str longer than 2
    for i in range(n):
        offset = 1
        while i - offset >= 0 and i + offset < n:
            if s[i - offset] == s[i + offset]:
                counter += 1
                offset += 1
                continue
            else:
                break
    # following code counter repeats like "aa"
    repeats = 0
    for i in range(n - 1):
        if s[i] == s[i + 1]:
            repeats += 1
    res = counter + repeats + n # n is the palindrome with len 1
    return res


# print(substrCount(3, "aba"))
# print(substrCount(5, 'asasd'))
# print(substrCount(7, "abcbaba"))
# print(substrCount(8, "mnonopoo"))
# print(substrCount(7, 'abcbaba'))
# print(substrCount(5, "nnnnn"))
# print(substrCount(4, "nnnn"))

def function1():
    try:
        1/0
        print("Yeah!")
    except:
        print("This function has run time error")

# function1()



def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = [arr[0]]
    left = quicksort([arr[i] for i in range(len(arr)) if arr[i] < pivot[0]])
    right = quicksort([arr[i] for i in range(len(arr)) if arr[i] > pivot[0]])
    return left + pivot + right

print(quicksort([3, 5, 2, 1]))
print(quicksort([13, 3434, 35, 4345]))
print(quicksort([0]))
print(quicksort([1, 2, 3, 4, 5]))



print(" ")
print("haha merge sort !")

def merge(arr, lo, mid, hi):
    B = [0] * (hi - lo)
    i = lo
    j = mid
    k = 0
    while (i < mid) and (j < hi):
        if arr[i] <= arr[j]:
            B[k] = arr[i]
            i += 1
        else:
            B[k] = arr[j]
            j += 1
        k += 1
    while i < mid:
        B[k] = arr[i]
        i += 1
        k += 1
    while j < hi:
        B[k] = arr[j]
        j += 1
        k += 1
    for k in range(0, hi - lo):
        arr[lo + k] = B[k]


def mergesort(arr, lo, hi):
    if (hi - lo) <= 1:
        return
    mid = lo + (hi - lo) // 2
    mergesort(arr, lo, mid)
    mergesort(arr, mid, hi)
    merge(arr, lo, mid, hi)


arr = [3, 2, 1]
(mergesort(arr, 0, 3))
print(arr)
