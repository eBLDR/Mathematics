""" A collection of matrix transformations and other properties. """
import random
from typing import Union


class Matrix:
    def __init__(
            self,
            number_of_rows: int,
            number_of_columns: int,
            element_value: Union[int, float, complex] = None,
            choices_value: tuple = tuple(range(0, 9)),
    ):
        self.number_of_rows = number_of_rows
        self.number_of_columns = number_of_columns
        self.entries: list[list] = [[]]
        self._generate(
            element_value=element_value,
            choices_value=choices_value,
        )

    def __str__(self):
        """
        a1 a2 . . . an
        b1 b2 . . . bn
        .  .  . . . .
        .  .  . . . .
        .  .  . . . .
        n1 n2 . . . nn
        """
        # return "\n".join([" ".join([str(element) for element in row]) for row in self.entries])
        return "\n".join([" ".join(map(str, row)) for row in self.entries])

    def _generate(self, element_value: Union[int, float, complex] = None, choices_value: tuple = None):
        self.entries = [
            [element_value for _ in range(self.number_of_columns)]
            if element_value
            else random.choices(choices_value, k=self.number_of_columns)
            for _ in range(self.number_of_rows)
        ]

    @property
    def dimension(self) -> tuple[int, int]:
        """
        Returns matrix's dimensions.
        :return: (m, n)
        """
        return self.number_of_rows, self.number_of_columns

    def is_square(self) -> bool:
        """ Check if number of rows is equal to number of columns. """
        return self.number_of_rows == self.number_of_columns

    def is_magic(self) -> bool:
        """ Is magic if the sum of all the items on each row, each column,
        and each diagonal is equal. """
        if not self.is_square():
            return False

        reference_number = None

        # Checking rows
        for row in self.entries:
            if sum(row) != reference_number:
                return False

        # Checking columns
        for i in range(self.number_of_columns):
            if sum([self.entries[j][i] for j in range(self.number_of_rows)]) != reference_number:
                return False

        # Checking diagonals
        if (
                # Top left to bottom right
                sum([self.entries[i][i] for i in range(self.number_of_rows)]) != reference_number != reference_number
                or
                # Top right to bottom left
                sum([self.entries[i][len(self.entries) - 1 - i] for i in range(self.number_of_rows)]) != reference_number
        ):
            return False

        return True

    # Operations
    def transpose(self):
        self.entries = list(list(row) for row in zip(*self.entries))

    def matrix_addition(self, matrix):
        if self.dimension != matrix.dimension:
            raise Exception("Both matrices should have the same dimension.")

        self.entries = [
            map(sum, zip(*rows))
            for rows in zip(self.entries, matrix.entries)
        ]

    def scalar_product(self, k: Union[int, float, complex]):
        self.entries = [
            [element * k for element in row]
            for row in self.entries
        ]


class NullMatrix(Matrix):
    def __init__(self, number_of_rows: int, number_of_columns: int):
        super().__init__(
            number_of_rows=number_of_rows,
            number_of_columns=number_of_columns,
            element_value=0,
        )


class IdentityMatrix(Matrix):
    ...


def dot_product(matrix_1: list, matrix_2: list) -> list:
    """
    Dot product.
    """
    matrix_result = []

    for row_index in range(len(matrix_1)):
        row_result = []

        for column_index in range(len(matrix_1[row_index])):
            value = 0

            for operand in range(len(matrix_1[row_index])):
                value += matrix_1[row_index][operand] * matrix_2[operand][column_index]

            row_result.append(value)

    return matrix_result
