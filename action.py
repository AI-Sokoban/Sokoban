from board import BoardManager
class Action:

    def __init__(self,board : BoardManager):
        self.board = board
        return

    def up(self):
        b = self.board.getBoard()
        self.board.setBoard(b + "132456")
        return