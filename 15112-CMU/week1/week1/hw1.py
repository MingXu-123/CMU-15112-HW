#################################################
# Hw1
# Your andrewID:mxu2
# Your section: 2 N
#################################################

import cs112_s19_week1_linter

# For collaborative problems, you must list your collaborators!
# Each collaborative problem has a function which you should modify to 
# return a comma-separated string with the andrewIDs of your collaborators.
# Here is an example which you should not modify!
def exampleCollaborators():
    return "yiqizhou, afu1, justinau"

#################################################
# Lab1 COLLABORATIVE LAB problems 
# (Their problem descriptions will be released Friday, Jan 18)
#################################################
# The problems in this section are LAB PROBLEMS, which means you MUST
#     work on these with at least one collaborator.  See the collaboration
#     policy in the syllabus for more details.  Always list your collaborators!
#     For lab problems, YOU MUST LIST AT LEAST ONE COLLABORATOR


#### distance is a COLLABORATIVE problem ####
# Modify the output of distanceCollaborators to return the andrewIDs
#     of your collaborators as a string.  Separate each with a comma.

import math # import math module

def distanceCollaborators():
    return "afu1"

def distance(x1, y1, x2, y2):
    return math.sqrt((x1 - x2)**2 + (y1 - y2)**2)
    
#### isRightTriangle is a COLLABORATIVE problem ####
# Modify the output of isRightTriangleCollaborators to return the andrewIDs
#     of your collaborators as a string.  Separate each with a comma.
def isRightTriangleCollaborators():
    return "yiqizhou"

# The following helper function is from lecture notes
def almostEqual(x, y):
    return abs(x - y) < 10**-9


def isRightTriangle(x1, y1, x2, y2, x3, y3):
    return almostEqual(distance(x1,y1,x2,y2)**2 + distance(x2,y2,x3,y3)**2, distance(x1,y1,x3,y3)**2)\
           or almostEqual(distance(x1,y1,x3,y3)**2 + distance(x2,y2,x3,y3)**2, distance(x1,y1,x2,y2)**2)\
           or almostEqual(distance(x1,y1,x3,y3)**2 + distance(x2,y2,x1,y1)**2, distance(x2,y2,x3,y3)**2)


#### roundPegRectangularHole and rectangularPegRoundHole are COLLABORATIVE ####
# Modify the output of pegProblemCollaborators to return the andrewIDs
#     of your collaborators as a string.  Separate each with a comma.
def pegProblemCollaborators():
    return "justinau"
    
def roundPegRectangularHole(r, w, h):
    minsideofrec = min(w, h)
    if 2 * r <= minsideofrec:
        return True
    else:
        return False
    
def rectangularPegRoundHole(r, w, h):
    #halfdiag = ((w/2)**2 + (h/2)**2)**0.5
    halfdiag = (w ** 2 + h ** 2) ** 0.5 * 0.5
    if halfdiag <= r:
        return True
    else:
        return False

    
#################################################
# Hw1 COLLABORATIVE problem
#################################################
# The problems in this section are COLLABORATIVE, which means you may
#     work on them with your classmates if you wish.  See the collaboration
#     policy in the syllabus for more details.  Always list your collaborators!
    
#### nearestOdd is a COLLABORATIVE problem ####
# Modify the output of nearestOddCollaborators to return the andrewIDs
#     of your collaborators as a string.  Separate each with a comma.
def nearestOddCollaborators():
    return "nobody"


# The following function is from this week's lecture notes
def roundHalfUp(d):
    # Round to nearest with ties going away from zero.
    # You do not need to understand how this function works.
    import decimal
    rounding = decimal.ROUND_HALF_UP
    return int(decimal.Decimal(d).to_integral_value(rounding=rounding))


