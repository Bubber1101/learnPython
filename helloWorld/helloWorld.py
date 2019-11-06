import random as r


class Board(object):

    def __init__(self):
        self.rows = [[9, 9, 9], [9, 9, 9], [9, 9, 9]]
        self.vals = {
            9: ' ',
            1: 'X',
            4: 'O'
        }
        self.sums = {
            3: 'X',
            12: 'O'
        }

    def __str__(self):
        var = ""
        for row in self.rows:
            for spot in row:
                var += self.vals.get(spot, ' ')
                var += '|'
            var += '\n' \
                   + 8 * '-' \
                   + '\n'
        return var

    def setSpot(self, x, y, val):
        self.rows[y][x] = val

    def checkBoard(self):
        for x in range(0, 2):
            winner = self.checkRow(x)
            if (winner):
                return winner
            winner = self.checkColumn(x)
            if (winner):
                return winner
        winner = self.checkDiagonalDown()
        if (winner):
            return winner
        winner = self.checkDiagonalUp()
        if (winner):
            return winner
        return 0

    def checkRow(self, x):
        return self.sums.get(
            self.rows[x][0]
            + self.rows[x][1]
            + self.rows[x][2], 1)

    def checkColumn(self, x):
        return self.sums.get(
            self.rows[0][x]
            + self.rows[1][x]
            + self.rows[2][x], 0)

    def checkDiagonalDown(self):
        return self.sums.get(
            self.rows[0][0]
            + self.rows[1][1]
            + self.rows[2][2], 0)

    def checkDiagonalUp(self):
        return self.sums.get(
            self.rows[2][0]
            + self.rows[1][1]
            + self.rows[0][2], 0)


class TicTacToeGame(object):

    def __init__(self):
        self.board = Board()

    def printBoard(self):
        print(self.board)

    def randomMove(self, val):
        x = r.randrange(0, 2)
        y = r.randrange(0, 2)
        if self.board.rows[x][y] != 9:
            self.randomMove(val)
        else:
            self.board.setSpot(x, y, val)
            winner = self.board.checkBoard()
            if winner:
                print(f'YaY {winner} won')


if __name__ == '__main__':
    game = TicTacToeGame()
    game.printBoard()
    while (1):
        val = int(input('select val'))
        game.randomMove(val)
        game.printBoard()
