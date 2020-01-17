#################################################
# Hw4
# Your andrewID:mxu2
# Your section: 2N
#################################################

import math
import copy
    
#################################################
# Hw4 COLLABORATIVE problems
#################################################
# The problem in this section is COLLABORATIVE, which means you may
#     work on it with your classmates if you wish.  See the collaboration
#     policy in the syllabus for more details.  Always list your collaborators!


def lookAndSayCollaborators():
    return "nobody"


# get the result in function lookAndSay
def getResult(i, listNum, count, result):
    if listNum[i] == listNum[i - 1]:
        result.append((count, listNum[i - 1]))
    else:
        result.append((1, listNum[i]))


# Return "reading off" of the list using the look-and-say method
def lookAndSay(lst):
    listNum = list(lst)
    result = []
    count = 1
    if listNum == []:
        return []
    elif listNum != []:
        for i in range(len(listNum)):
            if (i + 1) < len(listNum) and listNum[i + 1] == listNum[i]:
                count += 1
            else:
                if i == 0 and listNum[i + 1] != listNum[i]:
                    result.append((1, listNum[0]))
                elif i == 0 and listNum[i + 1] == listNum[i]:
                    continue
                else:
                    getResult(i, listNum, count, result)
                count = 1
    return result


def inverseLookAndSayCollaborators():
    return "nobody"


# Return the inverse list of the function lookAndSay
def inverseLookAndSay(lst):
    result = []
    for element in lst:
        n = element[0]
        num = element[1]
        while n > 0:
            result.append(num)
            n -= 1
    return result

#################################################
# Hw4 SOLO problems
#################################################


# Remove all the repeats in a list without destruct original list
def nondestructiveRemoveRepeats(lst):
    result = []
    for num in lst:
        if num not in result:
            result.append(num)
    return result


# Remove all the repeats in a list by destructing the original list
def destructiveRemoveRepeats(lst):
    for i in range(len(lst) - 1, -1, -1):
        if lst.count(lst[i]) > 1:
            lst.pop(i)

# get value of each letter
def valueOfLetter(letterScores, letter):
    indexOfLetter = ord(letter) - 97
    value = letterScores[indexOfLetter]
    return value

# get scores of target word list
def getScoresOfWords(letterScores, targetWordLst):
    scores = []
    for i in range(len(targetWordLst)):
        score = 0
        for j in range(len(targetWordLst[i])):
            score += valueOfLetter(letterScores, targetWordLst[i][j])
        scores.append(score)
    return scores

# get index of target
def getIndexOfTarget(idx, scoreList, maxScore):
    i = 0
    while i < len(scoreList):
        if scoreList[i] == maxScore:
            idx.append(i)
        i += 1
    return idx

# This is the final target word list
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

# This is the main function of best scrabble score,
# which will return the highest score with word list
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
    if not scoreList:  # if scoreList == []:
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


#################################################
# Hw4 Graphics & Animation Functions
# All graphics must go under here to avoid angering the autograder!
# ignore_rest
#################################################
from tkinter import *

## Tortoise Animation functions ##
## Note - the Tortoise animation is collaborative! ##

## Tortoise Animation bonus features: none ##

def tortoiseAnimationCollaborators():
    return "nobody"


# This is the init function of animation
def init(data):
    data.torX = data.width/2
    data.torY = data.height/2
    data.commands = listOfDataCode(data)
    data.commandsToDraw = []
    data.torToDraw = []
    data.counter = 0

# Return list of data code
def listOfDataCode(data):
    lstOfDataCode = []
    for line in data.code.split("\n"):
        lstOfDataCode.append(line)
    lstOfDataCode.pop()
    lstOfDataCode = lstOfDataCode[1:]
    return lstOfDataCode

# this is a mouse event handler
def mousePressed(event, data):
    pass

# this is a keyboard event handler
def keyPressed(event, data):
        if (event.keysym == "Return"):
            if data.counter < len(data.commands):
                data.commandsToDraw.append((data.commands[data.counter], data.counter))
                data.counter += 1

# Get information of each command
def getInformationOfCommands(text, color, x, y, angle):
    if text.startswith('color'):
        color = text[6:]
    elif text.startswith('left'):
        angle = angle - int(text[5:])
    elif text.startswith('right'):
        angle = angle + int(text[6:])
    return color, x, y, angle

# This is the run current line function
def runProgram(canvas, data, currentLine):
    color = ""
    angle = 0
    for i in range(currentLine):
        canvas.create_text(data.width/50,
                           data.height/20 + data.commandsToDraw[i][1]*data.height/30,
                           text=str(data.commandsToDraw[i][0]), anchor="w", fill='gray')
        getInformationOfCommands(data.commandsToDraw[i][0], color, data.torX, data.torY, angle)