def nearestOdd(n):
    if type(n) == int:
        if n % 2 == 1:
            return n
        else:
            return n - 1
    elif type(n) == float:
        if n < 0:
            n = abs(n)
            if roundHalfUp(n) % 2 == 1:
                return roundHalfUp(n) * -1
            elif roundHalfUp(n) % 2 == 0:
                if abs(roundHalfUp(n) + 1 - n) < abs(n - (roundHalfUp(n) - 1)):
                    return (roundHalfUp(n) + 1) * -1
                elif abs(roundHalfUp(n) + 1 - n) == abs(n - (roundHalfUp(n) - 1)):
                    return (roundHalfUp(n) + 1) * -1
                elif abs(roundHalfUp(n) + 1 - n) > abs(n - (roundHalfUp(n) - 1)):
                    return (roundHalfUp(n) - 1) * -1
        elif n > 0:
            if roundHalfUp(n) % 2 == 1:
                return roundHalfUp(n)
            elif roundHalfUp(n) % 2 == 0:
                if abs(roundHalfUp(n) + 1 - n) < abs(n - (roundHalfUp(n) - 1)):
                    return roundHalfUp(n) + 1
                elif abs(roundHalfUp(n) + 1 - n) == abs(n - (roundHalfUp(n) - 1)):
                    return roundHalfUp(n) - 1
                elif abs(roundHalfUp(n) + 1 - n) > abs(n - (roundHalfUp(n) - 1)):
                    return roundHalfUp(n) - 1


#### colorBlender is a COLLABORATIVE problem ####
# Modify the output of colorBlenderCollaborators to return the andrewIDs
#     of your collaborators as a string.  Separate each with a comma.
def colorBlenderCollaborators():
    return "nobody"


