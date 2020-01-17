###############################################################################
# ---------------- 15-112 Recitation Week 1: Getting Started ---------------- #

# This is a starter file of the problems we did in recitation. A good way to
# use this file is to try to re-write problems you saw in recitation from
# scratch. This way, you can test your understanding and ask on Piazza or
# office hours if you have questions :)

# --------------------------------------------------------------------------- #
###############################################################################
# Functions
###############################################################################

# write a function that returns n times 5
def timesFive(n):
    return 5 * n

# write a function that returns n multiplied by m
def mult(n, m):
    return n * m

# write a function that returns n raised to the p power
def pow(n,p):
    return n ** p

# write a function that returns the 100s value of n
def returnHundredsValue(n):
    return (n // 100) % 10


# write a function that calculates the slope of a line given two points
def slope(x1, y1, x2, y2):
    return (y2 - y1) / (x2 - x1)

###############################################################################
# Code Tracing
###############################################################################

def ct(x):
   x -= 1
   print(x**2)
   x %= 4
   return ((x * 2) % 4) // 2

print(ct(6))
print("Hello World")

###############################################################################
# Reasoning Over Code
###############################################################################

def rc(n):
    assert(type(n) == int)
    if ((n < 0) or (n > 99)): return False
    d1 = n % 10 #onesdigit
    d2 = n // 10  #tensdigit
    m = 10 * d1 + d2
    return ((m < n) and (n < 12))


print(rc(234))


