#################################################
# Hw2
# Your andrewID: mxu2
# Your section: 2 N
#################################################

import cs112_s19_week2_linter

### You'll need isPrime for one of the problems, so it is provided here ###
def isPrime(n):
    if (n < 2):
        return False
    maxFactor = round(n**0.5)
    for factor in range(2, maxFactor+1):
        if (n % factor == 0):
            return False
    return True

#################################################
# Lab2 COLLABORATIVE LAB problems
# (Their problem descriptions will be released Friday, Jan 25)
#################################################
# The problems in this section are LAB PROBLEMS, which means you MUST
#     work on these with at least one collaborator.  See the collaboration
#     policy in the syllabus for more details.  Always list your collaborators!
#     For lab problems, YOU MUST LIST AT LEAST ONE COLLABORATOR

def isSmithNumberCollaborators():
    return "yufeiche"


def sum_digits(n):
    sum = 0
    while n:
        sum += n % 10
        n //= 10
    return sum


def isSmithNumber(n):
    if isPrime(n):
        return False
    sumofdigit = sum_digits(n)
    sumOfPrimeFactor = 0
    for factor in range(2, n + 1):
        if isPrime(factor):
            while n % factor == 0:
                sumOfPrimeFactor += sum_digits(factor)
                n = n / factor
    if sumOfPrimeFactor == sumofdigit:
        return True
    else:
        return False


### You can find drawFlagOfCuba in the Graphics section below ###

#################################################
# Hw2 COLLABORATIVE problem
#################################################
# The problems in this section are COLLABORATIVE, which means you may
#     work on them with your classmates if you wish.  See the collaboration
#     policy in the syllabus for more details.  Always list your collaborators!

#### Debugging isMultiPowerfulNumber is a COLLABORATIVE problem ####
def isMultiPowerfulNumberCollaborators():
    return "nobody"

# Bug 1: n % factor should be == 0, = means assign a value to some value, and in this same line
# I put isPrime(factor) before n % factor for the simple reason that if I put n % factor before the key work and
# when factor == 0, there will be a ZeroDivisionError. So if isPrime(0) is False, python will not check n % 0.
# Bug 2: I replace return False after the second if statement with continue,
# because if n % an square of factor is not equal to 0 the return False statement will ends the loop.
# So, I replace it with continue.
# Bug 3: The factorCount += 1 should move to right with on more indent.Because after the second if statement
# if n % (factor**2) == 0, it should be prime factor for multi-powerful number and factorCount should plus 1.

#### Insert the isMultiPowerfulNumber code here ####
def isMultiPowerfulNumber(n):
    factorCount = 0
    for factor in range(n):
        if isPrime(factor) and n % factor == 0:
            if n % (factor**2) != 0:
                continue
            factorCount += 1
    return factorCount > 1


#################################################
# Hw2 SOLO problems
#################################################

def isKaprekarNumber(n):
    if n < 1:
        return False
    if n == 1:
        return True
    lenOfNumsquare = len(str(n**2))
    for i in range(1, lenOfNumsquare):
        A = n**2 // 10 ** i
        B = n**2 % 10 ** i
        if B != 0 and A + B == n:
            return True
    return False


def nthKaprekarNumber(n):
    found = -1
    guess = 0
    while (found < n):
        guess += 1
        if (isKaprekarNumber(guess)):
            found += 1
    return guess


def nearestKaprekarNumber(n):
    if n <= 1:
        return 1
    count = 1
    if type(n) == int:
        if isKaprekarNumber(n):
            return n
        while not isKaprekarNumber(n):
            a = n - count
            if isKaprekarNumber(a):
                return a
            b = n + count
            if isKaprekarNumber(b):
                return b
            count += 1
    if type(n) == float:
        import math
        rawnum = n
        count = 1
        if (n - int(n)) <= 0.5:
            if isKaprekarNumber(int(n)):
                return int(n)
            while not isKaprekarNumber(int(n)):
                a = int(n) - count
                if isKaprekarNumber(a):
                    targeta = a
                    break
                count += 1
            count = 1
            while not isKaprekarNumber(int(n)):
                b = int(n) + count
                if isKaprekarNumber(b):
                    targetb = b
                    break
                count += 1
            if abs(rawnum - targeta) <= abs(targetb - rawnum):
                return targeta
            if abs(rawnum - targeta) > abs(targetb - rawnum):
                return targetb
        if (n - int(n)) > 0.5:
            if isKaprekarNumber(math.ceil(n)):
                return math.ceil(n)
            while not isKaprekarNumber(math.ceil(n)):
                a = math.ceil(n) - count
                if isKaprekarNumber(a):
                    targeta = a
                    break
                count += 1
            count = 1
            while not isKaprekarNumber(math.ceil(n)):
                b = math.ceil(n) + count
                if isKaprekarNumber(b):
                    targetb = b
                    break
                count += 1
            if abs(rawnum - targeta) <= abs(targetb - rawnum):
                return targeta
            if abs(rawnum - targeta) > abs(targetb - rawnum):
                return targetb


