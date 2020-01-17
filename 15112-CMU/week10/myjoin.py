from functools import reduce
# this is the lambda function for myJoin
myJoin = lambda L, sep: str(L[0])\
    if len(L) == 1 else reduce(lambda x, y: (x + y),
                               list(map(lambda x: str(x) + sep,
                                        L[:-1]))) + str(L[-1])

print(myJoin([1, 2, 'c', 'd'], ''))
print(myJoin(['a','b','c'], '-'))
print(type(myJoin([1, 2, 'c', 'd'],"")))
print(myJoin([42], ''))
# l = [42]
# a = list(map(lambda x: str(x) + "", l[:-1]))
# print(a)
