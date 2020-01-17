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


def valueOfLetter(letterScores, letter):
    indexOfLetter = ord(letter) - 97
    value = letterScores[indexOfLetter]
    return value


def getScoresOfWords(letterScores, targetWordLst):
    scores = []
    for i in range(len(targetWordLst)):
        score = 0
        for j in range(len(targetWordLst[i])):
            score += valueOfLetter(letterScores, targetWordLst[i][j])
        scores.append(score)
    return scores


def bestScrabbleScore(dictionary, letterScores, hand):
    allPossibleWords = findAllPossibleWordsOfHand(hand)
    targetWordLst = []
    for i in range(len(allPossibleWords)):
        if allPossibleWords[i] in dictionary and\
                allPossibleWords[i] not in targetWordLst:
            targetWordLst.append(allPossibleWords[i])
    if targetWordLst == []:
        return None
    scoreList = getScoresOfWords(letterScores, targetWordLst)
    index = []
    maxScore = max(scoreList)
    i = 0
    while i < len(scoreList):
        if scoreList[i] == maxScore:
            index.append(i)
        i += 1
    resultList = []
    for c in index:
        resultList.append(targetWordLst[c])
    if len(resultList) == 1:
        return(resultList[0], maxScore)
    else:
        return(resultList, maxScore)


def testBestScrabbleScore():
    print("Testing bestScrabbleScore()...", end="")
    def d1(): return ["a", "b", "c"]
    def ls1(): return [1] * 26
    def d2(): return ["xyz", "zxy", "zzy", "yy", "yx", "wow"]
    def ls2(): return [1 + (i % 5) for i in range(26)]
    assert(bestScrabbleScore(d1(), ls1(), ["b"]) == ("b", 1))
    assert(bestScrabbleScore(d1(), ls1(), ["a", "c", "e"]) == (["a", "c"], 1))
    assert(bestScrabbleScore(d1(), ls1(), ["b"]) == ("b", 1))
    assert(bestScrabbleScore(d1(), ls1(), ["z"]) == None)
    # x = 4, y = 5, z = 1
    # ["xyz", "zxy", "zzy", "yy", "yx", "wow"]
    #    10     10     7     10    9      -
    assert(bestScrabbleScore(d2(), ls2(), ["x","y","z"]) == (["xyz","zxy"], 10))
    assert(bestScrabbleScore(d2(), ls2(),
                            ["x", "y", "z", "y"]) == (["xyz", "zxy", "yy"], 10))
    assert(bestScrabbleScore(d2(), ls2(), ["x", "y", "q"]) == ("yx", 9))
    assert(bestScrabbleScore(d2(), ls2(), ["y", "z", "z"]) == ("zzy", 7))
    assert(bestScrabbleScore(d2(), ls2(), ["w", "x", "z"]) == None)
    print("Passed.")

testBestScrabbleScore()

# print(findAllPossibleWordsOfHand(["x","y","z"]))


def d1(): return ["a", "b", "c"]
def ls1(): return [1] * 26
def d2(): return ["xyz", "zxy", "zzy", "yy", "yx", "wow"]
def ls2(): return [1 + (i % 5) for i in range(26)]
# print(bestScrabbleScore(d2(), ls2(), ["x","y","z"]))
# print(bestScrabbleScore(d1(), ls1(), ["b"]))
# print(bestScrabbleScore(d1(), ls1(), ["a", "c", "e"]))
# print(bestScrabbleScore(d1(), ls1(), ["z"]))
# print(bestScrabbleScore(d2(), ls2(),
#                             ["x", "y", "z", "y"]))