def transformRGB(rgb1, rgb2, midpoints, n):
    blue1 = rgb1%10**3
    green1 = (rgb1//10**3)%(10**3)
    red1 = (rgb1//10**3)//10**3
    blue2 = rgb2%10**3
    green2 = (rgb2//10**3)%(10**3)
    red2 = (rgb2//10**3)//10**3
    equalblue = (blue1 - blue2)/(midpoints + 1)
    equalgreen = (green1 - green2)/(midpoints + 1)
    equalred = (red1 - red2)/(midpoints + 1)
    targetblue = roundHalfUp(blue1 - equalblue * n)
    targetgreen = roundHalfUp(green1 - equalgreen * n)
    targetred = roundHalfUp(red1 - equalred * n)
    targetred = str(targetred)
    if len(str(targetgreen)) == 1:
        targetgreen = "00" + str(targetgreen)
    elif len(str(targetgreen)) == 2:
        targetgreen = "0" + str(targetgreen)
    else:
        targetgreen = str(targetgreen)

    if len(str(targetblue)) == 1:
        targetblue = "00" + str(targetblue)
    elif len(str(targetblue)) == 2:
        targetblue = "0" + str(targetblue)
    else:
        targetblue = str(targetblue)

    return targetred + targetgreen + targetblue

def colorBlender(rgb1, rgb2, midpoints, n):
    if n < 0 or n > (midpoints + 1):
        return None
    elif 0 <= n <= (midpoints + 1):
        return int(transformRGB(rgb1, rgb2, midpoints, n))




#################################################
# Hw1 SOLO problems
#################################################
# These problems must be completed WITHOUT COLLABORATION.  See the collaboration
#     policy in the syllabus for more details.  You may always use piazza, 
#     office hours, and other official 15-112 course resources for questions.


def syllabusAnswer():
    return """
1: Family/Personal Emergencies
2: Students may only use electronic devices in lecture during learning activities which involve those devices
3: No I can not!
4: If I missing my laptop/phone on a specific lecture day, or if the form does not load for me,
 I may approach the instructors personally at the end of class to be marked as attending
5: I submit a 15-112 Regrade Request form on line within three weeks of the time that the contested grade was released.
"""


def debuggingAnswer():
    return "This is a logical error because if an even integer is greater than 10 such as 14, this function will return None" \
           "What I add to fix this problem is to add two lines of codes after the conditional if statement if x % 2 == 1: return True" \
           "add two lines of codes if x % 2 == 1: return True \ else: return False "


def rocAnswer():
    return 126


#### the following three functions go together ####
# Note: You'll need to use distance(x1,y1,x2,y2) as a helper function!
# Wait to do this problem until after you write distance in Friday's lab
def lineIntersection(m1, b1, m2, b2):
    if m1 == m2:
        return None
    else:
        return (b1 - b2)/(m2 - m1)


def triangleArea(s1, s2, s3):
    s = 0.5 * (s1 + s2 + s3)
    return math.sqrt(s * (s - s1) * (s - s2) * (s - s3))


def threeLinesArea(m1, b1, m2, b2, m3, b3):
    if m1 == m2 or m1 == m3 or m2 == m3 or m1 == m2 == m3:
        return 0
    else:
        x1 = lineIntersection(m1, b1, m2, b2)
        y1 = m1 * x1 + b1
        x2 = lineIntersection(m1, b1, m3, b3)
        y2 = m3 * x2 + b3
        x3 = lineIntersection(m2, b2, m3, b3)
        y3 = m2 * x3 + b2
        d1 = distance(x1, y1, x2, y2)
        d2 = distance(x1, y1, x3, y3)
        d3 = distance(x2, y2, x3, y3)
        return triangleArea(d1, d2, d3)


#### the following two functions go together ####

def getKthDigit(n, k):
    if n < 0:
        n = abs(n)
    if n == 0:
        return 0
    if k == 0:
        return n % 10
    elif n // (10 ** k) == 0:
        return n // 10 ** k
    else:
        return n // (10 ** k) % 10


def setKthDigit(n, k, d):
    if n < 0:
        n = abs(n)
        if k == 0:
            return ((n // 10) * 10 + d) * -1
        if n // 10 ** k == 0:
            return (10 ** k * d + n) * -1
        else:
            currentDigit = getKthDigit(n, k)
            return (n - currentDigit * (10 ** k) + d * (10 ** k)) * -1
    if k == 0:
        return (n // 10) * 10 + d
    if n // 10 ** k == 0:
        return 10 ** k * d + n
    else:
        currentDigit = getKthDigit(n, k)
        return n - currentDigit * (10 ** k) + d * (10 ** k)


#### bonusFindIntRootsOfCubic is a bonus problem, and therefore optional ####
# Note: Bonus problems are solo. Do not collaborate on bonus problems.    
    
def bonusFindIntRootsOfCubic(a, b, c, d):
    return






#################################################
# Hw1 Test Functions
# ignore_rest
#################################################

def testDistance():
    import math
    print("Testing distance()...", end="")
    assert(math.isclose(distance(0, 0, 1, 1), 2**0.5))
    assert(math.isclose(distance(3, 3, -3, -3), 6*2**0.5))
    assert(math.isclose(distance(20, 20, 23, 24), 5))
    print("Passed.")

def testIsRightTriangle():
    print('Testing isRightTriangle()... ', end='')
    assert(isRightTriangle(0, 0, 0, 3, 4, 0) == True)
    assert(isRightTriangle(1, 1.3, 1.4, 1, 1, 1) == True)
    assert(isRightTriangle(9, 9.12, 8.95, 9, 9, 9) == True)
    assert(isRightTriangle(0, 0, 0, math.pi, math.e, 0) == True)
    assert(isRightTriangle(0, 0, 1, 1, 2, 0) == True)
    assert(isRightTriangle(0, 0, 1, 2, 2, 0) == False)
    assert(isRightTriangle(1, 0, 0, 3, 4, 0) == False)
    print('Passed.')

    
def testRoundPegRectangularHole():
    print("Testing roundPegRectangularHole()...", end="")
    assert(roundPegRectangularHole(1,2,3)==True)
    assert(roundPegRectangularHole(4,5,6)==False)
    assert(roundPegRectangularHole(1,20,10)==True)
    assert(roundPegRectangularHole(10,2,30)==False)
    print("Passed.")
    
def testRectangularPegRoundHole():
    print("Testing rectangularPegRoundHole()...", end="")
    assert(rectangularPegRoundHole(1,2,3)==False)
    assert(rectangularPegRoundHole(5,4,6)==True)
    assert(rectangularPegRoundHole(2,4,4)==False)
    assert(rectangularPegRoundHole(5,8,6)==True)
    assert(rectangularPegRoundHole(6,10,8)==False)
    print("Passed.")
    
def testNearestOdd():
    print('Testing nearestOdd()... ', end='')
    assert(nearestOdd(13) == 13)
    assert(nearestOdd(12.001) == 13)
    assert(nearestOdd(12) == 11)
    assert(nearestOdd(11.999) == 11)
    assert(nearestOdd(-13) == -13)
    assert(nearestOdd(-12.001) == -13)
    assert(nearestOdd(-12) == -13)
    assert(nearestOdd(-11.999) == -11)
    print('Passed.')

def testColorBlender():
    print("Testing colorBlender()...", end="")
    # http://meyerweb.com/eric/tools/color-blend/#DC143C:BDFCC9:3:rgbd
    assert(colorBlender(220020060, 189252201, 3, -1) == None)
    assert(colorBlender(220020060, 189252201, 3, 0) == 220020060)
    assert(colorBlender(220020060, 189252201, 3, 1) == 212078095)
    assert(colorBlender(220020060, 189252201, 3, 2) == 205136131)
    assert(colorBlender(220020060, 189252201, 3, 3) == 197194166)
    assert(colorBlender(220020060, 189252201, 3, 4) == 189252201)
    assert(colorBlender(220020060, 189252201, 3, 5) == None)
    # http://meyerweb.com/eric/tools/color-blend/#0100FF:FF0280:2:rgbd
    assert(colorBlender(1000255, 255002128, 2, -1) == None)
    assert(colorBlender(1000255, 255002128, 2, 0) == 1000255)
    assert(colorBlender(1000255, 255002128, 2, 1) == 86001213)
    assert(colorBlender(1000255, 255002128, 2, 2) == 170001170)
    assert(colorBlender(1000255, 255002128, 2, 3) == 255002128)
    print("Passed.")

def testSyllabusAnswer():
    print("Your answer to the syllabus question is:")
    print(syllabusAnswer())
    print("The TAs will grade this later.")
    print()

def testDebuggingAnswer():
    print("Your answer to the debugging question is:")
    print(debuggingAnswer())
    print("The TAs will grade this later.")
    print()

def roc(x):
    if type(x) != int:
        return False
    elif x <= 120:
        return False
    elif x % 100 == x - 100:
        a = x // 10
        b = x % 10
        if a != 2 * b:
            return False
        return True
    else:
        return x == 42

def testRocAnswer():
    print("Testing rocAnswer()...", end="")
    answer = rocAnswer()
    assert(roc(answer) == True)
    print("Passed.")

def testLineIntersection():
    import math
    print("Testing lineIntersection()...", end="")
    assert(lineIntersection(2.5, 3, 2.5, 11) == None)
    assert(lineIntersection(25, 3, 25, 11) == None)
    # y=3x-5 and y=x+5 intersect at (5,10)
    assert(math.isclose(lineIntersection(3,-5,1,5), 5))
    # y=10x and y=-4x+35 intersect at (2.5,25)
    assert(math.isclose(lineIntersection(10,0,-4,35), 2.5))
    print("Passed.")

def testTriangleArea():
    import math
    print("Testing triangleArea()...", end="")
    assert(math.isclose(triangleArea(3,4,5), 6))
    assert(math.isclose(triangleArea(2**0.5, 1, 1), 0.5))
    assert(math.isclose(triangleArea(2**0.5, 2**0.5, 2), 1))
    print("Passed.")

def testThreeLinesArea():
    import math
    print("Testing threeLinesArea()...", end="")
    assert(math.isclose(threeLinesArea(1, 2, 3, 4, 5, 6), 0))
    assert(math.isclose(threeLinesArea(0, 7, 1, 0, -1, 2), 36))
    assert(math.isclose(threeLinesArea(0, 3, -.5, -5, 1, 3), 42.66666666666))
    assert(math.isclose(threeLinesArea(1, -5, 0, -2, 2, 2), 25))
    assert(math.isclose(threeLinesArea(0, -9.75, -6, 2.25, 1, -4.75), 21))
    print("Passed.")

def testGetKthDigit():
    print("Testing getKthDigit()...", end="")
    assert(getKthDigit(809, 0) == 9)
    assert(getKthDigit(809, 1) == 0)
    assert(getKthDigit(809, 2) == 8)
    assert(getKthDigit(809, 3) == 0)
    assert(getKthDigit(0, 100) == 0)
    assert(getKthDigit(-809, 0) == 9)
    print("Passed.")

def testSetKthDigit():
    print("Testing setKthDigit()...", end="")
    assert(setKthDigit(809, 0, 7) == 807)
    assert(setKthDigit(809, 1, 7) == 879)
    assert(setKthDigit(809, 2, 7) == 709)
    assert(setKthDigit(809, 3, 7) == 7809)
    assert(setKthDigit(0, 4, 7) == 70000)
    assert(setKthDigit(-809, 0, 7) == -807)
    print("Passed.")

def getCubicCoeffs(k, root1, root2, root3):
    # Given roots e,f,g and vertical scale k, we can find
    # the coefficients a,b,c,d as such:
    # k(x-e)(x-f)(x-g) =
    # k(x-e)(x^2 - (f+g)x + fg)
    # kx^3 - k(e+f+g)x^2 + k(ef+fg+eg)x - kefg
    e,f,g = root1, root2, root3
    return k, -k*(e+f+g), k*(e*f+f*g+e*g), -k*e*f*g

def testFindIntRootsOfCubicCase(k, z1, z2, z3):
    import math
    a,b,c,d = getCubicCoeffs(k, z1, z2, z3)
    result1, result2, result3 = bonusFindIntRootsOfCubic(a,b,c,d)
    m1 = min(z1, z2, z3)
    m3 = max(z1, z2, z3)
    m2 = (z1+z2+z3)-(m1+m3)
    actual = (m1, m2, m3)
    assert(math.isclose(m1, result1))
    assert(math.isclose(m2, result2))
    assert(math.isclose(m3, result3))

def testBonusFindIntRootsOfCubic():
    print("Testing bonusFindIntRootsOfCubic()...", end="")
    testFindIntRootsOfCubicCase(5, 1, 3,  2)
    testFindIntRootsOfCubicCase(2, 5, 33, 7)
    testFindIntRootsOfCubicCase(-18, 24, 3, -8)
    testFindIntRootsOfCubicCase(1, 2, 3, 4)
    print("Passed.")

#################################################
# Hw1 Main
#################################################

def testAll():
    testDistance()
    testIsRightTriangle()
    testRoundPegRectangularHole()
    testRectangularPegRoundHole()
    testNearestOdd()
    testColorBlender()
    testSyllabusAnswer()
    testDebuggingAnswer()
    testRocAnswer()
    testLineIntersection()
    testTriangleArea()
    testThreeLinesArea()
    testGetKthDigit()
    testSetKthDigit()


    
    #Uncomment the next line if you want to try the bonus!
    #testBonusFindIntRootsOfCubic() 

def main():
    cs112_s19_week1_linter.lint() # check for banned tokens
    testAll()

if __name__ == '__main__':
    main()



    