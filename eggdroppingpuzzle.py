import unittest

def minimum_attempts_needed(N, K):
    matrix = [[0 for _ in range(K + 1)] for _ in range(N + 1)]
    for idx in range(1, N + 1):
        matrix[idx][1] = 1
    for idx in range(1, K + 1):
        matrix[1][idx] = idx
    for n in range(2, N + 1):
        for k in range(2, K + 1):
            matrix[n][k] = float('inf')
            for x in range(1, k + 1):
                matrix[n][k] = min(matrix[n][k], 1 + max(matrix[n - 1][x - 1], matrix[n][k - x]))
    return matrix[N][K]

class Test(unittest.TestCase):
    def test_medium_sample(self):
        n = 2
        k = 100

        actual = minimum_attempts_needed(n, k)
        expected = 14

        self.assertEqual(actual, expected)

unittest.main(verbosity=2)
