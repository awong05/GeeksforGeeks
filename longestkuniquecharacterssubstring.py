import unittest

from collections import defaultdict

def find_substring_length(s, k):
    tracked_characters = defaultdict(set)
    substring_start = 0
    max_length = -1
    for i in range(len(s)):
        tracked_characters[s[i]].add(i)
        unique_characters_so_far = len(tracked_characters.keys())
        if unique_characters_so_far == k:
            max_length = max(max_length, i - substring_start + 1)
        elif unique_characters_so_far > k:
            while len(tracked_characters.keys()) != k:
                first_character_in_substring = s[substring_start]
                tracked_characters[first_character_in_substring].remove(substring_start)
                if not len(tracked_characters[first_character_in_substring]):
                    del tracked_characters[first_character_in_substring]
                substring_start += 1
    return max_length

class Test(unittest.TestCase):
    def test_small_sample(self):
        actual = find_substring_length('nwnk', 1)
        expected = 1
        self.assertEqual(actual, expected)

    def test_large_sample(self):
        actual = find_substring_length('wlrbbmqbhcdarzowkkyhiddqscdxrjmowfrxsjybldbefsarcbynecdyggxxpklorellnmpapqfwkhopkmco', 5)
        expected = 7
        self.assertEqual(actual, expected)

unittest.main(verbosity=2)
