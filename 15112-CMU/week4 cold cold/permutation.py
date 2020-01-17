# function to generate all the sub lists
def getSubLists(lst):
    # store all the sub lists
    subLists = []
    # first loop
    for i in range(len(lst)):
        # second loop
        for j in range(i + 1, len(lst) + 1):
            # slice the sub array
            sub = lst[i:j]
            print(sub)
            subLists.append(sub)
    # return subLists


print(getSubLists(["a","b","c","d"]))











#
# print(combine(["a","b","c","d"], 3))