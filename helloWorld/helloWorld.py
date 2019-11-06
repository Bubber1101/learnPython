class Board(object):

    def __init__(self):
        self.rows =  [[9, 9, 9],[9, 9, 9],[9, 9, 9]]

    def __str__(self):
        var = ""
        for row in self.rows:
            for spot in row:
                var += {
                    9: ' ',
                    1: 'X',
                    2: 'O'
                }.get(spot, ' ')
                var += '|'
            var += '\n------\n'
        return var

    def setSpot(self, x, y, val):
        self.rows[y][x] = val


class TicTacToeGame(object):

    def __init__(self):
        self.board = Board()
        # self.board.__init__()
        self.board.setSpot(0, 1, 1)
        self.board.setSpot(0, 2, 2)

    def printBoard(self):
        print(self.board)


if __name__ == '__main__':
    game = TicTacToeGame()
    game.printBoard()
