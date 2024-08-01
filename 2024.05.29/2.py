from collections.abc import Iterable
from numbers import Number
from typing import Callable, Self
from functools import cached_property, cache

class Matrix:
    def __init__(self, *raw_matrix: Number, n: int, m: int):
        if not self.is_valid(raw_matrix, n, m):
            raise ValueError("невозможно сконструировать матрицу")
        
        self.__flat = tuple(raw_matrix)
        self.n = n
        self.m = m

    @staticmethod
    def is_valid(processed_matrix: Iterable[Number], n: int, m: int) -> bool:
        if len(processed_matrix) != n * m:
            return False
        return all(isinstance(num, Number) for num in processed_matrix)

    @cached_property
    def transpose(self) -> Self:
        transposed_elements = [self.__flat[j * self.m + i] for i in range(self.m) for j in range(self.n)]
        return Matrix(*transposed_elements, n=self.m, m=self.n)

    def __element_wise_operation(self, other: Self | Number, operation: Callable[[Number, Number], Number]) -> Self:
        if isinstance(other, Matrix):
            if self.n != other.n or self.m != other.m:
                raise ValueError("сложение и вычитание возможно только для матриц одной размерности")
            result_elements = tuple(operation(a, b) for a, b in zip(self.__flat, other.__flat))
        elif isinstance(other, Number):
            result_elements = tuple(operation(a, other) for a in self.__flat)
        else:
            raise TypeError("алгебраические операции возможны только с матрицами и числами")
        return Matrix(*result_elements, n=self.n, m=self.m)

    def __add__(self, other: Self | Number) -> Self:
        return self.__element_wise_operation(other, lambda x, y: x + y)

    def __radd__(self, other: Number) -> Self:
        return self.__add__(other)

    def __neg__(self) -> Self:
        return self.__mul__(-1)

    def __sub__(self, other: Self | Number) -> Self:
        return self.__element_wise_operation(other, lambda x, y: x - y)

    def __rsub__(self, other: Number) -> Self:
        return self.__element_wise_operation(other, lambda x, y: y - x)

    def __mul__(self, other: Number) -> Self:
        if isinstance(other, Number):
            return self.__element_wise_operation(other, lambda x, y: x * y)
        raise NotImplementedError("умножение матриц будет реализовано в будущем")

    def __rmul__(self, other: Number) -> Self:
        return self.__mul__(other)

    @cache
    def __repr__(self) -> str:
        col_widths = [
            max(len(str(self.__flat[i * self.m + j])) for i in range(self.n))
            for j in range(self.m)
        ]
        matrix_str = "\n".join(
            " ".join(
                f"{str(self.__flat[i * self.m + j]).rjust(col_widths[j])}"
                for j in range(self.m)
            ) for i in range(self.n)
        )
        return matrix_str
#Примеры теста:
#>>> Matrix(1, 2, 3, 4, 5, n=2, m=3)
#Traceback (most recent call last):
#  File "<stdin>", line 1, in <module>
#  File "C:\Git\Zotkina\2024.05.29\2.py", line 9, in __init__
#    raise ValueError("невозможно сконструировать матрицу")
#ValueError: невозможно сконструировать матрицу
#>>> from itertools import repeat
#>>> m1 = Matrix(*repeat(1, 15), n=3, m=5)
#>>> m2 = Matrix(*range(1, 16), n=3, m=5)
#>>> m1
#1 1 1 1 1
#1 1 1 1 1
#1 1 1 1 1
#>>> m2
# 1  2  3  4  5
# 6  7  8  9 10
#11 12 13 14 15
#>>> m1[0][0]
#Traceback (most recent call last):
#  File "<stdin>", line 1, in <module>
#TypeError: 'Matrix' object is not subscriptable
#>>> m2.transpose
#1  6 11
#2  7 12
#3  8 13
#4  9 14
#5 10 15
#>>> m1 + m1
#2 2 2 2 2
#2 2 2 2 2
#2 2 2 2 2
#>>> m2 - m1
# 0  1  2  3  4
# 5  6  7  8  9
#10 11 12 13 14
#>>> m1 * m2
#Traceback (most recent call last):
#  File "<stdin>", line 1, in <module>
#  File "C:\Git\Zotkina\2024.05.29\2.py", line 55, in __mul__
#    raise NotImplementedError("умножение матриц будет реализовано в будущем")
#NotImplementedError: умножение матриц будет реализовано в будущем
#>>> 3 + m1
#4 4 4 4 4
#4 4 4 4 4
#4 4 4 4 4
#>>> m2.transpose - 10
#-9 -4 1
#-8 -3 2
#-7 -2 3
#-6 -1 4
#-5  0 5
#>>> -1.5 - m1
#-2.5 -2.5 -2.5 -2.5 -2.5
#-2.5 -2.5 -2.5 -2.5 -2.5
#-2.5 -2.5 -2.5 -2.5 -2.5
#>>> m3 + m1
#Traceback (most recent call last):
#  File "<stdin>", line 1, in <module>
#NameError: name 'm3' is not defined. Did you mean: 'm1'?
#>>> m3 = Matrix(*range(1, 5), n=2, m=2)
#>>> m3
#1 2
#3 4
#>>> m3 * 4.5
# 4.5  9.0
#13.5 18.0
#>>> -m3
#-1 -2
#-3 -4
#>>> m3 - [4, 3, 2, 1]
#Traceback (most recent call last):
#  File "<stdin>", line 1, in <module>
#  File "C:\Git\Zotkina\2024.05.29\2.py", line 47, in __sub__
#    return self.__element_wise_operation(other, lambda x, y: x - y)
#           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
#  File "C:\Git\Zotkina\2024.05.29\2.py", line 34, in __element_wise_operation
#    raise TypeError("алгебраические операции возможны только с матрицами и числами")
#TypeError: алгебраические операции возможны только с матрицами и числами
#>>>

