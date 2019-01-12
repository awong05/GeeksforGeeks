import unittest

def rotate_matrix_in_place(matrix):
    width = len(matrix)
    boundary = width - 1
    for lower_boundary in range(int(width / 2)):
        upper_boundary = boundary - lower_boundary
        for idx in range(lower_boundary, upper_boundary):
            matrix[lower_boundary][idx], matrix[idx][upper_boundary], matrix[upper_boundary][boundary - idx], matrix[boundary - idx][lower_boundary] = \
                matrix[boundary - idx][lower_boundary], matrix[lower_boundary][idx], matrix[idx][upper_boundary], matrix[upper_boundary][boundary - idx]

class Test(unittest.TestCase):
    def test_medium_list(self):
        input_matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        rotate_matrix_in_place(input_matrix)
        expected = [[7, 4, 1], [8, 5, 2], [9, 6, 3]]
        self.assertEqual(input_matrix, expected)

unittest.main(verbosity=2)
