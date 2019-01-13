import unittest

def explore_node(arr, l, w, x, y):
    arr[x][y] = 'Visited'
    if 0 <= x < l - 1 and arr[x + 1][y] == 'X':
        explore_node(arr, l, w, x + 1, y)
    if 0 <= y < w - 1 and arr[x][y + 1] == 'X':
        explore_node(arr, l, w, x, y + 1)
    if 0 < x < l and arr[x - 1][y] == 'X':
        explore_node(arr, l, w, x - 1, y)
    if 0 < y < w and arr[x][y - 1] == 'X':
        explore_node(arr, l, w, x, y - 1)

def count_x_shapes(arr):
    n = len(arr)
    m = len(arr[0])
    count = 0
    for x in range(n):
        for y in range(m):
            node = arr[x][y]
            if node == 'X':
                count += 1
                explore_node(arr, n, m, x, y)
    return count

class Test(unittest.TestCase):
    def test_small_list(self):
        input_matrix = [
            ['O', 'O', 'O', 'O', 'X', 'X', 'O'],
            ['O', 'X', 'O', 'X', 'O', 'O', 'X'],
            ['X', 'X', 'X', 'X', 'O', 'X', 'O'],
            ['O', 'X', 'X', 'X', 'O', 'O', 'O']
        ]
        actual = count_x_shapes(input_matrix)
        expected = 4
        self.assertEqual(actual, expected)

    def test_medium_list(self):
        input_matrix = [
            ['X', 'X', 'O'],
            ['O', 'O', 'X'],
            ['O', 'X', 'O'],
            ['O', 'O', 'O'],
            ['X', 'O', 'X'],
            ['X', 'O', 'X'],
            ['O', 'X', 'O'],
            ['X', 'X', 'O'],
            ['X', 'X', 'X'],
            ['O', 'O', 'O']
        ]
        actual = count_x_shapes(input_matrix)
        expected = 6
        self.assertEqual(actual, expected)

    def test_large_list(self):
        input_matrix = [
            ['X', 'O', 'X', 'O', 'O', 'O', 'X', 'O'],
            ['X', 'O', 'X', 'O', 'X', 'X', 'O', 'X'],
            ['O', 'X', 'X', 'X', 'X', 'X', 'O', 'O'],
            ['X', 'O', 'X', 'X', 'X', 'X', 'O', 'X'],
            ['X', 'X', 'X', 'O', 'O', 'X', 'X', 'X']
        ]
        actual = count_x_shapes(input_matrix)
        expected = 4
        self.assertEqual(actual, expected)

unittest.main(verbosity=2)
