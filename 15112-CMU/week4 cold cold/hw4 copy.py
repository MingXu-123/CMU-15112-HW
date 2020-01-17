#################################################
# Hw4
# Your andrewID:yufeiche
# Your section: J
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

# A function that return the "reading off" list
def lookAndSay(lst):
    newList = []
    # consider an exception
    if lst == []:
        return []
    else:
        # create non-destructively function
        createLst = copy.copy(lst)
        i = 0
        while i < len(createLst):
            newValue = createLst[i]
            countNumber = 0
            while (i + countNumber < len(createLst) and lst[i + countNumber] == newValue):
                countNumber += 1
            i += countNumber
            newList += [(countNumber, newValue)]
    return newList


def inverseLookAndSayCollaborators():
    return "nobody"

# a function that does the inverse of the function lookAndSay    
def inverseLookAndSay(lst):
    # consider an exception
    if lst == []:
        return []
    else:
        # create a new list
        newList = []
        # find every tuple in list
        for i in range(len(lst)):
            (x,y) = lst[i]
            # add item y to newList x times
            for j in range(x):
                newList += [y]
    return newList

#################################################
# Hw4 SOLO problems
#################################################

# a function that non destructively remove the repeated values in list
def nondestructiveRemoveRepeats(lst):
    # non destructively copy the list
    copyLst = copy.copy(lst)
    newList = []
    i = 0
    while i < len(copyLst):
        newValue = copyLst[i]
        # count the number of newValue in string
        countNumber = copyLst.count(newValue)
        newList += [copyLst[i]]
        # leave only one per value in string
        for j in range(countNumber):
            copyLst.remove(newValue)
        i = 0
    return newList

# a function that destructively remove the repeated values in list
def destructiveRemoveRepeats(lst):
    i = 0
    # reverse the list
    lst.reverse()
    while i < len(lst):
        newValue = lst[i]
        # count the number of newValue in string
        countNumber = lst.count(newValue)
        if countNumber == 1:
            i += 1
        # leave only one per value in string
        for j in range(countNumber-1):
            lst.remove(newValue)
    lst.reverse()

# return the letterScore value of all the sting in a list
def returnValue(letterScore,lst):
    totalValue = 0
    for i in range(len(lst)):
        # order the string in alphabet
        j = ord(lst[i])-97
        totalValue += letterScore[j]
    return totalValue

# return whether alphabet in list can make up word
def createWords(word,lst):
    newStr = ""
    lst = copy.copy(lst)
    i = 0
    j = 0
    while i < len(word):
        while j < len(lst):
            # a new string to add alphabets that match
            if word[i] == lst[j]:
                newStr += word[i]
                lst[j] = " " 
                j = len(lst)
            else:
                j += 1
        i += 1
        j = 0
    # whether the match alphabets equal to the oroginal word
    if newStr == word:
        return True
    else:
        return False

# return the highest score as well as match words from dictionary
def bestScrabbleScore(dictionary,letterScore,hand):
    highestScore = 0
    returnWord = []
    newStr = ""
    for i in range(len(dictionary)):
        # see if string in hand matches word in dictionary
        if createWords(dictionary[i],hand) == True:
            # if match, calculate the value of that word
            totalValue = returnValue(letterScore,dictionary[i])
            # compare its score with the highest score
            if highestScore < totalValue:
                highestScore = totalValue
                returnWord = [dictionary[i]]
            elif highestScore == totalValue:
                returnWord += [dictionary[i]]
    
    if len(returnWord) == 1:
        return(returnWord[0], highestScore)
    # if no word match, return none
    elif len(returnWord) == 0:
        return None
    else:
        return (returnWord,highestScore)
    
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

# initialize the GUI
def init(data):
    data.x = data.width/2
    data.y = data.height/2
    data.angle = 0
    data.lineX = data.width/50
    data.lineY = data.height/40
    
    # breaks code into series of commands
    data.counter = 0
    data.commands = data.code.split("\n")
    
    # keeps track of lines
    data.lineCenter = []
    
    # keeps track of rectangles
    data.color = "black"
    data.text = ""
    colorTuple = ("red","orange","yellow","green","blue","purple","white",
                  "white","white","white")
    data.rectlist = [(i*data.width/10,data.height-data.width/10, (i+1) * 
                data.width/10,data.height, colorTuple[i]) for i in range(10)]


