#################################################
# Hw5
# Your andrewID:mxu2
# Your section: 2N
#################################################


import copy

#################################################
# Hw5 COLLABORATIVE problems
#################################################
# The problem in this section is COLLABORATIVE, which means you may
#     work on it with your classmates if you wish.  See the collaboration
#     policy in the syllabus for more details.  Always list your collaborators!

def collaborator():
    return "xiaoqint"

# find the position of each num in board
def findPositionOfNum(num, board):
    rows = len(board)
    cols = rows
    rowOfNum = 0
    colOfNum = 0
    for row in range(rows):
        for col in range(cols):
            if board[row][col] == num:
                rowOfNum = row
                colOfNum = col
    return rowOfNum, colOfNum

# check whether one of the num in board has next step
def hasNextStep(num, nextNum, board):
    numRow, numCol = findPositionOfNum(num, board)
    nextNumRow, nextNumCol = findPositionOfNum(nextNum, board)
    if (nextNumRow - numRow) * (nextNumCol - numCol) == 2 or\
            (nextNumRow - numRow) * (nextNumCol - numCol) == -2:
        return True
    else:
        return False

# return True if board is a Knights Tour and return False otherwise
def isKnightsTour(board):
    if board == [[0]]:
        return False
    rows = len(board)
    cols = rows
    compareList = [i for i in range(1, cols ** 2 + 1)]
    tourList = []
    for row in range(rows):
        for col in range(cols):
            tourList.append(board[row][col])
    tourList.sort()
    # check whether tourList meet the requirement of Knights tour
    if compareList != tourList:
        return False
    finalNum = rows * cols
    knightsTour = True
    for num in range(1, finalNum):
        nextNum = num + 1
        if hasNextStep(num, nextNum, board):
            knightsTour = True
            continue
        else:
            knightsTour = False
            break
    return knightsTour


# this is the non destructive function to remove
# rows and cols in a list
def nondestructiveRemoveRowAndCol(lst, row, col):
    newLst = copy.deepcopy(lst)
    newLst = newLst[:row] + newLst[row+1:]
    result = []
    for i in range(len(newLst)):
        result += [newLst[i][:col] + newLst[i][col+1:]]
    return result


# this is the destructive function to remove
# rows and cols in a list
def destructiveRemoveRowAndCol(lst, row, col):
    lst.pop(row)
    for i in range(len(lst)):
        lst[i].pop(col)

#################################################
# Hw5 Test Functions
#################################################
def testnondestructiveRemoveRowAndCol():
    print("Testing nondestructiveRemoveRowAndCol()...", end="")
    lst = [[2, 3, 4, 5],
           [8, 7, 6, 5],
           [0, 1, 2, 3]]
    result = [[2, 3, 5],
              [0, 1, 3]]
    # Copy the input list so we can check it later
    lstCopy = copy.deepcopy(lst)
    # The first assert is an ordinary test; the second is a non-destructive test
    assert (nondestructiveRemoveRowAndCol(lst, 1, 2) == result)
    assert (lst == lstCopy), "input list should not be changed"
    print("passed.")


def testdestructiveRemoveRowAndCol():
    print("Testing destructiveRemoveRowAndCol()...", end="")
    lst = [[2, 3, 4, 5],
           [8, 7, 6, 5],
           [0, 1, 2, 3]]
    result = [[2, 3, 5],
              [0, 1, 3]]
    # Copy the input list so we can check it later
    lstCopy = copy.deepcopy(lst)
    # The first assert is an ordinary test; the second is a destructive test
    assert (destructiveRemoveRowAndCol(lst, 1, 2) == None)
    assert (lst == result)
    assert (lst != lstCopy), "input list should be changed"
    print("passed.")


def testisKnightsTour():
    print("Testing isKnightsTour()...", end="")
    board = [[1, 60, 39, 34, 31, 18, 9, 64],

             [38, 35, 32, 61, 10, 63, 30, 17],

             [59, 2, 37, 40, 33, 28, 19, 8],

             [36, 49, 42, 27, 62, 11, 16, 29],

             [43, 58, 3, 50, 41, 24, 7, 20],

             [48, 51, 46, 55, 26, 21, 12, 15],

             [57, 44, 53, 4, 23, 14, 25, 6],

             [52, 47, 56, 45, 54, 5, 22, 13],

             ]
    assert (isKnightsTour(board) == True)
    board1 = [[1, 60, 39, 34, 31, 18, 9, 64],

             [38, 35, 32, 61, 10, 63, 30, 17],

             [59, 2, 37, 40, 33, 28, 19, 8],

             [36, 49, 42, 27, 62, 11, 16, 29],

             [43, 58, 3, 50, 41, 24, 7, 20],

             [48, 51, 46, 55, 26, 21, 12, 15],

             [57, 44, 53, 4, 23, 14, 25, 6],

             [52, 47, 56, 45, 54, 5, 22, 1],

             ]
    assert (isKnightsTour(board1) == False)
    board2 = [[1, 60, 39, 34, 31, 18, 9, 64],

              [38, 35, 32, 61, 10, 63, 30, 17],

              [59, 2, 37, 40, 33, 28, 19, 8],

              [36, 49, 42, 27, 62, 11, 16, 29],

              [43, 58, 3, 50, 41, 24, 7, 20],

              [48, 51, 46, 55, 26, 21, 12, 15],

              [57, 44, 53, 4, 23, 14, 25, 6],

              [52, 47, 56, 45, 54, 5, 22, 13],

              ]
    assert (isKnightsTour(board2) == True)
    board3 = [[1, 60, 39, 34, 31, 18, 9, 64],

              [38, 35, 32, 61, 10, 63, 30, 17],

              [59, 2, 37, 40, 33, 28, 19, 8],

              [36, 49, 27, 42, 62, 11, 16, 29],

              [43, 58, 3, 50, 41, 24, 7, 20],

              [48, 51, 46, 55, 26, 21, 12, 15],

              [57, 44, 53, 4, 23, 14, 25, 6],

              [52, 47, 56, 45, 54, 5, 22, 13],

              ]
    assert (isKnightsTour(board3) == False)
    board4 = [[0, 59, 38, 33, 30, 17, 8,  63],

              [37, 34, 31, 60, 9, 62, 29, 16],

              [58, 1, 36, 39, 32, 27, 18, 7],

              [35, 48, 41, 26, 61, 10, 15, 28],

              [42, 57, 2, 49, 40, 23, 6, 19],

              [47, 50, 45, 54, 25, 20, 11, 14],

              [56, 43, 52, 3, 22, 13, 24, 5],

              [51, 46, 55, 44, 53, 4, 21, 12],
             ]
    assert (isKnightsTour(board4) == False)
    board5 = [[3, 6, 1],
              [8, 9, 4],
              [5, 2, 7],
             ]
    assert (isKnightsTour(board5) == False)
    board6 = [[19, 14, 3, 8, 25],
              [4, 9, 18, 13, 2],
              [15, 20, 1, 24, 7],
              [10, 5, 22, 17, 12],
              [21, 16, 11, 6, 23]
             ]
    assert (isKnightsTour(board6) == True)
    print("passed.")

# This is the test All function
def testAll():
    testisKnightsTour()
    testnondestructiveRemoveRowAndCol()
    testdestructiveRemoveRowAndCol()