### The three following problems are bonus problems, and therefore optional ###
# Note: Bonus problems are solo. Do not collaborate on bonus problems.

def squaresGenerator():
    return

def nswGenerator():
    return

def nswPrimesGenerator():
    return

#################################################
# Hw2 Graphics Functions
# All graphics must go under here to avoid angering the autograder!
# ignore_rest
#################################################

from tkinter import *

### Note that drawFlagOfCuba is COLLABORATIVE and a LAB problem ###
def drawFlagOfCubaCollaborators():
    return "afu1"

def drawFlagOfCuba(canvas, width, height):
    heightofrec = height / 5
    for row in range(5):
        left = 0
        top = 0 + row * heightofrec
        right = width
        bottom = width * heightofrec
        if row == 0 or row == 2 or row == 4:
            color = "darkblue"
        else:
            color = "white"
        canvas.create_rectangle(left, top, right, bottom, fill=color)
        canvas.create_polygon(0, 0, 0, height, (3**0.5)/2 * height, height/2, fill="red3")
        (cx, cy, r) = ((3**0.5)/6 * height, height/2, 0.8 * heightofrec)
        canvas.create_oval(cx - r, cy - r, cx + r, cy + r, fill="white")


### Note that drawThreadPattern is COLLABORATIVE ###
def drawThreadPatternCollaborators():
    return "nobody"


def drawThreadPattern(canvas, size, numSpokes, startSpoke, numSkips):
    import math
    (cx, cy, r) = (size/2, size/2, size/2 * 0.9)
    # draw a large circle
    canvas.create_oval(cx - r, cy - r, cx + r, cy + r, outline='black', width=r/30)
    # draw small circles
    for i in range(numSpokes):
        iAngle = math.pi / 2 - (2 * math.pi) * (i / numSpokes) - math.pi
        ix = cx + r * math.cos(iAngle)
        iy = cy - r * math.sin(iAngle)
        # ixt = cx + 0.85 * r * math.cos(iAngle)
        # iyt = cy - 0.85 * r * math.sin(iAngle)
        # canvas.create_text(ixt, iyt, text= str(i), font="Arial 16 bold", width=10)
        if i == startSpoke:
            canvas.create_oval(ix - (r/20)*1.2, iy - (r/20)*1.1, ix + (r/20)*1.1, iy + (r/20) * 1.1,
                           fill='green', outline='black', width=1)
        else:
            canvas.create_oval(ix - (r / 20) * 1.2, iy - (r / 20) * 1.1, ix + (r / 20) * 1.1, iy + (r / 20) * 1.1,
                               fill='red', outline='black', width=1)
    # draw threads
    for n in range(numSpokes):
        if n == startSpoke:
            begin = True
            fixAngle = math.pi / 2 - (2 * math.pi) * (n / numSpokes) - math.pi
            xfix = cx + 0.95 * r * math.cos(fixAngle)
            yfix = cy - 0.95 * r * math.sin(fixAngle)
            nAngle = math.pi / 2 - (2 * math.pi) * (n / numSpokes) - math.pi
            nxold, nyold = xfix, yfix
            while begin:
                nAnglenew = nAngle - (2 * math.pi) * (numSkips/numSpokes)
                nxnew = cx + 0.95 * r * math.cos(nAnglenew)
                nynew = cy - 0.95 * r * math.sin(nAnglenew)
                canvas.create_line(nxold, nyold, nxnew, nynew, width=1)
                nAngle = nAnglenew
                if abs(nxnew - xfix) < 0.0001 and abs(nynew - yfix) < 0.0001:
                    break
                nxold, nyold = nxnew, nynew


