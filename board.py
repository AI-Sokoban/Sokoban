class BoardManager:

# a = player
# @ = player ที่ทับบน goal
# □ = block ที่ไม่อยู่ตรง goal
# ■ = block ที่อยู่ตรง goal
# • = goal-

    def __init__(self,board):
        self.board = board
        return

    def __str__(self):
        return self.board

    def getBoard(self):
        return self.board

    def setBoard(self,new_board):
        self.board = new_board

    