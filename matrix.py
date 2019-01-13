# TODO: Improve this using memoization.

import unittest

def check_for_duplicate_in_row(matrix, value, x, y):
    for i in range(9):
        if i == y:
            continue
        if matrix[x][i] == value:
            return True
    return False

def check_for_duplicate_in_column(matrix, value, x, y):
    for i in range(9):
        if i == x:
            continue
        if matrix[i][y] == value:
            return True
    return False

def is_valid_sudoku_configuration(matrix):
    for x in range(9):
        for y in range(9):
            c = matrix[x][y]
            if c == 0:
                continue
            if check_for_duplicate_in_row(matrix, c, x, y) or \
                check_for_duplicate_in_column(matrix, c, x, y):
                return 0
    return 1

class Test(unittest.TestCase):
    def test_example_matrix(self):
        example_matrix = [
            [3, 0, 6, 5, 0, 8, 4, 0, 0],
            [5, 2, 0, 0, 0, 0, 0, 0, 0],
            [0, 8, 7, 0, 0, 0, 0, 3, 1],
            [0, 0, 3, 0, 1, 0, 0, 8, 0],
            [9, 0, 0, 8, 6, 3, 0, 0, 5],
            [0, 5, 0, 0, 9, 0, 6, 0, 0],
            [1, 3, 0, 0, 0, 0, 2, 5, 0],
            [0, 0, 0, 0, 0, 0, 0, 7, 4],
            [0, 0, 5, 2, 0, 6, 3, 0, 0]
        ]

        actual = is_valid_sudoku_configuration(example_matrix)
        expected = 1
        self.assertEqual(actual, expected)

unittest.main(verbosity=2)