# this function get the coordinate of the black rectangle
def getCoordinateOfRectangle(width, height):
    recx0 = 0
    recy0 = (9 / 10) * height
    recx1 = width
    recy1 = height
    return recx0, recy0, recx1, recy1

# this function get the color of the small rectangles
def getColorOfBox(i):
    if i == 0:
        color = 'red'
    elif i == 1:
        color = 'orange'
    elif i == 2:
        color = 'yellow'
    elif i == 3:
        color = 'green'
    elif i == 4:
        color = 'blue'
    elif i == 5:
        color = 'purple'
    else:
        color = 'white'
    return color

# this function get the coordinates of the small rectangles
def coordinatesInLoop(margin, i, widthOfRectangles, recy0):
    x0 = margin + i * widthOfRectangles + i * margin
    y0 = recy0 + margin
    x1 = x0 + widthOfRectangles
    y1 = y0 + widthOfRectangles - margin
    return x0, y0, x1, y1

# this is the main animation function
def redrawAll(canvas, data):
    currentLine = data.counter
    runProgram(canvas, data, currentLine)
    margin = (1/100)*data.height
    widthOfRectangles = (data.width - 11 * margin)/10
    recx0, recy0, recx1, recy1 = getCoordinateOfRectangle(data.width, data.height)
    canvas.create_rectangle(recx0, recy0, recx1, recy1, fill='black')
    for i in range(10):
        x0, y0, x1, y1 = coordinatesInLoop(margin, i, widthOfRectangles, recy0)
        color = getColorOfBox(i)
        canvas.create_rectangle(x0, y0, x1, y1, fill=color)


""" This function is provided as part of the starter code.
You don't need to change it, but you should call it!"""
def drawArrow(canvas, x, y, angle):
    offset = 135
    r = 10
    x1 = x + r*math.cos(math.radians(angle))
    y1 = y - r*math.sin(math.radians(angle))
    x2 = x + r*math.cos(math.radians(angle + offset))
    y2 = y - r*math.sin(math.radians(angle + offset))
    x3 = x + r*math.cos(math.radians(angle - offset))
    y3 = y - r*math.sin(math.radians(angle - offset))
    canvas.create_polygon(x1, y1, x2, y2, x3, y3, fill="black")


### Timeline Game is a bonus problem, and therefore optional ###
# Note: Bonus problems are solo. Do not collaborate on bonus problems.

## Timeline Game functions ##

""" This function is provided as part of the starter code.
You don't need to change it, but you should call it!"""
def starterCards():
    import random
    cards = [ ("Domestication of the Cat", -4500),
              ("Creation of the Pythagorean Theorem", -548),
              ("Invention of Chess", 570),
              ("First Calculating Machine", 1642), 
              ("Invention of the Telegraph", 1837),
              ("Invention of Morse Code", 1838),
              ("Invention of the Plastic Bottle", 1963), 
              ("Invention of the Computer Mouse", 1963), 
              ("Invention of the Laptop Computer", 1981),
              ("First Public Internet Access", 1990)
            ]
    random.shuffle(cards)
    return cards

def initTimeline(data):
    pass

def mousePressedTimeline(event, data):
    pass

def keyPressedTimeline(event, data):
    pass

def redrawAllTimeline(canvas, data):
    pass

#################################################
# Hw4 Test Functions
#################################################

def _verifyLookAndSayIsNondestructive():
    a = [1,2,3]
    b = copy.copy(a)
    lookAndSay(a) # ignore result, just checking for destructiveness here
    return (a == b)

def testLookAndSay():
    print("Testing lookAndSay()...", end="")
    assert(_verifyLookAndSayIsNondestructive() == True)
    assert(lookAndSay([]) == [])
    assert(lookAndSay([1,1,1]) ==  [(3,1)])
    assert(lookAndSay([-1,2,7]) == [(1,-1),(1,2),(1,7)])
    assert(lookAndSay([3,3,8,-10,-10,-10]) == [(2,3),(1,8),(3,-10)])
    print("Passed.")

def _verifyInverseLookAndSayIsNondestructive():
    a = [(1,2), (2,3)]
    b = copy.copy(a)
    inverseLookAndSay(a) # ignore result, just checking for destructiveness here
    return (a == b)

def testInverseLookAndSay():
    print("Testing inverseLookAndSay()...", end="")
    assert(_verifyInverseLookAndSayIsNondestructive() == True)
    assert(inverseLookAndSay([]) == [])
    assert(inverseLookAndSay([(3,1)]) == [1,1,1])
    assert(inverseLookAndSay([(1,-1),(1,2),(1,7)]) == [-1,2,7])
    assert(inverseLookAndSay([(2,3),(1,8),(3,-10)]) == [3,3,8,-10,-10,-10])
    print("Passed.")

