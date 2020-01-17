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


def getIndexOfTarget(idx, scoreList, maxScore):
    i = 0
    while i < len(scoreList):
        if scoreList[i] == maxScore:
            idx.append(i)
        i += 1
    return idx

def finalTarget(lst, hand):
    handStr = ""
    for s in hand:
        handStr += s
    newList = []
    for c in lst:
        for char in c:
            if c.count(char) == handStr.count(char):
                if c not in newList:
                    newList.append(c)
    return newList


def bestScrabbleScore(dictionary, letterScores, hand):
    targetWordLst = []
    for word in dictionary:
        CharInHand = True
        for char in word:
            if char in hand:
                CharInHand = True
            else:
                CharInHand = False
                break
        if CharInHand == True:
            targetWordLst.append(word)
    targetWordLst = finalTarget(targetWordLst, hand)
    scoreList = getScoresOfWords(letterScores, targetWordLst)
    if scoreList == []:
        return None
    maxScore = max(scoreList)
    idx = []
    idx = getIndexOfTarget(idx, scoreList, maxScore)
    resultList = []
    for c in idx:
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
#print(bestScrabbleScore(d1(), ls1(), ["b"]))
# print(bestScrabbleScore(d1(), ls1(), ["a", "c", "e"]))
# print(bestScrabbleScore(d1(), ls1(), ["z"]))
# print(bestScrabbleScore(d2(), ls2(),
#                             ["x", "y", "z", "y"]))