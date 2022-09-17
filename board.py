import action
from tile import BLOCK, BOX, OBJECT, PLAYER, PLAYER_ON_GOAL, WALL

class BoardManager:

    # a = player
    # @ = player ที่ทับบน goal
    # □ = block ที่ไม่อยู่ตรง goal
    # ■ = block ที่อยู่ตรง goal
    # . = goal-

    up = action.Up()
    down = action.Down()
    left = action.Left()
    right = action.Right()

    def __init__(self, board):
        board_ = board.split('\n')[1:-1]

        for b in range(len(board_)):
            board_[b] = list(board_[b])

        self.board_lst = board_

        i, j = self.playerPosition()
        self.playerI = i
        self.playerJ = j

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
            yield BoardManager.up
        # down
        if actions[1]:
            yield BoardManager.down
        # left
        if actions[2]:
            yield BoardManager.left
        # right
        if actions[3]:
            yield BoardManager.right


    def pushAction(self, action):
        newBoard = action.execute(self)
        return newBoard