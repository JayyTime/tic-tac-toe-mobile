from itertools import permutations as per
from wids.score import Score

class TicTacToe:
    player_moves1 = []
    player_moves2 = []
    winner = ''
    crossed_boxes = 0
    uncrossed_boxes = 9
    app = ''

    def win(self, turn, app, mode):
        self.app = app
        self.mode = mode
        self.crossed_boxes += 1
        self.uncrossed_boxes -= 1
        winning_cases = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6],
                         [1, 4, 7], [2, 4, 8], [0, 4, 8], [2, 4, 6]]
        if turn == 1:
            lista = self.player_moves1
        else:
            lista = self.player_moves2

        # Iteriert durch alle möglichen Winning- Cases und checkt,
        # ob einer der Spieler einen Winning- Cases erreicht hat
        for case in winning_cases:
            for combination in list(per(lista, len(lista))):
                for case2 in list(per(case, len(case2))):
                    if list(combination) == list(case2):
                        return True
        return False

    def tie(self):
        if self.crossed_boxes == 9 and self.uncrossed_boxes == 0:
            self.app.open_score('tie', self.mode)

    def reset(self):
        self.player_moves1.clear()
        self.player_moves2.clear()
        self.crossed_boxes = 0
        self.uncrossed_boxes = 9
        self.winner = ''
        self.app = ''
