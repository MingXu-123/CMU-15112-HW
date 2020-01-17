def subsets(lst):
    output = [[]]
    for i in range(len(lst)):
        for j in range(len(output)):
            output.append(output[j] + [lst[i]])
    output.remove([])
    return output
print(subsets(["a","b","c","d"]))