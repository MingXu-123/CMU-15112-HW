
# written by Eric Clinch

###########################################################
# psuedocode for Monte Carlo Tree Search (MCTS) algorithm #
###########################################################

import math

class MCT(object):

    # creates an unexpanded node
    def __init__(self, player):
        self.score = 0
        self.visits = 0
        self.player = player

        # will take moves as keys and have children Monte Carlo Trees as values
        self.children = dict()

    # runs a round of the MCTS algorithm and returns the result of the playout
    def MCRound(self, board):
        if self.visits == 0:
            # base case / node expansion stage
            moves = board.legalMoves(self.player)
            opponent = Minnie if self.player == Maxie else Maxie
            for move in moves: # create all the children nodes
                self.children[move] = MCT(opponent)
            # play a random playout starting from the current board,
            # with it starting on self.player's turn.
            # Note that randomPlayout must be a nondestructive function,
            # and should return 1 if the starting player wins and 0 otherwise
            playoutResult = randomPlayout(board, self.player)
            self.score += playoutResult
            self.visits += 1
            return playoutResult

        else:
            # recursive case / selection stage
            selectedMove = self.selectMove()
            selectedChild = self.children[selectedMove]
            board.makeMove(selectedMove)
            playoutResult = 1 - selectedChild.MCRound(board)
            board.undoMove(selectedMove)
            self.score += playoutResult
            self.visits += 1
            return playoutResult

    def getUCB1Score(self, parentVisits):
        exploitationTerm = self.score / self.visits
        explorationTerm = math.sqrt(2 * math.log(parentVisits) / self.visits)
        return exploitationTerm + explorationTerm

    # returns the next move to select in the search
    def selectMove(self):
        bestScore = 0
        bestMove = None
        for move in self.children:
            child = self.children[move]
            if (child.visits == 0):
                # this child has never been visited, so select it
                return move
            moveScore = child.getUCB1Score(self.visits)
            if (bestMove == None or moveScore > bestScore):
                bestScore = moveScore
                bestMove = move
        return bestMove

    def getResultMove(self):
        # we'll return the move that we have visited the most
        mostVisits = 0
        bestMove = None
        for move in self.children:
            child = self.children[move]
            if (bestMove == None or child.visits > mostVisits):
                mostVisits = child.visits
                bestMove = move
        return bestMove