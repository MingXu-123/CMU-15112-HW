###############################################################################
# --------------- 15-112 Recitation Week 2: Loops & Graphics ---------------- #

# This is a starter file of the problems we did in recitation. A good way to
# use this file is to try to re-write problems you saw in recitation from
# scratch. This way, you can test your understanding and ask on Piazza or
# office hours if you have questions :)

# --------------------------------------------------------------------------- #
###############################################################################
# Code Tracing
###############################################################################

def ct2(n):
    k = 0
    total = 0
    while (n >= k):
        print('k =', k)
        for i in range(k):
            total += n%10
            n //= 10
            print(i, n%10, total)
        k += 1 
    print('total =', total)
    return k

# print(ct2(123))

###############################################################################
# Code Tracing
###############################################################################

'''
Write the function longestDigitRun(n) that takes a possibly-negative int value n
and returns the digit that has the longest consecutive run (ignoring ties).
So,longestDigitRun(117773732) returns 7 (because there is a run of 3 consecutive
7's), and longestDigitRun(-677886) can return either 7 or 8 because both have
runs of length two.
'''

def longestDigitRun(n):
    return 42


def testLongestDigitRun():
    assert(longestDigitRun(117773732) == 7)
    result = longestDigitRun(-677886)
    assert(result == 7 or result == 8)
    # TODO: add more test cases here!

###############################################################################
# Draw American Flag
###############################################################################

from tkinter import *

def drawAmericanFlag(canvas, width, height):
    pass

def runDrawing(width=300, height=300):
    root = Tk()
    root.resizable(width=False, height=False) # prevents resizing window
    canvas = Canvas(root, width=width, height=height)
    canvas.configure(bd=0, highlightthickness=0)
    canvas.pack()
    drawAmericanFlag(canvas, width, height)
    root.mainloop()
    print("bye!")

# runDrawing(350, 200)