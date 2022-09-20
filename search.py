import time
from board import BoardManager

from collections import deque

# renderer
from render import Renderer
import msvcrt

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

def bfs(board: BoardManager,renderer : Renderer = None):
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

            #newBoard Renderer
            if renderer : 
                renderer.fromInstance(newBoard).render()
                # wait for input to change render
                # msvcrt.getch()
                # time delay for renderer only
                time.sleep(0.01)
                

            childState = ProblemState(newBoard,action,state)

            if(childState not in exploredSet) and (childState not in queue):
                if childState.board.isGameOver():
                    return solution(childState)
                queue.append(childState)

level = 0  
isRender = True
sokoban = BoardManager(data[level])
renderer = Renderer(sokoban).setCaption("Sokoban")

renderer.render()
print(bfs(sokoban,renderer if isRender else None))

