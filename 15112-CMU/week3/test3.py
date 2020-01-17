def getAllSubstrings(s):
    substrings = ""
    lenOfS = len(s)
    for i in range(0, lenOfS):
        for j in range(i, lenOfS):
            string = s[i: j+1]
            substrings += string + ","
    substrings = substrings[:-1]
    return substrings


def findCommonSubstrings(s1, s2):
    commonStrings = ""
    substringOfS1 = getAllSubstrings(s1)
    substringOfS2 = getAllSubstrings(s2)
    strings1 = substringOfS1.split(",")
    strings2 = substringOfS2.split(",")
    for string_1 in strings1:
        for string_2 in strings2:
            if string_1 == string_2:
                commonStrings += string_1 + ","
    commonStrings = commonStrings[:-1]
    return commonStrings


def longestCommonSubstring(s1, s2):
    if s1 == "" or s2 == "":
        return ""
    elif s1 == s2:
        return s1
    else:
        commonStrings = findCommonSubstrings(s1, s2)
        lenofmax = 0
        for commonstring in commonStrings.split(","):
            if len(commonstring) > lenofmax:
                lenofmax = len(commonstring)
        result = ""
        for commonstring in commonStrings.split(","):
            if len(commonstring) == lenofmax:
                result += commonstring + ","
        result = result[:-1]
        resultList = result.split(",")
        return min(resultList)



print(longestCommonSubstring("abcdef", "abqrcdest"))
print(longestCommonSubstring("abcABC", "zzabZZAB"))
