class BoardManager:

# a = player
# @ = player ที่ทับบน goal
# □ = block ที่ไม่อยู่ตรง goal
# ■ = block ที่อยู่ตรง goal
# . = goal-

    def __init__(self,board):
        board_ = board.split('\n')[1:-1]

        for b in range(len(board_)):
            board_[b] = list(board_[b])

        self.board_lst = board_
        return

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

    def updateBoard(self,new_board):
        self.board_lst = new_board

    def playerPosition(self):
       for i in range(len(self.board_lst)):
        for j in range(len(self.board_lst[i])):
            if self.board_lst[i][j] == 'a' or self.board_lst[i][j] == '@':
                return i,j
