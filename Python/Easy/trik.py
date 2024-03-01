moves = input()

class Position:
    def __init__(self) -> None:
        self.p = 1

    def make_move(self, move):
        if move == 'A':
            self.move_a()
        elif move == 'B':
            self.move_b()
        else:
            self.move_c()

    def move_a(self):
        if self.p == 1:
            self.p = 2
        elif self.p == 2:
            self.p = 1

    def move_b(self):
        if self.p == 2:
            self.p = 3
        elif self.p == 3:
            self.p = 2

    def move_c(self):
        if self.p == 1:
            self.p = 3
        elif self.p == 3:
            self.p = 1


pos = Position()
for move in moves:
    pos.make_move(move)
print(pos.p)
