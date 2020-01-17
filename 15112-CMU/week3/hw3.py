#################################################
# Hw3
# Your andrewID:mxu2
# Your section: 2N
#################################################

import cs112_s19_week3_linter


#################################################
# Lab3 COLLABORATIVE LAB problem
# (The problem description will be released Friday, Feb 1)
#################################################
# The problems in this section are LAB PROBLEMS, which means you MUST
#     work on them with at least one collaborator.  See the collaboration
#     policy in the syllabus for more details.  Always list your collaborators!
#     For lab problems, YOU MUST LIST AT LEAST ONE COLLABORATOR

# Note: You will need extra files for gradebookSummary.  These will be
#     released FRIDAY during lab! Comment out the tests for now!
def gradebookSummaryCollaborators():
    return "nobody"

# Return content in files
def readFile(path):
    with open(path, "rt") as f:
        return f.read()

# Return the summary of students grades in files
def gradebookSummary(gradebookFilename):
    script = readFile(gradebookFilename)
    script = script.split("\n")
    result = ""
    for line in script:
        if line != '':
            if not line.startswith("#"):
                name = ""
                score = 0
                characters = line.split(",")
                for i in range(len(characters)):
                    if i == 0:
                        name += characters[i]
                    else:
                        score += int(characters[i])
                score = score/(len(characters) - 1)
                score = "%0.2f" % score
                result += name + "\t" + score + "\n"
    result = result[:-1]
    return result

def applyCaesarCipherCollaborators():
    return "nobody"

def getFinalLetter(ch, shiftNum):
    stayInAlphabet = ord(ch) + shiftNum
    if ch.isalpha() and ch.islower() and shiftNum > 0:
        if stayInAlphabet > ord('z'):
            stayInAlphabet -= 26
    elif ch.isalpha() and ch.islower() and shiftNum < 0:
        if stayInAlphabet < ord('a'):
            stayInAlphabet += 26
    elif ch.isalpha() and ch.isupper() and shiftNum > 0:
        if stayInAlphabet > ord('Z'):
            stayInAlphabet -= 26
    elif ch.isalpha() and ch.isupper() and shiftNum < 0:
        if stayInAlphabet < ord('A'):
            stayInAlphabet += 26
    finalLetter = chr(stayInAlphabet)
    return finalLetter

# Return a cipher text follow by Caesar's law
def applyCaesarCipher(message, shiftNum):
    cipherText = ""
    for ch in message:
        if ch.isspace():
            finalLetter = ch
            cipherText += finalLetter
        elif ch.isalpha():
            finalLetter = getFinalLetter(ch, shiftNum)
            cipherText += finalLetter
        else:
            cipherText += ch
    return cipherText

#################################################
# Hw2 COLLABORATIVE problem
#################################################
# The problem in this section is COLLABORATIVE, which means you may
#     work on it with your classmates if you wish.  See the collaboration
#     policy in the syllabus for more details.  Always list your collaborators!

def rightJustifyTextCollaborators():
    return "xiaoqint"

# Return a newText by replacing various kinds of spaces
# in text with a single space
def replaceWhiteSpace(text):
    element = text.split()
    newText = " ".join(element)
    return newText

# Return a right justified text with a fixed width
def rightJustifyText(text, width):
    text = replaceWhiteSpace(text)
    lenOfStr = len(text)
    i = width
    judgeIndex = i
    while judgeIndex < lenOfStr:
        if text[i] == " ":
            text = text[:i] + "\n" + text[i + 1:]
            judgeIndex = i + width + 1
            i = judgeIndex
        else:
            while text[i] != " ":
                i -= 1
                if text[i] == " ":
                    text = text[:i] + "\n" + text[i + 1:]
                    judgeIndex = i + width + 1
                    i = judgeIndex
                    if judgeIndex > lenOfStr - 1:
                        break
    lines = text.split('\n')
    result = ""
    for line in lines:
        spaces = width - len(line)
        if lines.index(line) != len(lines) - 1:
            result += (" " * spaces + line + "\n")
        else:
            result += (" " * spaces + line)
    return result


#################################################
# Hw2 SOLO problems
#################################################


"""
List your style fixes here:
1: change str to char because str is a function name means turn
 something to a string
2: count_matches_1= 0, for this variable missing a whitespace before the = sign.
The same error with if count_matches_1 !=count_matches_2:
 In order to Fix the style, we
need to write like this if count_matches_1 != count_matches_2:
3: I put the statement print("bad case") before return False.
 If it is after return False,
the statement print("bad case") is unreachable.
4: multiple if statements should be joined into an if-elif-else chain.
5: Comments should be included at the start of
 every function (including helper functions).
"""

