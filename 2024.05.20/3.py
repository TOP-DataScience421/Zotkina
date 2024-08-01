class ChessKing:
    files = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8}
    ranks = {str(i): i for i in range(1, 9)}

    def __init__(self, color: str = 'white', square: str = None):
        self.color = color
        if square is None:
            self.square = 'e1' if color == 'white' else 'e8'
        else:
            self.square = square

    def __repr__(self):
        return f"{self.color[0].upper()}K: {self.square}"

    def __str__(self):
        return self.__repr__()

    def is_turn_valid(self, new_square: str) -> bool:
        if new_square[0] not in self.files or new_square[1] not in self.ranks:
            return False

        file_diff = abs(self.files[new_square[0]] - self.files[self.square[0]])
        rank_diff = abs(self.ranks[new_square[1]] - self.ranks[self.square[1]])

        return file_diff <= 1 and rank_diff <= 1 and (file_diff + rank_diff) > 0

    def turn(self, new_square: str) -> None:
        if not self.is_turn_valid(new_square):
            raise ValueError(f"Invalid move for {self.color} king from {self.square} to {new_square}")
        self.square = new_square

#пример теста
#>>> wk = ChessKing()
#>>> wk.color
#'white'
#>>> wk.square
#'e1'
#>>> wk.turn('e2')
#>>> wk
#WK: e2
#>>> wk.turn('d4')
#Traceback (most recent call last):
#  File "<stdin>", line 1, in <module>
#  File "C:\Git\Zotkina\2024.05.20\3.py", line 29, in turn
#    raise ValueError(f"Invalid move for {self.color} king from {self.square} to {new_square}")
#ValueError: Invalid move for white king from e2 to d4
#>>> bk = ChessKing('black')
#>>> print(bk)
#BK: e8