def runTortoiseAnimation(code, width=500, height=500):
    def redrawAllWrapper(canvas, data):
        canvas.delete(ALL)
        canvas.create_rectangle(0, 0, data.width, data.height,
                                fill='white', width=0)
        redrawAll(canvas, data)
        canvas.update()    

    def mousePressedWrapper(event, canvas, data):
        mousePressed(event, data)
        redrawAllWrapper(canvas, data)

    def keyPressedWrapper(event, canvas, data):
        keyPressed(event, data)
        redrawAllWrapper(canvas, data)

    class Struct(object): pass
    data = Struct()
    data.width = width
    data.height = height
    data.code = code
    root = Tk()
    root.resizable(width=False, height=False) # prevents resizing window
    init(data)
    canvas = Canvas(root, width=data.width, height=data.height)
    canvas.configure(bd=0, highlightthickness=0)
    canvas.pack()
    root.bind("<Button-1>", lambda event:
                            mousePressedWrapper(event, canvas, data))
    root.bind("<Key>", lambda event:
                            keyPressedWrapper(event, canvas, data))
    redrawAllWrapper(canvas, data)
    root.mainloop()  # blocks until window is closed

def testTortoiseAnimation():
    print("Running Tortoise Animation...", end="")
    runTortoiseAnimation("""
# This is a simple tortoise program
color blue
move 50

left 90

color red
move 100

color none # turns off drawing
move 50

right 45

color green # drawing is on again
move 50

right 45

color orange
move 50

right 90

color purple
move 100
""")
    runTortoiseAnimation("""
# Y
color red
right 45
move 50
right 45
move 50
right 180
move 50
right 45
move 50
color none # space
right 45
move 25

# E
color green
right 90
move 85
left 90
move 50
right 180
move 50
right 90
move 42
right 90
move 50
right 180
move 50
right 90
move 43
right 90
move 50  # space
color none
move 25

# S
color blue
move 50
left 180
move 50
left 90
move 43
left 90
move 50
right 90
move 42
right 90
move 50
""")
    print("Done.")

def _verifyNondestructiveRemoveRepeatsIsNondestructive():
    a = [3, 5, 3, 3, 6]
    b = copy.copy(a)
    # ignore result, just checking for destructiveness here
    nondestructiveRemoveRepeats(a)
    return (a == b)

def testNondestructiveRemoveRepeats():
    print("Testing nondestructiveRemoveRepeats()", end="")
    assert(_verifyNondestructiveRemoveRepeatsIsNondestructive())
    assert(nondestructiveRemoveRepeats([1,3,5,3,3,2,1,7,5]) == [1,3,5,2,7])
    assert(nondestructiveRemoveRepeats([1,2,3,-2]) == [1,2,3,-2])
    print("Passed.")

def testDestructiveRemoveRepeats():
    print("Testing destructiveRemoveRepeats()", end="")
    a = [1,3,5,3,3,2,1,7,5]
    assert(destructiveRemoveRepeats(a) == None)
    assert(a == [1,3,5,2,7])
    b = [1,2,3,-2]
    assert(destructiveRemoveRepeats(b) == None)
    assert(b == [1,2,3,-2])
    print("Passed.")

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

def runTimelineGame(width=1200, height=400):
    def redrawAllWrapper(canvas, data):
        canvas.delete(ALL)
        canvas.create_rectangle(0, 0, data.width, data.height,
                                fill='white', width=0)
        redrawAllTimeline(canvas, data)
        canvas.update()    

    def mousePressedWrapper(event, canvas, data):
        mousePressedTimeline(event, data)
        redrawAllWrapper(canvas, data)

    def keyPressedWrapper(event, canvas, data):
        keyPressedTimeline(event, data)
        redrawAllWrapper(canvas, data)

    class Struct(object): pass
    data = Struct()
    data.width = width
    data.height = height
    root = Tk()
    root.resizable(width=False, height=False) # prevents resizing window
    initTimeline(data)
    canvas = Canvas(root, width=data.width, height=data.height)
    canvas.configure(bd=0, highlightthickness=0)
    canvas.pack()
    root.bind("<Button-1>", lambda event:


                            mousePressedWrapper(event, canvas, data))
    root.bind("<Key>", lambda event:
                            keyPressedWrapper(event, canvas, data))
    redrawAllWrapper(canvas, data)
    root.mainloop()  # blocks until window is closed

#################################################
# Hw4 Main
#################################################

def testAll():
    ## Collaborative Functions ##
    testLookAndSay()
    testInverseLookAndSay()
    testTortoiseAnimation()
    ## Solo Functions ##
    testNondestructiveRemoveRepeats()
    testDestructiveRemoveRepeats()
    testBestScrabbleScore()
    
    # Uncomment the next line if you want to try the bonus!
    #runTimelineGame()

def main():
    testAll()

if __name__ == '__main__':
    main()