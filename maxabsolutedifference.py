import unittest

def max_absolute_difference(A, N):
    min_ending_here = max_ending_here = min_so_far = max_so_far = A[0]
    for x in A[1:]:
        min_ending_here = min(x, min_ending_here + x)
        max_ending_here = max(x, max_ending_here + x)
        min_so_far = min(min_so_far, min_ending_here)
        max_so_far = max(max_so_far, max_ending_here)
    return abs(max_so_far - min_so_far)

class Test(unittest.TestCase):
    def test_small_sample(self):
        actual = max_absolute_difference([-2, -3, 4, -1, -2, 1, 5, -3], 8)
        expected = 12

        self.assertEqual(actual, expected)

    def test_medium_sample(self):
        actual = max_absolute_difference([2, -1, -2, 1, -4, 2, 8], 7)
        expected = 16

        self.assertEqual(actual, expected)

    def test_large_sample(self):
        actual = max_absolute_difference([778, -794, -387, 650, -363, -691, -764, 541, 173, 212, 568, -783, 863, -68, -930, 23, 70, -394, 12, 230, -422, -785, -199, 316, 414, 92, 957, -863, 997, -306, -85, -337, -847, -314, -125, -583, -815, -435, 44, 88, 277, 789, 404, -755, -933, 677, 740, 227, 95, -796, 435, 468, -98, 318, 653, 302, 287, -866, -445, -441, -32, -98, -482, -710, -568, 498, -587, -307, -220, 529, -733, -504, -271, 709, -341, -797, -619, -847, -922, -380, 765, 842, 194, 35], 84)
        expected = 12220

        self.assertEqual(actual, expected)

unittest.main(verbosity=2)
