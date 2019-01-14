import unittest

def count_of_distinct_transformations(A, B):
    return 0

class Test(unittest.TestCase):
    def test_with_first_example(self):
        A = 'nkccccbbbuewhsqm'
        B = 'nkuewhsqm'
        actual = count_of_distinct_transformations(A, B)
        expected = 1
        self.assertEqual(actual, expected)

    def test_with_second_example(self):
        A = 'wlrrrrbaakkaabmqbpphcdarzoccccwxllllxkkhhhhyllhiyyyyddqsbbppbcdqqxrjkkmoeeeewfrxseeej'
        B = 'wlrbbmqbhcdarzowkkyhiddqscdxrjmowfrxsj'
        actual = count_of_distinct_transformations(A, B)
        expected = 4
        self.assertEqual(actual, expected)

unittest.main(verbosity=2)