# Return True if if s1 and s2 are Anagram (that is, if they contain the same
# letters in possibly-different orders)
def areAnagrams(s1, s2):
    if len(s1) != len(s2):
        print("bad case")
        return False
    else:
        for char in s1:
            one = 1
            count_matches_1 = 0
            count_matches_2 = 0
            for i in range(len(s1)):
                if s1[i] == char:
                    count_matches_1 += one
            for i in range(len(s2)):
                if s2[i] == char:
                    count_matches_2 += one
            if count_matches_1 != count_matches_2:
                return False
        return True


# Return all substrings of a string
def getAllSubstrings(s):
    substrings = ""
    lenOfS = len(s)
    for i in range(0, lenOfS):
        for j in range(i, lenOfS):
            string = s[i: j+1]
            substrings += string + ","
    substrings = substrings[:-1]
    return substrings


# Return common substrings of two strings
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


# Return the longest common substring in common substrings
def longestCommonSubstring(s1, s2):
    if s1 == "" or s2 == "":
        return ""
    elif s1 == s2:
        return s1
    else:
        commonStrings = findCommonSubstrings(s1, s2)
        lenOfMax = 0
        for commonString in commonStrings.split(","):
            if len(commonString) > lenOfMax:
                lenOfMax = len(commonString)
        result = ""
        for commonString in commonStrings.split(","):
            if len(commonString) == lenOfMax:
                result += commonString + ","
        result = result[:-1]
        resultList = result.split(",")
        return min(resultList)


### getEvalSteps is a bonus problem, and therefore optional ###
# Note: Bonus problems are solo. Do not collaborate on bonus problems.
def getEvalSteps(expr):
    return

#################################################
# Hw3 Graphics Functions
# All graphics must go under here to avoid angering the autograder!
# ignore_rest
#################################################
from tkinter import *

# Transfer original string to a new string with equal length of each line
def makeUpString(text):
    lines = text.split("\n")
    maxLenOfLine = len(max(lines, key=len))
    result = ""
    for line in lines:
        blanks = maxLenOfLine - len(line)
        result += (line + blanks * " " + "\n")
    result = result[:-1]
    result = "".join(result)
    return result

# Return the number of the row of Canvas need to draw
def findRowOfCanvas(text):
    text = makeUpString(text)
    height = 0
    for c in text:
        if c == "\n":
            height += 1
    height += 1
    return height

# Return the number of the column of Canvas need to draw
def findColOfcanvas(text):
    text = makeUpString(text)
    lines = text.split("\n")
    column = len(lines[0])
    return column

def getColor(line, i):
    color = ""
    if line[i] == "0":
        color = "#000"
    elif line[i] == "1":
        color = "#00F"
    elif line[i] == "2":
        color = "#0F0"
    elif line[i] == "3":
        color = "#0FF"
    elif line[i] == "4":
        color = "#F00"
    elif line[i] == "5":
        color = "#F0F"
    elif line[i] == "6":
        color = "#FF0"
    elif line[i] == "7":
        color = "#FFF"
    return color

# This is the main function of asciiDraw
def asciiDraw(canvas, artStr, width, height):
    newText = makeUpString(artStr)
    rowOfCanvas = findRowOfCanvas(newText)
    colOfCanvas = findColOfcanvas(newText)
    heightOfRectangle = height / rowOfCanvas
    widthOfRectangle = width / colOfCanvas
    j = 0
    for line in newText.split("\n"):
        for i in range(len(line)):
            left = 0 + i * widthOfRectangle
            top = 0 + j * heightOfRectangle
            right = left + widthOfRectangle
            bottom = top + heightOfRectangle
            color = getColor(line, i)
            canvas.create_rectangle(left, top, right, bottom, fill=color, width=0)
        j += 1


#################################################
# Hw3 Test Functions
#################################################

import string


def testGradebookSummary():
    print("Testing gradebookSummary()...", end="")
    import os
    if not os.path.exists("hw3_files"):
        assert False,"You need to unzip hw3_files.zip to test gradebookSummary"

    assert(gradebookSummary("hw3_files/gradebook1.txt") ==
            "wilma\t92.67\nfred\t90.40\nbetty\t88.00")
    assert(gradebookSummary("hw3_files/gradebook2.txt") ==
            "wilma\t92.67\nfred\t90.40\nbetty\t88.00")
    assert(gradebookSummary("hw3_files/small1.txt") ==
            "fred\t0.00")
    assert(gradebookSummary("hw3_files/small2.txt") ==
            "fred\t-1.00\nwilma\t-2.00")
    assert(gradebookSummary("hw3_files/small3.txt") ==
            "fred\t100.50")
    assert(gradebookSummary("hw3_files/small4.txt") ==
            "fred\t49.00\nwilma\t50.00")
    print("Passed.")