### Note that drawSteelersLogo is SOLO ###
def drawSteelersLogo(canvas, x, y, r):
    sizeOfFont = int(r/4.3)
    (cx, cy, r) = (x, y, 0.95 * r)
    canvas.create_oval(cx - r, cy - r, cx + r, cy + r, fill="white", outline="gray", width=r/10)
    # define the centers of diamonds
    (goldx, goldy) = (cx, cy - r / 2)
    (bluex, bluey) = (cx, cy + r / 2)
    (redx, redy) = (cx + r / 2, cy)
    canvas.create_polygon(goldx, goldy + 0.8 * r/2, goldx + 0.8 * r/2, goldy,
                          goldx, goldy - 0.8 * r/2, goldx - 0.8 * r/2, goldy, fill="gold")
    canvas.create_polygon(bluex, bluey - 0.8 * r/2, bluex + 0.8 * r/2, bluey,
                          bluex, bluey + 0.8 * r/2, bluex - 0.8 * r/2, bluey, fill="blue")
    canvas.create_polygon(redx - 0.8 * r/2, redy, redx, redy - 0.8 * r/2,
                          redx + 0.8 * r/2, redy, redx, redy + 0.8 * r/2, fill="red")
    canvas.create_text(cx, cy, text="Steelers",
                       fill="black", font=('Times', sizeOfFont, 'bold'), anchor="e")


### Note that drawButtonPattern is SOLO ###
def drawCircle(canvas, x0, y0, x1, y1, r, color):
    (cx, cy, r) = (x0 + (x1 - x0)/2, y0 + (y1 - y0)/2, r)
    while r >= 1:
        canvas.create_oval(cx - r, cy - r, cx + r, cy + r, fill=color, outline='black')
        r = (2/3) * r


def drawButtonPattern(canvas, size, n):
    canvas.create_rectangle(0, 0, size, size, fill="purple")
    width = size / n
    r = width / 2
    for col in range(n):
        for row in range(n):
            # print('col',col,'row', row)
            left = 0 + width * col
            top = 0 + width * row
            right = width * (col + 1)
            bottom = width * (row + 1)
            if (col + row) % 4 == 0:
                color = 'red'
                drawCircle(canvas, left, top, right, bottom, r, color)
            if row % 3 == 0:
                if (col + row) % 4 != 0:
                    color = 'green'
                    drawCircle(canvas, left, top, right, bottom, r, color)
            if col % 2 == 1:
                if ((row - 1) % 12) == 0 or ((row - 5) % 12 == 0):
                    if (col - 1) % 4 == 0:
                        color = 'yellow'
                        drawCircle(canvas, left, top, right, bottom, r, color)

                if ((row - 7) % 12) == 0 or ((row - 11) % 12 == 0):
                    if (col - 3) % 4 == 0:
                        color = 'yellow'
                        drawCircle(canvas, left, top, right, bottom, r, color)

                if ((row - 2) % 6 == 0) or ((row - 4) % 6 == 0):
                    if col % 2 == 1:
                        color = 'yellow'
                        drawCircle(canvas, left, top, right, bottom, r, color)
            if (row - 1) % 6 == 0 or (row - 5) % 6 == 0:
                if col % 2 == 0:
                    color = 'blue'
                    drawCircle(canvas, left, top, right, bottom, r, color)
            if (row - 2) % 12 == 0 or (row - 10) % 12 == 0:
                if (col - 4) % 4 == 0:
                    color = 'blue'
                    drawCircle(canvas, left, top, right, bottom, r, color)
            if (row - 4) % 12 == 0 or (row - 8) % 12 == 0:
                if (col - 2) % 4 == 0:
                    color = 'blue'
                    drawCircle(canvas, left, top, right, bottom, r, color)



#### Note that drawNiceRobot is BONUS, and therefore optional ####
def drawNiceRobot(canvas, width, height):
    pass

#################################################
# Hw2 Test Functions
# ignore_rest
#################################################

def testIsSmithNumber():
    print("Testing isSmithNumber()...", end="")
    assert(isSmithNumber(22) == True)
    assert(isSmithNumber(21) == False)
    assert(isSmithNumber(4) == True)
    assert(isSmithNumber(378) == True)
    assert(isSmithNumber(1) == False)
    assert(isSmithNumber(27) == True)
    assert(isSmithNumber(9) == False)
    assert(isSmithNumber(7) == False)
    print("Passed.")

