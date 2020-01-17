def ct1(x, d, *args):
    print(" " * d + str(args) + " " + str(x))
    if len(args) <= 2:
        result = x
    else:
        mid = len(args) // 2
        res1 = ct1(x + len(args), d + 1, *args[:mid])
        res2 = ct1(x + sum(args), d + 1, *args[mid:])
        result = res1 + res2
        print(" " * d + "--> " + str(result))
    return result
print(ct1(0, 0, 7, 3, 5, 1, 2))