# register mouse press
def mousePressed(event, data):
    # ckecks if first 7 rectangles are clicked
    for r in data.rectlist[:6]:
        if (event.x > r[0] and event.x < r[2] and event.y > r[1] 
            and event.y < r[3]):
            data.counter += 1
            data.commands.insert(data.counter, "color "+ r[4])
    if (event.x > data.rectlist[6][0] and event.x < data.rectlist[6][2] and
        event.y > data.rectlist[6][1] and event.y < data.rectlist[6][3]):
        data.counter += 1
        data.commands.insert(data.counter, "color none")
    # checks if last 3 rectangles are clicked
    for i in range(3):
        if (event.x > data.rectlist[7 + i][0] and 
            event.x < data.rectlist[7 + i][2] and 
            event.y > data.rectlist[7 + i][1] and 
            event.y < data.rectlist[7 + i][3]):
            data.counter += 1
            data.commands.insert(data.counter, "move " + str((5, 25, 50)[i] ) ) 

# registers keypress
def keyPressed(event, data):
    if event.keysym == "Return":
        data.counter += 1
    elif event.keysym == "Left":
        data.counter += 1
        data.commands.insert(data.counter, "left 30")
    elif event.keysym == "Right":
        data.counter += 1
        data.commands.insert(data.counter, "right 30")

# helper function called by redrawAll and draws graphics 
def runProgram(canvas, data, currentLine):
    if currentLine < len(data.commands):
        data.text += (data.commands[currentLine] + "\n")
        moveDistance(canvas,data, currentLine)
        turnAngle(canvas,data, currentLine)
    else:
        data.counter = len(data.commands) - 1
    canvas.create_text(data.lineX,data.lineY, text = data.text, fill = "grey", 
                       anchor = "nw")
                       
    drawLines(canvas,data)
    drawArrow(canvas,data.x,data.y,data.angle)
    
    # draws squares on the bottom
    sideRectangle = data.width/10
    colorTuple = ("red","orange","yellow","green","blue","purple","white",
                 "white","white","white")
    for r in data.rectlist:
        canvas.create_rectangle(r[0],r[1],r[2],r[3],fill = r[4], width = 3)
    canvas.create_text(data.width*7.5/10,data.height-data.width/20,text = "5")
    canvas.create_text(data.width*8.5/10,data.height-data.width/20,text = "25")
    canvas.create_text(data.width*9.5/10,data.height-data.width/20,text = "50")    
    

# helper function controls the movement of the graphic
def moveDistance(canvas,data,currentLine):
    currentContent = data.commands[currentLine]
    newList = currentContent.split(" ")
    if newList[0] == "move":
        newX = data.x + int(newList[1])*math.cos(math.radians(data.angle))
        newY = data.y - int(newList[1])*math.sin(math.radians(data.angle))
        data.lineCenter += [(data.x,data.y,newX,newY,data.color)]
        data.x = newX
        data.y = newY
    if newList[0] == "color":
        data.color = newList[1]
        
# helper function draws the line        
def drawLines(canvas,data):
    for tuple in data.lineCenter:
        if(tuple[4] != 'none'):
            canvas.create_line(tuple[0],tuple[1],tuple[2],tuple[3],
                               fill = tuple[4],width = 5)
    
    
# helper function controls the angle of the graphic
def turnAngle(canvas,data,currentLine):
    currentContent = data.commands[currentLine]
    newList = currentContent.split(" ")
    if newList[0] == "left":
        data.angle += int(newList[1])
    elif newList[0] == "right":
        data.angle -= int(newList[1])
        
# main function
def redrawAll(canvas, data):
    runProgram(canvas, data, data.counter)
    


""" This function is provided as part of the starter code.
You don't need to change it, but you should call it!"""
def drawArrow(canvas, x, y, angle):
    offset = 135
    r = 10
    x1 = x + r*math.cos(math.radians(angle))
    y1 = y - r*math.sin(math.radians(angle))
    x2 = x + r*math.cos(math.radians(angle + offset))
    y2 = y - r*math.sin(math.radians(angle + offset))
    x3 = x + r*math.cos (math.radians(angle - offset))
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