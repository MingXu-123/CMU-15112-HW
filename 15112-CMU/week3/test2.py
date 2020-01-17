def getAllSubstrings(s):
    substrings = ""
    lenOfS = len(s)
    for i in range(0, lenOfS):
        for j in range(i, lenOfS):
            string = s[i:j+1]
            substrings += string + ","
    return substrings


def findCommonSubstring(s1, s2):
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
        pass




def testLongestCommonSubstring():
    print("Testing longestCommonSubstring()...", end="")
    assert(longestCommonSubstring("abcdef", "abqrcdest") == "cde")
    assert(longestCommonSubstring("abcdef", "ghi") == "")
    assert(longestCommonSubstring("", "abqrcdest") == "")
    assert(longestCommonSubstring("abcdef", "") == "")
    assert(longestCommonSubstring("abcABC", "zzabZZAB") == "AB")
    print("Passed.")


testLongestCommonSubstring()