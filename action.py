import copy
from tile import *

class Up:
    def execute(self, board):
        i, j = board.playerI, board.playerJ

        newBoard = copy.deepcopy(board)

        boardlist = newBoard.board_lst
        
        #move กล่อง ถ้ามี
        if boardlist[i-1][j] in BLOCK:
            boardlist[i-1][j] = GOAL if boardlist[i-1][j] == BOX_ON_GOAL else EMPTY
            boardlist[i-2][j] = BOX_ON_GOAL if boardlist[i-2][j] == GOAL else BOX

        #move player
        boardlist[i-1][j] = PLAYER_ON_GOAL if boardlist[i-1][j] == GOAL else PLAYER
        boardlist[i][j] = GOAL if boardlist[i][j] == PLAYER_ON_GOAL else EMPTY

        newBoard.playerI -= 1

        return newBoard
        

class Down:
    def execute(self, board):
        i, j = board.playerI, board.playerJ

        newBoard = copy.deepcopy(board)

        boardlist = newBoard.board_lst

        #move กล่อง ถ้ามี
        if boardlist[i+1][j] in BLOCK:
            boardlist[i+1][j] = GOAL if boardlist[i+1][j] == BOX_ON_GOAL else EMPTY
            boardlist[i+2][j] = BOX_ON_GOAL if boardlist[i+2][j] == GOAL else BOX

        #move player
        boardlist[i+1][j] = PLAYER_ON_GOAL if boardlist[i+1][j] == GOAL else PLAYER
        boardlist[i][j] = GOAL if boardlist[i][j] == PLAYER_ON_GOAL else EMPTY

        newBoard.playerI += 1

        return newBoard

class Left:
    def execute(self, board):
        i, j = board.playerI, board.playerJ

        newBoard = copy.deepcopy(board)

        boardlist = newBoard.board_lst

        #move กล่อง ถ้ามี
        if boardlist[i][j-1] in BLOCK:
            boardlist[i][j-1] = GOAL if boardlist[i][j-1] == BOX_ON_GOAL else EMPTY
            boardlist[i][j-2] = BOX_ON_GOAL if boardlist[i][j-2] == GOAL else BOX

        #move player
        boardlist[i][j-1] = PLAYER_ON_GOAL if boardlist[i][j-1] == GOAL else PLAYER
        boardlist[i][j] = GOAL if boardlist[i][j] == PLAYER_ON_GOAL else EMPTY

        newBoard.playerJ -= 1

        return newBoard

class Right:
    def execute(self, board):
        i, j = board.playerI, board.playerJ

        newBoard = copy.deepcopy(board)

        boardlist = newBoard.board_lst

        #move กล่อง ถ้ามี
        if boardlist[i][j+1] in BLOCK:
            boardlist[i][j+1] = GOAL if boardlist[i][j+1] == BOX_ON_GOAL else EMPTY
            boardlist[i][j+2] = BOX_ON_GOAL if boardlist[i][j+2] == GOAL else BOX

        #move player
        boardlist[i][j+1] = BOX_ON_GOAL if boardlist[i][j+1] == GOAL else PLAYER
        boardlist[i][j] = GOAL if boardlist[i][j] == PLAYER_ON_GOAL else EMPTY

        newBoard.playerJ += 1

        return newBoard