def runDrawFlagOfCuba(width, height):
    root = Tk()
    root.resizable(width=False, height=False) # prevents resizing window
    canvas = Canvas(root, width=width, height=height)
    canvas.configure(bd=0, highlightthickness=0)
    canvas.pack()
    # width must equal height
    assert(width == 2*height)
    drawFlagOfCuba(canvas, width, height)
    root.mainloop()

def testDrawFlagOfCuba():
    print("Testing drawFlagOfCuba()...", end="")
    runDrawFlagOfCuba(580, 290)
    runDrawFlagOfCuba(100, 50)
    runDrawFlagOfCuba(300, 150)
    print("Done.")

def testIsMultiPowerfulNumber():
    print("Testing isMultiPowerfulNumber()...", end="")
    isMultiPowerfulNumber(36)
    isMultiPowerfulNumber(72)
    isMultiPowerfulNumber(100)
    isMultiPowerfulNumber(108)
    #print("NO TEST CASES YET! Write them yourself!")
    print("Passed.")

def runDrawThreadPattern(width, height, numSpokes, startSpoke, numSkips):
    root = Tk()
    root.resizable(width=False, height=False) # prevents resizing window
    canvas = Canvas(root, width=width, height=height)
    canvas.configure(bd=0, highlightthickness=0)
    canvas.pack()
    # width must equal height
    assert(width == height)
    drawThreadPattern(canvas, width, numSpokes, startSpoke, numSkips)
    root.mainloop()

def testDrawThreadPattern():
    print("Testing drawThreadPattern...", end="")
    runDrawThreadPattern(400, 400, 12, 0, 5)
    runDrawThreadPattern(200, 200, 10, 3, 4)
    runDrawThreadPattern(500, 500, 19, 8, 15)
    print("Done.")

def runDrawSteelersLogo(width, height, x, y, r):
    root = Tk()
    root.resizable(width=False, height=False) # prevents resizing window
    canvas = Canvas(root, width=width, height=height)
    canvas.configure(bd=0, highlightthickness=0)
    canvas.pack()
    drawSteelersLogo(canvas, x, y, r)
    root.mainloop()

def testDrawSteelersLogo():
    print("Testing drawSteelersLogo...", end="")
    runDrawSteelersLogo(300, 300, 150, 150, 100)
    runDrawSteelersLogo(500, 600, 300, 200, 200)
    runDrawSteelersLogo(150, 100, 50, 60, 40)
    print("Done.")

def testIsKaprekarNumber():
    print("Testing isKaprekarNumber()...", end="")
    assert(isKaprekarNumber(0) == False)
    assert(isKaprekarNumber(1) == True)
    assert(isKaprekarNumber(4) == False)
    assert(isKaprekarNumber(9) == True)
    assert(isKaprekarNumber(36) == False)
    assert(isKaprekarNumber(45) == True)
    assert(isKaprekarNumber(450) == False)
    print("Passed.")

def testNthKaprekarNumber():
    print("Testing nthKaprekarNumber()...", end="")
    assert(nthKaprekarNumber(0) == 1)
    assert(nthKaprekarNumber(1) == 9)
    assert(nthKaprekarNumber(2) == 45)
    assert(nthKaprekarNumber(3) == 55)
    assert(nthKaprekarNumber(4) == 99)
    assert(nthKaprekarNumber(5) == 297)
    assert(nthKaprekarNumber(6) == 703)
    assert(nthKaprekarNumber(7) == 999)
    print('Passed.')

def testNearestKaprekarNumber():
    print("Testing nearestKaprekarNumber()...", end="")
    assert(nearestKaprekarNumber(1) == 1)
    assert(nearestKaprekarNumber(0) == 1)
    assert(nearestKaprekarNumber(-1) == 1)
    assert(nearestKaprekarNumber(-2) == 1)
    assert(nearestKaprekarNumber(-12345) == 1)
    assert(nearestKaprekarNumber(1.234) == 1)
    assert(nearestKaprekarNumber(4.99999999) == 1)
    assert(nearestKaprekarNumber(5) == 1)
    assert(nearestKaprekarNumber(5.00000001) == 9)
    assert(nearestKaprekarNumber(27) == 9)
    assert(nearestKaprekarNumber(28) == 45)
    assert(nearestKaprekarNumber(45) == 45)
    assert(nearestKaprekarNumber(50) == 45)
    assert(nearestKaprekarNumber(51) == 55)
    assert(nearestKaprekarNumber(1611) == 999)
    assert(nearestKaprekarNumber(1612) == 2223)
    assert(nearestKaprekarNumber(2475.4) == 2223)
    assert(nearestKaprekarNumber(2475.5) == 2223)
    assert(nearestKaprekarNumber(2475.51) == 2728)
    assert(nearestKaprekarNumber(2475.6) == 2728)
    assert(nearestKaprekarNumber(995123) == 994708)
    assert(nearestKaprekarNumber(9376543) == 9372385)
    assert(nearestKaprekarNumber(13641234) == 13641364)
    print("Passed.")

