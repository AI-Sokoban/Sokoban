import action
from tile import BLOCK, BOX, OBJECT, PLAYER, PLAYER_ON_GOAL, WALL,EMPTY,BOX_ON_GOAL,GOAL 
import random

HASHING_PIECE = 5

HASH_TILE = [PLAYER, PLAYER_ON_GOAL, BOX,BOX_ON_GOAL,GOAL ]

UNHASH_TILE = {EMPTY, WALL}

def generateZobristTable(board):
    size = 0
    for row in board:
        for tile in row:
            size += 1

    table = [[0 for _ in range(HASHING_PIECE)] for _ in range(size)]

    for i in range(size):
        for j in range(HASHING_PIECE):
            table[i][j] = random.getrandbits(64)

    return table

class BoardManager:

    # a = player
    # @ = player ที่ทับบน goal
    # □ = block ที่ไม่อยู่ตรง goal
    # ■ = block ที่อยู่ตรง goal
    # . = goal-

    def __init__(self, board):
        board_ = board.split('\n')[1:-1]

        for b in range(len(board_)):
            board_[b] = list(board_[b])

        self.board_lst = board_
        self.zobristTable = generateZobristTable(self.board_lst)

        self.setPlayerPosition()

        self.history = []

    def __str__(self):
        return self.getBoard()

    def getBoard(self):
        board_lst = []
        for bb in self.board_lst:
            board_lst.append("".join(bb))
        board_lst = [''] + board_lst + ['']
        return "\n".join(board_lst)

    def getBoardList(self):
        return self.board_lst

    def updateBoard(self, new_board):
        self.board_lst = new_board

    def setPlayerPosition(self):
        i, j = self.playerPosition()
        self.playerI = i
        self.playerJ = j

    def playerPosition(self):
        for i in range(len(self.board_lst)):
            for j in range(len(self.board_lst[i])):
                if self.board_lst[i][j] == PLAYER or self.board_lst[i][j] == PLAYER_ON_GOAL:
                    return i, j

    def isGameOver(self):
        for i in range(len(self.board_lst)):
            for j in range(len(self.board_lst[i])):
                if self.board_lst[i][j] == BOX:
                    return False
        return True

    def genNewBoard(self, board):
        board_ = board.split('\n')[1:-1]

        for b in range(len(board_)):
            board_[b] = list(board_[b])

        self.board_lst = board_
        self.setPlayerPosition()

    def checkMovingState(self):
        boardlist = self.board_lst
        i, j = self.playerI, self.playerJ

        up,down,left,right = True,True,True,True

        #up
        if boardlist[i-1][j] in OBJECT:
            if boardlist[i-1][j] == WALL: #เจอกำแพง
                up = False
            elif (boardlist[i-1][j] in BLOCK) and (boardlist[i-2][j] in OBJECT): #เจอกล่อง แล้วกล่องชนกับ object
                up = False

        #down
        if boardlist[i+1][j] in OBJECT:
            if boardlist[i+1][j] == WALL: #เจอกำแพง
                down = False
            elif (boardlist[i+1][j] in BLOCK) and (boardlist[i+2][j] in OBJECT): #เจอกล่อง แล้วกล่องชนกับ object
                down = False

        #left
        if boardlist[i][j-1] in OBJECT:
            if boardlist[i][j-1] == WALL: #เจอกำแพง
                left = False
            elif (boardlist[i][j-1] in BLOCK) and (boardlist[i][j-2] in OBJECT): #เจอกล่อง แล้วกล่องชนกับ object
                left = False

        #right
        if boardlist[i][j+1] in OBJECT:
            if boardlist[i][j+1] == WALL: #เจอกำแพง
                right = False
            elif (boardlist[i][j+1] in BLOCK) and (boardlist[i][j+2] in OBJECT): #เจอกล่อง แล้วกล่องชนกับ object
                right = False

        return up,down,left,right


    def getValidActions(self):
        actions = self.checkMovingState()
        
        # up
        if actions[0]:
            yield action.Up
        # down
        if actions[1]:
            yield action.Down
        # left
        if actions[2]:
            yield action.Left
        # right
        if actions[3]:
            yield action.Right

    def __hash__(self):
        hash_value = 0
        table = self.zobristTable

        idx = 0
        for i, row in enumerate(self.board_lst):
            for j, tile in enumerate(row):
                if tile not in UNHASH_TILE:
                    tile_zobrist_idx = HASH_TILE.index(tile)
                    hash_value ^= table[idx][tile_zobrist_idx]
                idx += 1

        return hash_value
    def __eq__(self, other):
        if isinstance(other, BoardManager):
            return hash(self) == hash(other)
        return False

    """
    alloc(bool) - ถ้า true จะทำ deepcopy กับ board เพื่อสร้าง board ใน state ใหม่ขึ้นมา

    return(BoardManager) - board ใน state ใหม่หลังจาก execute action ไปแล้ว
    """
    def push(self, action, alloc=False):
        newBoard, isBoxPush = action.execute(self, alloc)
        newBoard.history.append((action, isBoxPush))
        return newBoard

    """
    return(tuple[oldboard, action]) - action ล่าสุดกับ board ใน state เก่า
    """
    def pop(self, alloc=False):
        recentlyAction, isBoxPush = self.history.pop()
        board = recentlyAction.restore(self, isBoxPush, alloc)

        return  board, recentlyAction