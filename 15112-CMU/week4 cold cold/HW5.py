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
    return "nobody"

def findRowAndColOf1(board):
    n = len(board)
    rows = n
    cols = rows
    rowOf1 = 0
    colOf1 = 0
    for row in range(rows):
        for col in range(cols):
            if board[row][col] == 1:
                rowOf1 = row
                colOf1 = col
    print(rowOf1, colOf1)
    return rowOf1, colOf1

def getNextSteps(firstStep):
    nextSteps = [(firstStep[0] + 2, firstStep[1] + 1),
                 (firstStep[0] + 2, firstStep[1] - 1),
                 (firstStep[0] + 1, firstStep[1] + 2),
                 (firstStep[0] + 1, firstStep[1] - 2),
                 (firstStep[0] - 1, firstStep[1] + 2),
                 (firstStep[0] - 1, firstStep[1] - 2),
                 (firstStep[0] - 2, firstStep[1] + 1),
                 (firstStep[0] - 2, firstStep[1] - 1)
                 ]
    return nextSteps


def CheckNextStep(startPosition, board):
    counter = 1
    n = len(board)
    firstStep = [startPosition[0], startPosition[1]]
    nextSteps = getNextSteps(firstStep)
    isKnightsTour = True
    while counter < n**2:
        i = 0
        while i < len(nextSteps):
            if 0 <= nextSteps[i][0] <= n - 1 and 0 <= nextSteps[i][1] <= n - 1:
                if board[nextSteps[i][0]][nextSteps[i][1]] == counter + 1:
                    counter += 1
                    firstStep = [nextSteps[i][0], nextSteps[i][1]]
                    nextSteps = getNextSteps(firstStep)
                    i = 0
                elif board[nextSteps[i][0]][nextSteps[i][1]] != counter + 1:
                    i += 1
                    if i >= 8:
                        return False
                    else:
                        continue
            else:
                i += 1
    return isKnightsTour



def isKnightsTour(board):
    n = len(board)
    rows = n
    cols = rows
    compareList = [i for i in range(1, n**2 + 1)]
    tourList = []
    for row in range(rows):
        for col in range(cols):
            tourList.append(board[row][col])
    tourList.sort()
    if compareList != tourList:
        return False
    else:
        rowOf1, colOf1 = findRowAndColOf1(board)
        startPosition = [rowOf1, colOf1]
        isKnightsTour = CheckNextStep(startPosition, board)
        return isKnightsTour




def testisKnightsTour():
    print("Testing nondestructiveRemoveRepeats()...", end="")
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

    print("passed.")

board = [    [1, 60, 39, 34, 31, 18, 9, 64],

             [38, 35, 32, 61, 10, 63, 30, 17],

             [59, 2, 37, 40, 33, 28, 19, 8],

             [36, 49, 42, 27, 62, 11, 16, 29],

             [43, 58, 3, 50, 41, 24, 7, 20],

             [48, 51, 46, 55, 26, 12, 21, 15],

             [57, 44, 53, 4, 23, 14, 25, 6],

             [52, 47, 56, 45, 54, 5, 22, 13],

         ]

board2 = [[1, 60, 39, 34, 31, 18, 9, 64],

             [38, 35, 32, 61, 10, 63, 30, 17],

             [59, 2, 37, 40, 33, 28, 19, 8],

             [36, 49, 42, 27, 62, 11, 16, 29],

             [43, 58, 3, 50, 41, 24, 7, 20],

             [48, 51, 46, 55, 26, 21, 12, 15],

             [57, 44, 53, 4, 23, 14, 25, 6],

             [52, 47, 56, 45, 54, 5, 22, 13],

            ]

board3 = [[1, 60, 39, 34, 31, 18, 9, 64],

             [38, 35, 32, 61, 10, 63, 30, 17],

             [59, 2, 37, 40, 33, 28, 19, 8],

             [36, 49, 27, 42, 62, 11, 16, 29],

             [43, 58, 3, 50, 41, 24, 7, 20],

             [48, 51, 46, 55, 26, 21, 12, 15],

             [57, 44, 53, 4, 23, 14, 25, 6],

             [52, 47, 56, 45, 54, 5, 22, 13],

             ]


# testisKnightsTour()
print(isKnightsTour([[19, 14, 3, 8, 25],
                    [4, 9, 18, 13, 2],
                    [15, 20, 1, 24, 7],
                    [10, 5, 22, 17, 12],
                    [21, 16, 11, 6, 23]]))
