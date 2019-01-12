import unittest
from collections import deque

def count_x_shapes(arr):
    count = 0
    height = len(arr)
    width = len(arr[0])
    q = deque([(0, 0)])
    while len(q):
        x, y = q.popleft()

        left_neighbor_is_an_x = False
        right_neighbor_is_an_x = False

        if x < height - 1 and y == 0:
            q.append((x + 1, y))
        if y < width - 1:
            q.append((x, y + 1))

        if x + 1 < height and arr[x + 1][y] == 'X':
            left_neighbor_is_an_x = True
        if y + 1 < width and arr[x][y + 1] == 'X':
            right_neighbor_is_an_x = True

        if arr[x][y] == 'X' and not left_neighbor_is_an_x and not right_neighbor_is_an_x:
            count += 1

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

unittest.main(verbosity=2)
