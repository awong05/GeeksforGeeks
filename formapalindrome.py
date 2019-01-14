import unittest

def minimum_insertions_needed(sample_string, memo={}, level=0):
    if sample_string in memo and memo[sample_string] == level:
        return memo[sample_string]
    if sample_string == sample_string[::-1]:
        memo[sample_string] = level
        return level
    if sample_string[0] == sample_string[-1]:
        memo[sample_string] = minimum_insertions_needed(sample_string[1:-1], memo, level)
        return memo[sample_string]
    memo[sample_string] = min(
        minimum_insertions_needed(sample_string[1:], memo, level + 1),
        minimum_insertions_needed(sample_string[:-1], memo, level + 1)
    )
    return memo[sample_string]

class Test(unittest.TestCase):
    def test_first_sample(self):
        first_sample = 'abcd'

        actual = minimum_insertions_needed(first_sample)
        expected = 3

        self.assertEqual(actual, expected)

    def test_second_sample(self):
        first_sample = 'aba'

        actual = minimum_insertions_needed(first_sample)
        expected = 0

        self.assertEqual(actual, expected)

    def test_third_sample(self):
        first_sample = 'geeks'

        actual = minimum_insertions_needed(first_sample)
        expected = 3

        self.assertEqual(actual, expected)

    def test_less_complicated_sample(self):
        first_sample = 'india'

        actual = minimum_insertions_needed(first_sample)
        expected = 2

        self.assertEqual(actual, expected)

    def test_complicated_sample(self):
        first_sample = 'helppreanadkada'

        actual = minimum_insertions_needed(first_sample)
        expected = 10

        self.assertEqual(actual, expected)

    def test_more_complicated_sample(self):
        first_sample = 'justintumblera'

        actual = minimum_insertions_needed(first_sample)
        expected = 9

        self.assertEqual(actual, expected)

unittest.main(verbosity=2)
