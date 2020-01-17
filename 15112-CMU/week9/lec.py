def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)

print(factorial(5))

print("aaabbcaad")
print("abcad")

# recursive calls
def shortenStrings(s):
    if len(s) == 1:
        return s
    else:
        if s[1] == s[0]:
            return shortenStrings(s[1:])
        else:
            return s[0] + shortenStrings(s[1:])

print(shortenStrings("aaabbcaad"))

# The fibonacci sequence is a mathematical sequence where each element is equal to
# the sum of the two elements that came before it. This translates nicely into recursive code!
def fib(n, depth = 0):
    # print("my n is", n)
    # print("fib(",n,") at depth",depth)
    print(depth*"   |", "fib(", n, ")")
    if (n < 2):
        # Base case:  fib(0) and fib(1) are both 1
        return 1
    else:
        # Recursive case: fib(n) = fib(n-1) + fib(n-2)
        return fib(n-1, depth + 1) + fib(n-2, depth + 1)

print([fib(n) for n in range(15)])
# print(fib(5))

def merge(a, b):
    if len(a) == 0 or len(b) == 0:
        return a + b
    else:
        if a[0] < b[0]:
            return [a[0]] + merge(a[1:], b)
        else:
            return [b[0]] + merge(a, b[1:])

def mergeSort(lst):
    if len(lst) < 2:
        return lst
    else:
        mid = len(lst)//2
        left = lst[:mid]
        right = lst[mid:]
        left = mergeSort(left)
        right = mergeSort(right)
        return merge(left, right)

print(merge([1,2,4,7,9],[0,1,4,6,9]))
print(mergeSort([83,45,21,23,5]))