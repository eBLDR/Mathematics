""" A collection of matrix transformations and other properties. """

import tools
import random


def display(matrix: list, prompt: str) -> None:
    """ Display matrices nicely. """
    print(prompt)
    for row in matrix:
        for number in row:
            print(number, end=' ')
        print()


def sum_of_list(list_: list) -> int:
    """ Adds up all the elements in a list. """
    sum_ = 0
    for num in list_:
        sum_ = sum_ + num

    return sum_


def check_is_square(matrix: list) -> bool:
    """ Check if number of rows is equal to number of columns.
    It's assumed that the argument passed as matrix has at least 1 row containing 1 column. """
    if len(matrix) == len(matrix[0]):
        return True
    else:
        return False


def create_matrix_init():
    """ Collects needed data. """
    matrix_types = {'Null': 'null', 'Identity': 'identity', 'Known': 'known', 'Random': 'random'}
    type_ = matrix_types[tools.get_option(matrix_types)]
    rows = tools.get_integer("Number of rows: ")
    if type_ != 'identity':
        columns = tools.get_integer("Number of columns: ")
    else:
        columns = rows
    return create_matrix(rows, columns, type_)


def create_matrix(rows: int, columns: int, type_: str):
    """ Type can be: null / identity / known
    Null - full of 0.
    Identity - full of 0 except for the diagonal.
    Known - with given numbers.
    Random - random integers from 0 to 9"""
    matrix = []
    for r in range(rows):
        row = []
        for c in range(columns):
            if type_ == 'null':
                row.append(0)
            elif type_ == 'identity':
                if r == c:
                    row.append(1)
                else:
                    row.append(0)
            elif type_ == 'known':
                row.append(tools.get_integer("Element in row {} column {}: ".format(r+1, c+1)))
            elif type_ == 'random':
                row.append(random.randint(0, 9))
        matrix.append(row)

    prompt = "{} matrix of {} rows and {} columns:".format(type_, rows, columns)
    return matrix, prompt


def is_magic(matrix: list) -> bool:
    """ Is magic if the sum of all the items on each row, and each column, and each diagonal is equal. """
    # must be squared to be able to be magic
    is_square = check_is_square(matrix)
    if not is_square:
        return False

    list_of_sums = []
    # rows
    for row in matrix:
        list_of_sums.append(sum_of_list(row))

    # columns
    for i in range(len(matrix[0])):
        column = []
        for j in range(len(matrix)):
            column.append(matrix[j][i])
        list_of_sums.append(sum_of_list(column))

    # diagonals
    diagonal_1 = []  # from top left to bottom right
    diagonal_2 = []  # from top right to bottom left
    for i in range(len(matrix)):
        diagonal_1.append(matrix[i][i])
        diagonal_2.append(matrix[i][len(matrix)-1-i])

    list_of_sums.append(sum_of_list(diagonal_1))
    list_of_sums.append(sum_of_list(diagonal_2))

    # check if all the numbers in list_of_sums are equal
    reference_number = list_of_sums[0]  # we choose the first one as a reference

    for valor in list_of_sums[1:]:  # no need to compare to itself
        if valor != reference_number:
            return False
    else:
        return True


def main():
    option = tools.get_option(options_available)
    result, prompt = options_available[option]()
    display(result, prompt)


options_available = {'Create Matrix': create_matrix_init}

# to test stuff
if __name__ == '__main__':
    m, p = create_matrix(3, 3, 'known')
    print(m)
    display(m, p)
    print(is_magic(m))
