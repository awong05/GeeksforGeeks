import unittest

def find_largest_value(weight_limit, values, weights):
    values_for_weights = [0] * (weight_limit + 1)
    for value, weight in zip(values, weights):
        for idx, v in enumerate(values_for_weights):
            if weight > idx:
                continue
            values_for_weights[idx] = max(v, values_for_weights[idx - weight] + value)
    return values_for_weights[weight_limit]

class Test(unittest.TestCase):
    def test_small_example(self):
        weight_limit = 3
        values = [1, 1]
        weights = [2, 1]

        actual = find_largest_value(weight_limit, values, weights)
        expected = 3

        self.assertEqual(actual, expected)

    def test_medium_example(self):
        weight_limit = 8
        values = [1, 4, 5, 7]
        weights = [1, 3, 4, 5]

        actual = find_largest_value(weight_limit, values, weights)
        expected = 11

        self.assertEqual(actual, expected)

unittest.main(verbosity=2)