def testApplyCaesarCipher():
    print("Testing applyCaesarCipher()...", end="")
    assert(applyCaesarCipher("abcdefghijklmnopqrstuvwxyz", 3) == \
        "defghijklmnopqrstuvwxyzabc")
    assert(applyCaesarCipher("We Attack At Dawn", 1) == "Xf Buubdl Bu Ebxo")
    assert(applyCaesarCipher("1234", 6) == "1234")
    print("Passed.")

def testRightJustifyText():
    print("Testing rightJustifyText()...", end="")
    text1 = """\
We hold these truths to be self-evident:  that all men are created equal;
that they are endowed by their Creator with certain unalienable rights;
that among these are life, liberty, and the pursuit of happiness."""
    text1Result = """\
    We hold these truths to be
self-evident: that all men are
  created equal; that they are
 endowed by their Creator with
   certain unalienable rights;
    that among these are life,
   liberty, and the pursuit of
                    happiness."""
    assert(rightJustifyText(text1, 30) == text1Result)
    text2 = """\
Though, in reviewing the incidents of my administration,
I am unconscious of intentional error, I am nevertheless too sensible of my
defects not to think it probable that I may have committed many errors.
I shall also carry with me the hope that my country will view them with
indulgence; and that after forty-five years of my life dedicated to its service
with an upright zeal, the faults of incompetent abilities will be consigned to
oblivion, as I myself must soon be to the mansions of rest.

I anticipate with pleasing expectation that retreat in which I promise myself
to realize the sweet enjoyment of partaking, in the midst of my fellow-citizens,
the benign influence of good laws under a free government,
the ever-favorite object of my heart, and the happy reward,
as I trust, of our mutual cares, labors, and dangers."""
    text2Result = """\
         Though, in reviewing the incidents of my administration, I am
unconscious of intentional error, I am nevertheless too sensible of my
       defects not to think it probable that I may have committed many
 errors. I shall also carry with me the hope that my country will view
      them with indulgence; and that after forty-five years of my life
          dedicated to its service with an upright zeal, the faults of
 incompetent abilities will be consigned to oblivion, as I myself must
           soon be to the mansions of rest. I anticipate with pleasing
     expectation that retreat in which I promise myself to realize the
 sweet enjoyment of partaking, in the midst of my fellow-citizens, the
            benign influence of good laws under a free government, the
ever-favorite object of my heart, and the happy reward, as I trust, of
                                our mutual cares, labors, and dangers."""
    assert(rightJustifyText(text2, 70) == text2Result)
    print("Passed.")

def testLongestCommonSubstring():
    print("Testing longestCommonSubstring()...", end="")
    assert(longestCommonSubstring("abcdef", "abqrcdest") == "cde")
    assert(longestCommonSubstring("abcdef", "ghi") == "")
    assert(longestCommonSubstring("", "abqrcdest") == "")
    assert(longestCommonSubstring("abcdef", "") == "")
    assert(longestCommonSubstring("abcABC", "zzabZZAB") == "AB")
    print("Passed.")

def runAsciiDraw(artStr, width, height):
    root = Tk()
    root.resizable(width=False, height=False) # prevents resizing window
    canvas = Canvas(root, width=width, height=height)
    canvas.configure(bd=0, highlightthickness=0)
    canvas.pack()
    asciiDraw(canvas, artStr, width, height)
    root.mainloop()

