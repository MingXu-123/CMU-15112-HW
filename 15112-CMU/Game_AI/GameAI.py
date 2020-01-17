# written by Eric Clinch

#####################################################
# psuedocode for minimax with no heuristic          #
#####################################################

# takes a board and returns a tuple (move, score) where move is the
# best move for Maxie and score is the board score that results
# from making that move. The best move is the one that maximizes
# Maxie's score by maximizing the board score
def MaxieMove(board):
    if board.gameOver():
        return (None, float('inf')) if board.won(Maxie) else (None, float('-inf'))
    else:
        bestMove = None
        bestScore = float('-inf')
        for move in board.legalMoves(Maxie):
            board.makeMove(move)
            _, moveScore = MinnieMove(board)
            board.undoMove(move)
            if moveScore > bestScore:
                bestScore = moveScore
                bestMove = move
        return (bestMove, bestScore)

# same as Maxie, but maximizes Minnie's score by minimizing
# the board score
def MinnieMove(board):
    if board.gameOver():
        return (None, float('-inf')) if board.won(Minnie) else (None, float('inf'))
    else:
        bestMove = None
        bestScore = float('inf')
        for move in board.legalMoves(Minnie):
            board.makeMove(move)
            _, moveScore = MaxieMove(board)
            board.undoMove(move)
            if moveScore < bestScore:
                bestScore = moveScore
                bestMove = move
        return (bestMove, bestScore)

#####################################################
# psuedocode for minimax with heuristics            #
#####################################################

# takes a board and depth and returns a tuple (move, score) where move is the
# best move for Maxie and score is the board score that results
# from making that move. The best move is the one that maximizes
# Maxie's score by maximizing the board score.
# If depth is the max depth, returns the score given by a heuristic function
def MaxieMoveWithHeuristics(board, depth):
    if board.gameOver():
        return (None, float('inf')) if board.won(Maxie) else (None, float('-inf'))
    else if depth == maxDepth:
        return (None, heuristic(board))
    else:
        bestMove = None
        bestScore = float('-inf')
        for move in board.legalMoves(Maxie):
            board.makeMove(move)
            _, moveScore = MinnieMoveWithHeuristics(board, depth + 1)
            board.undoMove(move)
            if moveScore > bestScore:
                bestScore = moveScore
                bestMove = move
        return (bestMove, bestScore)

# same as Maxie, but maximizes Minnie's score by minimizing
# the board score
def MinnieMoveWithHeuristics(board, depth):
    if board.gameOver():
        return (None, float('-inf')) if board.won(Minnie) else (None, float('inf'))
    else if depth == maxDepth:
        return (None, heuristic(board))
    else:
        bestMove = None
        bestScore = float('inf')
        for move in board.legalMoves(Minnie):
            board.makeMove(move)
            _, moveScore = MaxieMoveWithHeuristics(board, depth + 1)
            board.undoMove(move)
            if moveScore < bestScore:
                bestScore = moveScore
                bestMove = move
        return (bestMove, bestScore)

#################################################################
# psuedocode for minimax with heuristics and alpha-beta pruning #
#################################################################

# takes a board, depth, alpha, and beta where alpha and beta are 
# the best scores guaranteed for Maxie and Minnie, respectively.
# Returns a tuple (move, score) where move is the
# best move for Maxie and score is the board score that results
# from making that move. The best move is the one that maximizes
# Maxie's score by maximizing the board score.
# Uses alpha-beta pruning to prune this part of the game tree if it
# detects that this branch will never be relevant to the overall search.
# If depth is the max depth, returns the score given by a heuristic function
def MaxieMoveAlphaBeta(board, depth, alpha, beta):
    assert(alpha < beta)
    if board.gameOver():
        return (None, float('inf')) if board.won(Maxie) else (None, float('-inf'))
    else if depth == maxDepth:
        return (None, heuristic(board))
    else:
        bestMove = None
        bestScore = float('-inf')
        for move in board.legalMoves(Maxie):
            board.makeMove(move)
            _, moveScore = MinnieMoveAlphaBeta(board, depth + 1, alpha, beta)
            board.undoMove(move)
            if moveScore > bestScore:
                bestScore = moveScore
                bestMove = move
                alpha = max(alpha, bestScore)
                if (alpha >= beta):
                    return (bestMove, bestScore)
        return (bestMove, bestScore)

# same as Maxie, but maximizes Minnie's score by minimizing
# the board score
def MinnieMoveAlphaBeta(board, depth, alpha, beta):
    assert(alpha < beta)
    if board.gameOver():
        return (None, float('-inf')) if board.won(Minnie) else (None, float('inf'))
    else if depth == maxDepth:
        return heuristic(board)
    else:
        bestMove = None
        bestScore = float('inf')
        for move in board.legalMoves(Minnie):
            board.makeMove(move)
            _, moveScore = MaxieMoveAlphaBeta(board, depth + 1, alpha, beta)
            board.undoMove(move)
            if moveScore < bestScore:
                bestScore = moveScore
                bestMove = move
                beta = min(beta, bestScore)
                if (alpha >= beta):
                    return (bestMove, bestScore)
        return (bestMove, bestScore)