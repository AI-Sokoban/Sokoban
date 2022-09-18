from collections import deque
from board import BoardManager



class State:
    def __init__(self, board, action=None, state=None):
        self.board = board
        self.prevState = state
        self.action = action


def bfs(sokoban: BoardManager):
    initialState = State(sokoban)
    queue = deque([initialState])

    if sokoban.isGameOver():
        return 

    exploredSet = set()
    
    while len(queue) > 0:
        state = queue.popleft()
        exploredSet.add(state)

        for action in state.board.getValidActions():
            state.board.push(action)
            # childState = State(state.board, action, )