from board import BoardManager
class Action:

    def __init__(self,board_lst : BoardManager):
        self.board_lst = board_lst
        self.obj = ['□','■','#']
        self.block = ['□','■']
    
        return

    def checkMovingState(self):
        i,j = self.board_lst.playerPosition()
        boardlist = self.board_lst.getBoardList()
        
        up,down,left,right = True,True,True,True

        #up
        if boardlist[i-1][j] in self.obj:
            if boardlist[i-1][j] == "#": #เจอกำแพง
                up = False
            elif (boardlist[i-1][j] in self.block) and (boardlist[i-2][j] in self.obj): #เจอกล่อง แล้วกล่องชนกับ object
                up = False

        #down
        if boardlist[i+1][j] in self.obj:
            if boardlist[i+1][j] == "#": #เจอกำแพง
                down = False
            elif (boardlist[i+1][j] in self.block) and (boardlist[i+2][j] in self.obj): #เจอกล่อง แล้วกล่องชนกับ object
                down = False

        #left
        if boardlist[i][j-1] in self.obj:
            if boardlist[i][j-1] == "#": #เจอกำแพง
                left = False
            elif (boardlist[i][j-1] in self.block) and (boardlist[i][j-2] in self.obj): #เจอกล่อง แล้วกล่องชนกับ object
                left = False

        #right
        if boardlist[i][j+1] in self.obj:
            if boardlist[i][j+1] == "#": #เจอกำแพง
                right = False
            elif (boardlist[i][j+1] in self.block) and (boardlist[i][j+2] in self.obj): #เจอกล่อง แล้วกล่องชนกับ object
                right = False

        return up,down,left,right

    def up(self):
        moving = self.checkMovingState()[0]

        if moving == False:
            return False

        i, j = self.board_lst.playerI, self.board_lst.playerJ
        boardlist = self.board_lst.getBoardList()

        #move กล่อง ถ้ามี
        if boardlist[i-1][j] in self.block:
            boardlist[i-1][j] = "." if boardlist[i-1][j] == "■" else " "
            boardlist[i-2][j] = "■" if boardlist[i-2][j] == "." else "□"

        #move player
        boardlist[i-1][j] = "@" if boardlist[i-1][j] == "." else "a"
        boardlist[i][j] = "." if boardlist[i][j] == "@" else " "

        self.board_lst.playerI -= 1

        self.board_lst.updateBoard(boardlist)
        return True

    def down(self):
        moving = self.checkMovingState()[1]

        if moving == False:
            return False

        i, j = self.board_lst.playerI, self.board_lst.playerJ
        boardlist = self.board_lst.getBoardList()

        #move กล่อง ถ้ามี
        if boardlist[i+1][j] in self.block:
            boardlist[i+1][j] = "." if boardlist[i+1][j] == "■" else " "
            boardlist[i+2][j] = "■" if boardlist[i+2][j] == "." else "□"

        #move player
        boardlist[i+1][j] = "@" if boardlist[i+1][j] == "." else "a"
        boardlist[i][j] = "." if boardlist[i][j] == "@" else " "

        self.board_lst.playerI += 1

        self.board_lst.updateBoard(boardlist)
        return True

    def left(self):
        moving = self.checkMovingState()[2]

        if moving == False:
            return False

        i, j = self.board_lst.playerI, self.board_lst.playerJ
        boardlist = self.board_lst.getBoardList()

        #move กล่อง ถ้ามี
        if boardlist[i][j-1] in self.block:
            boardlist[i][j-1] = "." if boardlist[i][j-1] == "■" else " "
            boardlist[i][j-2] = "■" if boardlist[i][j-2] == "." else "□"

        #move player
        boardlist[i][j-1] = "@" if boardlist[i][j-1] == "." else "a"
        boardlist[i][j] = "." if boardlist[i][j] == "@" else " "

        self.board_lst.playerJ -= 1

        self.board_lst.updateBoard(boardlist)
        return True

    def right(self):
        moving = self.checkMovingState()[3]

        if moving == False:
            return False

        i, j = self.board_lst.playerI, self.board_lst.playerJ
        boardlist = self.board_lst.getBoardList()

        #move กล่อง ถ้ามี
        if boardlist[i][j+1] in self.block:
            boardlist[i][j+1] = "." if boardlist[i][j+1] == "■" else " "
            boardlist[i][j+2] = "■" if boardlist[i][j+2] == "." else "□"

        #move player
        boardlist[i][j+1] = "@" if boardlist[i][j+1] == "." else "a"
        boardlist[i][j] = "." if boardlist[i][j] == "@" else " "

        self.board_lst.playerJ += 1

        self.board_lst.updateBoard(boardlist)
        return True

    def validActions(self):
        actions = self.checkMovingState()
        if actions[0]:
            yield self.up

        if actions[1]:
            yield self.down

        if actions[2]:
            yield self.left

        if actions[3]:
            yield self.right
