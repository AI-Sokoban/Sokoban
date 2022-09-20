from board import BoardManager

from collections import deque

# 8x8
data = [
    """
########
#      #
##a   ##
##.□■  #
##  #  #
#      #
#      #
########
""",
    """
########
#      #
##  a ##
##.□□  #
##  #  #
#      #
#   .  #
########
""",
    """
##########
#        #
##  a   ##
##.  □   #
##  #    #
#    □   #
#   .    #
##########
"""
]

class ProblemState:
    def __init__(self, board: BoardManager, action: str = None, prevState = None):
        self.board = board
        self.action = action
        self.prevState = prevState

    def __hash__(self):
        return self.board.__hash__()

    def __eq__(self, other):
        return self.board.__eq__(other.board)

def solution(state: ProblemState):
    result = []
    while state.action:
        result.append(state.action)
        state = state.prevState

    return list(reversed(result))

def bfs(board: BoardManager):
    initialState = ProblemState(board)
    queue = deque([initialState])

    if initialState.board.isGameOver():
        return solution(initialState)

    exploredSet = set()

    while len(queue) >0 :
        state = queue.popleft()
        exploredSet.add(state)

        for action in state.board.getValidActions():
            newBoard = state.board.push(action, True)
            childState = ProblemState(newBoard,action,state)

            if(childState not in exploredSet) and (childState not in queue):
                if childState.board.isGameOver():
                    return solution(childState)
                queue.append(childState)
   

level = 0
sokoban = BoardManager(data[level])
print(bfs(sokoban))

