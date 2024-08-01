from collections.abc import Iterable
from numbers import Number
from typing import List, Callable, Self


RawRow = Iterable[Number]
RawMatrix = Iterable[RawRow]

class Matrix:
    def __init__(self, raw_matrix: RawMatrix):
        if not self.is_valid(raw_matrix):
            raise ValueError("невозможно сконструировать матрицу")
        
        self.__rows = [list(row) for row in raw_matrix]
        self.n = len(self.__rows)
        self.m = len(self.__rows[0])

    @staticmethod
    def is_valid(processed_matrix: RawMatrix) -> bool:
        if not isinstance(processed_matrix, Iterable):
            return False
        
        iterator = iter(processed_matrix)
        first_row = next(iterator, None)
        if not first_row or not isinstance(first_row, Iterable):
            return False

        row_length = len(list(first_row))
        if not all(isinstance(num, Number) for num in first_row):
            return False

        for row in iterator:
            if not isinstance(row, Iterable) or len(list(row)) != row_length or not all(isinstance(num, Number) for num in row):
                return False
        
        return True

    def __getitem__(self, index: int) -> List[Number]:
        return self.__rows[index]

    @property
    def transpose(self) -> Self:
        transposed_matrix = [[self.__rows[j][i] for j in range(self.n)] for i in range(self.m)]
        return Matrix(transposed_matrix)

    def __element_wise_operation(self, other: Self | Number, operation: Callable) -> Self:
        if isinstance(other, Matrix):
            if self.n != other.n or self.m != other.m:
                raise ValueError("сложение и вычитание возможно только для матриц одной размерности")
            result_matrix = [
                [operation(self.__rows[i][j], other[i][j]) for j in range(self.m)] 
                for i in range(self.n)
            ]
        elif isinstance(other, Number):
            result_matrix = [
                [operation(self.__rows[i][j], other) for j in range(self.m)] 
                for i in range(self.n)
            ]
        else:
            raise TypeError("алгебраические операции возможны только с матрицами и числами")
        return Matrix(result_matrix)

    def __add__(self, other: Self | Number) -> Self:
        return self.__element_wise_operation(other, lambda x, y: x + y)

    def __radd__(self, other: Number) -> Self:
        return self.__add__(other)

    def __neg__(self) -> Self:
        return self.__element_wise_operation(-1, lambda x, y: x * y)

    def __sub__(self, other: Self | Number) -> Self:
        return self.__element_wise_operation(other, lambda x, y: x - y)

    def __rsub__(self, other: Number) -> Self:
        return self.__element_wise_operation(other, lambda x, y: y - x)

    def __mul__(self, other: Number) -> Self:
        return self.__element_wise_operation(other, lambda x, y: x * y)

    def __rmul__(self, other: Number) -> Self:
        return self.__mul__(other)

    def __repr__(self) -> str:
        col_widths = [max(len(str(self.__rows[i][j])) for i in range(self.n)) for j in range(self.m)]
        matrix_str = "\n".join(
            " ".join(f"{str(self.__rows[i][j]).rjust(col_widths[j])}" for j in range(self.m)) 
            for i in range(self.n)
        )
        return matrix_str


#>>> Matrix([[1, 2], [1, 2, 3, 4]])
#Traceback (most recent call last):
#  File "<stdin>", line 1, in <module>
#  File "C:\Git\Zotkina\2024.05.29\1.py", line 12, in __init__
#    raise ValueError("невозможно сконструировать матрицу")
#ValueError: невозможно сконструировать матрицу
#>>> m1 = Matrix([[1, 1, 1], [1, 1, 1]])
#>>> m2 = Matrix([[3, 3, 3], [3, 3, 3]])
#>>> m1
#1 1 1
#1 1 1
#>>> m2
#3 3 3
#3 3 3
#>>> for i in range(m1.n):
#...     for j in range(m1.m):
#...             print(m1[i][j], end=' ')
#...
#1 1 1 1 1 1 >>>
#>>> m2.transpose
#3 3
#3 3
#3 3
#>>> m1 + m2
#4 4 4
#4 4 4
#>>> m1 - m2
#-2 -2 -2
#-2 -2 -2
#>>> 5 + m1
#6 6 6
#6 6 6
#>>>     6 6 6
#  File "<stdin>", line 1
#    6 6 6
#IndentationError: unexpected indent
#>>>     6 6 6
#  File "<stdin>", line 1
#    6 6 6
#IndentationError: unexpected indent
#>>> 5 + m1
#6 6 6
#6 6 6
#>>> 10 - m2
#7 7 7
#7 7 7
#>>> m1[0][2] = 7
#>>> m1[1][2] = 7
#>>>
#>>> m1
#1 1 7
#1 1 7
#>>> m1.transpose
#1 1
#1 1
#7 7
#>>>
#>>> m3 = Matrix([[1, 2], [3, 4]])
#>>> m3 + m1
#Traceback (most recent call last):
#  File "<stdin>", line 1, in <module>
#  File "C:\Git\Zotkina\2024.05.29\1.py", line 64, in __add__
#    return self.__element_wise_operation(other, lambda x, y: x + y)
#           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
#  File "C:\Git\Zotkina\2024.05.29\1.py", line 49, in __element_wise_operation
#    raise ValueError("сложение и вычитание возможно только для матриц одной размерности")
#ValueError: сложение и вычитание возможно только для матриц одной размерности
#>>> m3 + m1
#Traceback (most recent call last):
#  File "<stdin>", line 1, in <module>
#  File "C:\Git\Zotkina\2024.05.29\1.py", line 64, in __add__
#    return self.__element_wise_operation(other, lambda x, y: x + y)
#           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
#  File "C:\Git\Zotkina\2024.05.29\1.py", line 49, in __element_wise_operation
#    raise ValueError("сложение и вычитание возможно только для матриц одной размерности")
#ValueError: сложение и вычитание возможно только для матриц одной размерности
#>>>
#>>> m3 * 3.9
# 3.9  7.8
#11.7 15.6
#>>> -m3
#-1 -2
#-3 -4
#>>> m3 + [2, 1]
#Traceback (most recent call last):
#  File "<stdin>", line 1, in <module>
#  File "C:\Git\Zotkina\2024.05.29\1.py", line 64, in __add__
#    return self.__element_wise_operation(other, lambda x, y: x + y)
#           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
#  File "C:\Git\Zotkina\2024.05.29\1.py", line 60, in __element_wise_operation
#    raise TypeError("алгебраические операции возможны только с матрицами и числами")
#TypeError: алгебраические операции возможны только с матрицами и числами