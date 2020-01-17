def perm(lst):
    if len(lst) == 0:
        return []
    elif len(lst) == 1:
        return [lst]
    else:
        result = []
        for i in range(len(lst)):
            x = lst[i]
            xs = lst[:i] + lst[i + 1:]
            for p in perm(xs):
                result.append([x] + p)
        return result


def getSubLists(lst):
    outPut = [[]]
    for i in range(len(lst)):
        for j in range(len(outPut)):
            outPut.append(outPut[j] + [lst[i]])
    outPut.remove([])
    return outPut


def findAllPossibleWordsOfHand(hand):
    if len(hand) == 1:
        return hand
    result = []
    subLists = getSubLists(hand)
    for i in range(len(subLists)):
        result += perm(subLists[i])
    answer = []
    for j in range(len(result)):
        char = "".join(result[j])
        answer += [char]
    return answer


def bestScrabbleScore(dictionary, hand):
    allPossibleWords = findAllPossibleWordsOfHand(hand)
    # valueOfWords = []
    # valueOfWord = 0
    wordLst = []
    for i in range(len(allPossibleWords)):
        if allPossibleWords[i] in dictionary:
            wordLst.append(allPossibleWords[i])
    print(wordLst)




def d1(): return ["a", "b", "c"]
def ls1(): return [1] * 26
def d2(): return ["xyz", "zxy", "zzy", "yy", "yx", "wow"]
def ls2(): return [1 + (i % 5) for i in range(26)]
print(bestScrabbleScore(d2(),["x","y","z"]))