def runDrawButtonPattern(width, height, n):
    root = Tk()
    root.resizable(width=False, height=False) # prevents resizing window
    canvas = Canvas(root, width=width, height=height)
    canvas.configure(bd=0, highlightthickness=0)
    canvas.pack()
    # width must equal height
    assert(width == height)
    drawButtonPattern(canvas, width, n)
    root.mainloop()

def testDrawButtonPattern():
    print("Testing drawButtonPattern()...", end="")
    runDrawButtonPattern(400, 400, 10)
    runDrawButtonPattern(300, 300, 5)
    runDrawButtonPattern(250, 250, 25)
    print("Done.")

def runDrawNiceRobot(width, height):
    root = Tk()
    root.resizable(width=False, height=False) # prevents resizing window
    canvas = Canvas(root, width=width, height=height)
    canvas.configure(bd=0, highlightthickness=0)
    canvas.pack()
    drawNiceRobot(canvas, width, height)
    root.mainloop()

def testDrawNiceRobot():
    print("Testing drawNiceRobot()...", end="")
    runDrawNiceRobot(500, 500)
    runDrawNiceRobot(250, 250)
    print("Done.")

def testSquaresGenerator():
    print("Testing squaresGenerator()...", end="")
    g = squaresGenerator()
    assert(next(g) == 1)
    assert(next(g) == 4)
    assert(next(g) == 9)
    assert(next(g) == 16)

    # ok, now with a for loop.
    squares = ""
    for square in squaresGenerator():
        if (squares != ""): squares += ", "
        squares += str(square)
        if (square >= 100): break
    assert(squares == "1, 4, 9, 16, 25, 36, 49, 64, 81, 100")
    print("Passed.")

def testNswGenerator():
    print("Testing nswGenerator()...", end="")
    nswNumbers = ""
    for nswNumber in nswGenerator():
        if (nswNumbers != ""): nswNumbers += ", "
        nswNumbers += str(nswNumber)
        if (nswNumber >= 152139002499): break
    # from: http://oeis.org/A001333
    assert(nswNumbers == "1, 1, 3, 7, 17, 41, 99, 239, 577, 1393, 3363, 8119, "
                         "19601, 47321, 114243, 275807, 665857, 1607521, 3880899, "
                         "9369319, 22619537, 54608393, 131836323, 318281039, "
                         "768398401, 1855077841, 4478554083, 10812186007, "
                         "26102926097, 63018038201, 152139002499"
          )
    print("Passed.")

def testNswPrimesGenerator():
    print("Testing nswPrimesGenerator()...", end="")
    nswPrimes = ""
    for nswPrime in nswPrimesGenerator():
        if (nswPrimes != ""): nswPrimes += ", "
        nswPrimes += str(nswPrime)
        if (nswPrime >= 63018038201): break
    # from: http://oeis.org/A088165
    assert(nswPrimes == "7, 41, 239, 9369319, 63018038201")
    print("Passed.")

#################################################
# Hw2 Main
#################################################

def testAll():
    ### Lab problems ###
    testIsSmithNumber()
    testDrawFlagOfCuba()
    ### Collaborative problems ###

    testIsMultiPowerfulNumber()
    testDrawThreadPattern()

    ### Solo problems ###
    testDrawSteelersLogo()
    testIsKaprekarNumber()
    testNthKaprekarNumber()
    testNearestKaprekarNumber()
    testDrawButtonPattern()

    # Uncomment the next lines if you want to try the bonus!
    #testDrawNiceRobot()
    #testSquaresGenerator()
    #testNswGenerator()
    #testNswPrimesGenerator()

def main():
    cs112_s19_week2_linter.lint() # check for banned tokens
    testAll()

if __name__ == '__main__':
    main()