def testAsciiDraw():
    testPattern="0123\n4567"
    print("Testing asciiDraw with color pattern:\n",testPattern,end="")
    runAsciiDraw(testPattern, 600, 300)

    diamondPattern=''' 
  1     2     4
 111   222   444
11111 22222 44444
 111   222   444
  1     2     4
 '''

    print("Testing asciiDraw with diamond pattern:\n",diamondPattern,end="")
    runAsciiDraw(diamondPattern, 600, 300)

    facePattern = ''' 
                          0022222222222222222
                      02222222222222222222222220
                   02222222222222222222222222222220         02   02 02
   0 0 0        02222222222222222222222222222222222220       02 22 2202
0 2 2 02      0222222222    2222222222222    2222222220       02202202
022222202     0222222222      22222222222      22222222220    02222222
  0222222    02222222222      22222222222      22222222222222222222222
  02222222222222222222222    2222222222222    22222222222222  0222
   022202222222222222222222222222222222222222222222222222222    0222
    022   022222222222222222222222222222222222222222222222222     02220
   0220   222222222222222222222222222222222222222222222222222       2220
   022    222222222222222222222222222222222222222222222000222222022220
  0222022222  2222222222222222222222222222222222222   022222222222222222
  0222   202222   2222222222222222222222222222222222     02220
 0222       0222    022222222222222222222222222220      0222
            02220     02222222222222222220220           022
              0220          02202222220              0222
               02220                                02220
                022220      02222220022220        02222
                  0222220     022222222220   022220
                     0222220  022222222222220
                        02222222022222222222
                                022222222222
                                   022222222222
                                     02222222220
                                      02220
                                      
 '''
    print("Testing asciiDraw with face pattern:\n",facePattern,end="")
    runAsciiDraw(facePattern, 800, 600)

    hourglassPattern = ''' 
                            0000
        00000000000000000000    00
00000000            0000000000000 00
0 000000000000000000         000000 00
0000                11111    0 0   00 00
00 0        111111111111111110 0   0000 0
 0 000000111111111111111111110 00000 0000
 0 0   0 111111111111111111110 0   0 0
 0 0   0 111111111111111555550 0   0 0
 0 0   0 111111111555644644640 0   0 0
 0 0   0 111115546446446446440 0   0 0
 0 0   0 111546464464464464460 0   0 0
 0 0   0 154644644644644646660 0   0 0
 0 0   0 056446446446666666660 0   0 0
 0 0   0 0 5666666666666666650 0   0 0
 0 0   0 0  566666666666666510 0   0 0
 0 0   0 0   16666666666661  0 0   0 0
 0 0   0 0    116666666651   0 0   0 0
 0 0   0 0       1156111     0 0   0 0
 0 0   0 0         55        0 0   0 0
 0 0   0 0      11165111     0 0   0 0
 0 0   0 0    1111156111111  0 0   0 0
 0 0   0 0   111111551111111 0 0   0 0
 0 0   0 0  111111165111111110 0   0 0
 0 0   0 0 1111111155111111110 0   0 0
 0 0   0 011111111161111111110 0   0 0
 0 0   0 011111111161111111110 0   0 0
 0 0   0 111111115666511111110 0   0 0
 0 0   0 111111156666651111110 0   0 0
 0 0   0 111111566666665111110 0   0 0
 0 0   01111115666666666511110 0   0 0
 0 0 0001111156666666666651110 00000 0000
 0 00   1111566666666666665110 0   000 00
 0 0    1111566666666666666510 0     00 0
00000   0115666666666666666510 0   00  00
0    00000000006666660000    000 00  00
0000000000000  111111  0000000000  00
            00000000000000000000000
 '''
    print("Testing asciiDraw with hourglass pattern:\n",hourglassPattern,end="")
    runAsciiDraw(hourglassPattern, 400, 600)
    print("Done testing asciiDraw!")

def testBonusGetEvalSteps():
    print("Testing getEvalSteps()...", end="")
    assert(getEvalSteps("0") == "0 = 0")
    assert(getEvalSteps("2") == "2 = 2")
    assert(getEvalSteps("3+2") == "3+2 = 5")
    assert(getEvalSteps("3-2") == "3-2 = 1")
    assert(getEvalSteps("3**2") == "3**2 = 9")
    assert(getEvalSteps("31%16") == "31%16 = 15")
    assert(getEvalSteps("31*16") == "31*16 = 496")
    assert(getEvalSteps("32//16") == "32//16 = 2")
    assert(getEvalSteps("2+3*4") == "2+3*4 = 2+12\n      = 14")
    assert(getEvalSteps("2*3+4") == "2*3+4 = 6+4\n      = 10")
    assert(getEvalSteps("2+3*4-8**3%3") == """\
2+3*4-8**3%3 = 2+3*4-512%3
             = 2+12-512%3
             = 2+12-2
             = 14-2
             = 12""")
    assert(getEvalSteps("2+3**4%2**4+15//3-8") == """\
2+3**4%2**4+15//3-8 = 2+81%2**4+15//3-8
                    = 2+81%16+15//3-8
                    = 2+1+15//3-8
                    = 2+1+5-8
                    = 3+5-8
                    = 8-8
                    = 0""")
    print("Passed.")

#################################################
# Hw3 Main
#################################################

def testAll():
    testGradebookSummary()
    testApplyCaesarCipher()
    testRightJustifyText()
    testLongestCommonSubstring()
    testAsciiDraw()

    #Uncomment the next line if you want to try the bonus!
    #testBonusGetEvalSteps()


def main():
    cs112_s19_week3_linter.lint() # check for banned tokens
    # testAll()

if __name__ == '__main__':
    main()


print(longestCommonSubstring("abcdef", "abqrcdest"))