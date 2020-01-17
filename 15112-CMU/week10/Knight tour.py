# this is the decorator for makeExample2DList
def print2DListResult(makeExample2DList):
    def printLst(n):
        lst = makeExample2DList(n)
        rows = len(lst)
        cols = len(lst[0])
        res = ''
        for row in range(rows):
            res += ("[" + " "*n)
            for col in range(cols):
                numOfspace = n
                lenOfnum = len(str(lst[row][col]))
                if lenOfnum > 1:
                    numOfspace -= (lenOfnum - 1)
                res += str(lst[row][col])
                res += " " * numOfspace
            res += "]\n"
        return res
    return printLst

# this is the main function for make example 2D list
@print2DListResult
def makeExample2DList(n):
    myList=createKnightBoard(n)
    return myList

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
    if board == None:
        return False
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


# this is the create knight's board function
def createKnightBoard(n):
    rows, cols = n, n
    board = []
    for i in range(n):
        board += [[0]*cols]
    return board


def traverse(board, x, y, count):
    rows, cols = len(board), len(board)
    board[x][y] = count
    if count >= rows * cols:
        return board
    directionY = [2, 2, 1, -1, -2, -2, -1, 1]
    directionX = [-1, 1, 2, 2, 1, -1, -2, -2]
    numOfdirection = 8
    for i in range(numOfdirection):
        nextX = x + directionX[i]
        nextY = y + directionY[i]
        if (nextX < 0 or nextX >= cols or nextY < 0 or nextY >= rows)\
                or board[nextX][nextY] != 0:
            continue
        tmpboard = traverse(board, nextX, nextY, count + 1)
        if tmpboard != None:
            return tmpboard
        # if tmpboard is None, then undo the move
        board[nextX][nextY] = 0


# This is the main function for createKnightsTour
def createKnightsTour(n):
    if n == 1:
        return [[1]]
    if n == 2:
        return None
    board = createKnightBoard(n)
    startRow = 0
    startCol = 0
    count = 1
    traverse(board, startRow, startCol, count)
    if isKnightsTour(board):
        return board
    else:
        return None



def testCreateKnightsTour():
    #The only n=1 board:
    board0 = [[1]]

    #A few different n=5 boards:
    board1 = [
    [ 1,  20, 9,  14, 3  ],
    [ 10, 15, 2,  19, 24 ],
    [ 21, 8,  25, 4,  13 ],
    [ 16, 11, 6,  23, 18 ],
    [ 7,  22, 17, 12, 5  ],
    ]

    board2 = [
    [ 1,  18, 23, 12, 7  ],
    [ 24, 13, 8,  17, 22 ],
    [ 19, 2,  25, 6,  11 ],
    [ 14, 9,  4,  21, 16 ],
    [ 3,  20, 15, 10, 5  ],
    ]

    board3 = createKnightsTour(5)
    board6 = createKnightsTour(1)

    #Our isKnightsTour function from HW5 should return True for each
    assert(isKnightsTour(board0)==True)
    assert(isKnightsTour(board1)==True)
    assert(isKnightsTour(board2)==True)
    assert(isKnightsTour(board3) ==True)
    assert(createKnightsTour(3) == None)
    assert(createKnightsTour(4) == None)
    assert(isKnightsTour(board6) == True)
    assert(createKnightsTour(2) == None)
    assert (createKnightsTour(1) == [[1]])
    print("Passed!")

testCreateKnightsTour()
# print(createKnightsTour(5))
# print(createKnightsTour(3))
# print(createKnightsTour(4))
# print(createKnightsTour(6))
# print(createKnightsTour(2))
