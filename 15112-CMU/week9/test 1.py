d = {1:[], 2:{}, "Retriever":
                  {"Golden": "Sammo",
                   "Labrador": "Nya"}}
print(type(d[1]))
print(type(d[2]) == dict)
print(type(d["Retriever"]))
a = []
print(a + [1])

# this is the load balance function
def loadBalance(lst):
    lstA = []
    lstB = []
    lst.sort()
    for item in reversed(lst):
        if sum(lstA) < sum(lstB):
            lstA += [item]
        else:
            lstB += [item]
    return (lstA, lstB)