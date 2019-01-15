import unittest

def target_segmentable(dictionary, string):
    if string == '':
        return True
    for word in dictionary:
        if not string.startswith(word):
            continue
        if target_segmentable(dictionary, string[len(word):]):
            return True
    return False



class Test(unittest.TestCase):
    def test_small_sample(self):
        words_in_dictionary = ['lrbbmqb', 'cd', 'r', 'owkk']
        target_string = 'lrbbmqbabowkkab'

        actual = target_segmentable(words_in_dictionary, target_string)
        expected = 0

        self.assertEqual(actual, expected)

    def test_medium_sample(self):
        words_in_dictionary = [
            'scd',
            'rjmowfrx',
            'jybldbe',
            'sarcbyne',
            'dyggxxp',
            'lorel',
            'nmpa',
            'qfwkho',
            'kmcoqhnw',
            'kuewhsqmgb'
        ]
        target_string = 'dyggxxp'

        actual = target_segmentable(words_in_dictionary, target_string)
        expected = 1

        self.assertEqual(actual, expected)

unittest.main(verbosity=2)
