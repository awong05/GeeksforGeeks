# TODO: Don't brute force this.

import unittest

def has_zero_sum_triplet(arr):
    for x in range(len(arr)):
        for y in range(len(arr)):
            for z in range(len(arr)):
                if arr[x] + arr[y] + arr[z] == 0 and x != y and x != z and y != z:
                    return 1
    return 0

class Test(unittest.TestCase):
    def test_example_input(self):
        example_input = [49, -73, 33, -47, 97, -96, 67, 6, 81, -24, 26, 73, 38, -24, 94, 7, 72, -6]
        actual = has_zero_sum_triplet(example_input)
        expected = 1
        self.assertEqual(actual, expected)

unittest.main(verbosity=2)
