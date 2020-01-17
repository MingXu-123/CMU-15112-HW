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
    return "mdtaylor, krivers, acarnegie"

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
def distanceCollaborators():
    return "nobody"

def distance(x1, y1, x2, y2):
    return
    
#### isRightTriangle is a COLLABORATIVE problem ####
# Modify the output of isRightTriangleCollaborators to return the andrewIDs
#     of your collaborators as a string.  Separate each with a comma.
def isRightTriangleCollaborators():
    return "nobody"
    
def isRightTriangle(x1, y1, x2, y2, x3, y3):
    return

#### roundPegRectangularHole and rectangularPegRoundHole are COLLABORATIVE ####
# Modify the output of pegProblemCollaborators to return the andrewIDs
#     of your collaborators as a string.  Separate each with a comma.
def pegProblemCollaborators():
    return "nobody"
    
def roundPegRectangularHole(r, w, h):
    return
    
def rectangularPegRoundHole(r, w, h):
    return
    
    
    
    
    
    
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
       
def nearestOdd(n):
    return

#### colorBlender is a COLLABORATIVE problem ####
# Modify the output of colorBlenderCollaborators to return the andrewIDs
#     of your collaborators as a string.  Separate each with a comma.
def colorBlenderCollaborators():
    return "nobody"
    
def colorBlender(rgb1, rgb2, midpoints, n):
    return






#################################################
# Hw1 SOLO problems
#################################################
# These problems must be completed WITHOUT COLLABORATION.  See the collaboration
#     policy in the syllabus for more details.  You may always use piazza, 
#     office hours, and other official 15-112 course resources for questions.

def syllabusAnswer():
    return """
1:
2:
3:
4:
5: 
"""

def debuggingAnswer():
    return "Your answer here"

def rocAnswer():
    return


#### the following three functions go together ####
# Note: You'll need to use distance(x1,y1,x2,y2) as a helper function!
# Wait to do this problem until after you write distance in Friday's lab

def lineIntersection(m1, b1, m2, b2):
    return 

def triangleArea(s1, s2, s3):
    return

def threeLinesArea(m1, b1, m2, b2, m3, b3):
    return

#### the following two functions go together ####

def getKthDigit(n, k):
    return

def setKthDigit(n, k, d):
    return


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