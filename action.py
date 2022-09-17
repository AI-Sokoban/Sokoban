import copy
from tile import *

"""
board - มี type BoardManager

method execute จะ return ค่าออกมาสองค่าคือ board ใน state ใหม่กับ boolean ที่บอกว่ากล่องถูกดันหรือไม่

method restore ในทุก class จะทำงานถูกต้องเมื่อ action ทุกๆ action มีการเปลี่ยนแปลงไปยัง board เท่านั้น
ควรจะใช้ method นี้เมื่อ action ที่ได้มาจาก getValidActions
"""


class Up:
    def execute(self, board, alloc=False):
        i, j = board.playerI, board.playerJ

        newBoard = board
        if alloc:
            newBoard = copy.deepcopy(board)

        boardlist = newBoard.board_lst
        
        isBoxPush = False
        #move กล่อง ถ้ามี
        if boardlist[i-1][j] in BLOCK:
            boardlist[i-1][j] = GOAL if boardlist[i-1][j] == BOX_ON_GOAL else EMPTY
            boardlist[i-2][j] = BOX_ON_GOAL if boardlist[i-2][j] == GOAL else BOX
            isBoxPush = True

        #move player
        boardlist[i-1][j] = PLAYER_ON_GOAL if boardlist[i-1][j] == GOAL else PLAYER
        boardlist[i][j] = GOAL if boardlist[i][j] == PLAYER_ON_GOAL else EMPTY

        newBoard.playerI -= 1

        return newBoard, isBoxPush

    def restore(self, board, isBoxPush, alloc=False):
        i, j = board.playerI, board.playerJ

        newBoard = board
        if alloc:
            newBoard = copy.deepcopy(board)

        boardlist = newBoard.board_lst

        boardlist[i+1][j] = PLAYER if boardlist[i+1][j] == EMPTY else PLAYER_ON_GOAL
        if isBoxPush:
            boardlist[i][j] = BOX if boardlist[i][j] == PLAYER else BOX_ON_GOAL
            boardlist[i-1][j] = EMPTY if boardlist[i-1][j] == BOX else GOAL
        else:
            boardlist[i][j] = EMPTY if boardlist[i][j] == PLAYER else GOAL

        newBoard.playerI += 1

        return newBoard
        

class Down:
    def execute(self, board, alloc=False):
        i, j = board.playerI, board.playerJ

        newBoard = board
        if alloc:
            newBoard = copy.deepcopy(board)

        boardlist = newBoard.board_lst

        isBoxPush = False
        #move กล่อง ถ้ามี
        if boardlist[i+1][j] in BLOCK:
            boardlist[i+1][j] = GOAL if boardlist[i+1][j] == BOX_ON_GOAL else EMPTY
            boardlist[i+2][j] = BOX_ON_GOAL if boardlist[i+2][j] == GOAL else BOX
            isBoxPush = True

        #move player
        boardlist[i+1][j] = PLAYER_ON_GOAL if boardlist[i+1][j] == GOAL else PLAYER
        boardlist[i][j] = GOAL if boardlist[i][j] == PLAYER_ON_GOAL else EMPTY

        newBoard.playerI += 1

        return newBoard, isBoxPush

    def restore(self, board, isBoxPush, alloc=False):
        i, j = board.playerI, board.playerJ

        newBoard = board
        if alloc:
            newBoard = copy.deepcopy(board)

        boardlist = newBoard.board_lst

        boardlist[i-1][j] = PLAYER if boardlist[i-1][j] == EMPTY else PLAYER_ON_GOAL
        if isBoxPush:
            boardlist[i][j] = BOX if boardlist[i][j] == PLAYER else BOX_ON_GOAL
            boardlist[i+1][j] = EMPTY if boardlist[i+1][j] == BOX else GOAL
        else:
            boardlist[i][j] = EMPTY if boardlist[i][j] == PLAYER else GOAL

        newBoard.playerI -= 1

        return newBoard


class Left:
    def execute(self, board, alloc=False):
        i, j = board.playerI, board.playerJ

        newBoard = board
        if alloc:
            newBoard = copy.deepcopy(board)

        boardlist = newBoard.board_lst

        isBoxPush = False
        #move กล่อง ถ้ามี
        if boardlist[i][j-1] in BLOCK:
            boardlist[i][j-1] = GOAL if boardlist[i][j-1] == BOX_ON_GOAL else EMPTY
            boardlist[i][j-2] = BOX_ON_GOAL if boardlist[i][j-2] == GOAL else BOX
            isBoxPush = True

        #move player
        boardlist[i][j-1] = PLAYER_ON_GOAL if boardlist[i][j-1] == GOAL else PLAYER
        boardlist[i][j] = GOAL if boardlist[i][j] == PLAYER_ON_GOAL else EMPTY

        newBoard.playerJ -= 1

        return newBoard, isBoxPush

    def restore(self, board, isBoxPush, alloc=False):
        i, j = board.playerI, board.playerJ

        newBoard = board
        if alloc:
            newBoard = copy.deepcopy(board)

        boardlist = newBoard.board_lst

        boardlist[i][j+1] = PLAYER if boardlist[i][j+1] == EMPTY else PLAYER_ON_GOAL
        if isBoxPush:
            boardlist[i][j] = BOX if boardlist[i][j] == PLAYER else BOX_ON_GOAL
            boardlist[i][j-1] = EMPTY if boardlist[i][j-1] == BOX else GOAL
        else:
            boardlist[i][j] = EMPTY if boardlist[i][j] == PLAYER else GOAL

        newBoard.playerJ += 1

        return newBoard


class Right:
    def execute(self, board, alloc=False):
        i, j = board.playerI, board.playerJ

        newBoard = board
        if alloc:
            newBoard = copy.deepcopy(board)

        boardlist = newBoard.board_lst

        isBoxPush = False
        #move กล่อง ถ้ามี
        if boardlist[i][j+1] in BLOCK:
            boardlist[i][j+1] = GOAL if boardlist[i][j+1] == BOX_ON_GOAL else EMPTY
            boardlist[i][j+2] = BOX_ON_GOAL if boardlist[i][j+2] == GOAL else BOX
            isBoxPush = True

        #move player
        boardlist[i][j+1] = PLAYER_ON_GOAL if boardlist[i][j+1] == GOAL else PLAYER
        boardlist[i][j] = GOAL if boardlist[i][j] == PLAYER_ON_GOAL else EMPTY

        newBoard.playerJ += 1

        return newBoard, isBoxPush

    def restore(self, board, isBoxPush, alloc=False):
        i, j = board.playerI, board.playerJ

        newBoard = board
        if alloc:
            newBoard = copy.deepcopy(board)

        boardlist = newBoard.board_lst

        boardlist[i][j-1] = PLAYER if boardlist[i][j-1] == EMPTY else PLAYER_ON_GOAL
        if isBoxPush:
            boardlist[i][j] = BOX if boardlist[i][j] == PLAYER else BOX_ON_GOAL
            boardlist[i][j+1] = EMPTY if boardlist[i][j+1] == BOX else GOAL
        else:
            boardlist[i][j] = EMPTY if boardlist[i][j] == PLAYER else GOAL

        newBoard.playerJ -= 1

        return newBoard