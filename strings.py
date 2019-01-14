import unittest

def get_largest_word(d, s):
    match = ''
    for word in d:
        if len(word) > len(s):
            continue
        word_scanner, s_scanner = 0, 0
        while word_scanner < len(word) and s_scanner < len(s):
            if s[s_scanner] != word[word_scanner]:
                s_scanner += 1
            else:
                s_scanner += 1
                word_scanner += 1
        if word_scanner == len(word):
            if len(word) > len(match):
                match = word
        if s_scanner == len(s):
            continue
    return match


class Test(unittest.TestCase):

    def test_small_dict(self):
        small_dict = ['ale', 'apple', 'monkey', 'plea']
        small_str = 'abpcplea'

        actual = get_largest_word(small_dict, small_str)
        expected = 'apple'

        self.assertEqual(actual, expected)

    def test_medium_dict(self):
        medium_dict = ['pintu', 'geeksfor', 'geeksgeeks', 'forgeek']
        medium_str = 'geeksforgeeks'

        actual = get_largest_word(medium_dict, medium_str)
        expected = 'geeksgeeks'

        self.assertEqual(actual, expected)

unittest.main(verbosity=2)
