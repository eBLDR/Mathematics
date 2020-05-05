""" A collection of matrix transformations and other properties. """
import random

import tools


def display(matrix: list, prompt: str) -> None:
    """ Display matrices nicely. """
    print(prompt)
    for row in matrix:
        for number in row:
            print(number, end=' ')
        print()


def get_dimensions(matrix: list) -> tuple:
    """
    Calculates matrix's dimensions:
        m -> number of rows
        n -> number of columns
    :return: (m, n)
    """
    return len(matrix), len(matrix[0])


def is_square(matrix: list) -> bool:
    """ Check if number of rows is equal to number of columns. """
    return len(matrix) == len(matrix[0])


def create_matrix_init():
    """ Collects needed data. """
    matrix_types = {
        'Null': 'null',
        'Identity': 'identity',
        'Known': 'known',
        'Random': 'random',
    }

    type_ = matrix_types[tools.get_option(matrix_types)]
    rows = tools.get_integer('Number of rows: ')
    columns = rows if type_ != 'identity' else tools.get_integer('Number of columns: ')

    return create_matrix(rows, columns, type_)


def create_matrix(rows: int, columns: int, type_: str):
    """ Type can be: null / identity / known
    Null - full of 0.
    Identity - full of 0 except for the diagonal.
    Known - with given numbers.
    Random - random integers from 0 to 9
    """
    matrix = []

    for r in range(rows):
        row = []

        for c in range(columns):
            if type_ == 'null':
                row.append(0)
            elif type_ == 'identity':
                row.append(1) if r == c else row.append(0)
            elif type_ == 'known':
                row.append(tools.get_integer(f'Element in row {r + 1} column {c + 1}: '))
            elif type_ == 'random':
                row.append(random.randint(0, 9))

        matrix.append(row)

    prompt = f'{type_} matrix of {rows} rows and {columns} columns: '

    return matrix, prompt


def addition(matrix_1: list, matrix_2: list) -> list:
    """
    Matrix addition.
    """
    if get_dimensions(matrix_1) == get_dimensions(matrix_2):
        raise Exception('Both matrices should have the same dimension.')

    matrix_result = []

    for row_1, row_2 in zip(matrix_1, matrix_2):
        matrix_result.append(
            [
                number_1 + number_2 for number_1, number_2 in zip(row_1, row_2)

            ]
        )

    return matrix_result


def scalar_product(matrix: list, scalar: int) -> list:
    """
    Scalar product.
    """
    matrix_result = []

    for row in matrix:
        matrix_result.append(
            [
                number * scalar for number in row
            ]
        )

    return matrix_result


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


def is_magic(matrix: list) -> bool:
    """ Is magic if the sum of all the items on each row, and each column,
    and each diagonal is equal. """
    if not is_square(matrix):
        return False

    list_of_sums = []

    # Checking rows
    for row in matrix:
        list_of_sums.append(sum(row))

    # Checking columns
    for i in range(len(matrix[0])):
        column = []
        for j in range(len(matrix)):
            column.append(matrix[j][i])
        list_of_sums.append(sum(column))

    # Checking diagonals
    diagonal_1 = []  # Top left to bottom right
    diagonal_2 = []  # Top right to bottom left

    for i in range(len(matrix)):
        diagonal_1.append(matrix[i][i])
        diagonal_2.append(matrix[i][len(matrix) - 1 - i])

    list_of_sums.append(sum(diagonal_1))
    list_of_sums.append(sum(diagonal_2))

    # Check if all the numbers in list_of_sums are equal
    reference_number = list_of_sums[0]

    for value in list_of_sums[1:]:
        if value != reference_number:
            return False
    else:
        return True


def main():
    option = tools.get_option(options_available)
    result, prompt = options_available[option]()
    display(result, prompt)


options_available = {
    'Create Matrix': create_matrix_init,
}

# to test stuff
if __name__ == '__main__':
    m, p = create_matrix(3, 3, 'known')
    print(m)
    display(m, p)
    print(is_magic(m))
