def valueOfLetter(letterScores, letter):
    indexOfLetter = ord(letter) - 97
    value = letterScores[indexOfLetter]
    return value

letterScores = [1] * 26
print(valueOfLetter(letterScores,"z"))