import unittest

def solution(M, N):
    A = {0}
    B = 0
    for _ in range(N):
        C = sorted(M[B])[1]
        for i, v in enumerate(M[B]):
            if i not in A and v == C:
                for j in range(N):
                    if i == j:
                        continue
                    M[i][j] += C
                A.add(i)
                B = i
                break
    return M[B][0]

class Test(unittest.TestCase):
    def test_small_example(self):
        N = 2
        M = [
            [0, 111],
            [112, 0]
        ]

        actual = solution(M, N)
        expected = 223

        self.assertEqual(actual, expected)

    def test_medium_example(self):
        N = 3
        M = [
            [0, 1000, 5000],
            [5000, 0, 1000],
            [1000, 5000, 0]
        ]

        actual = solution(M, N)
        expected = 3000

        self.assertEqual(actual, expected)

unittest.main(verbosity=2)
