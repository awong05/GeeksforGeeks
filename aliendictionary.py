import unittest

def find_first_set_of_differing_characters(A, B):
    a_index = b_index = 0
    a_character = A[a_index]
    b_character = B[b_index]
    while a_character == b_character:
        a_index += 1
        b_index += 1
        a_character = A[a_index]
        b_character = B[b_index]
    return (a_character, b_character)

def solution(D, K):
    ordering = []
    all_possible_characters = {character: set() for word in D for character in word}

    for i in range(len(D) - 1):
        f, t = find_first_set_of_differing_characters(D[i], D[i+1])
        all_possible_characters[f].add(t)

    for k, v in all_possible_characters.items():
        if k not in ordering:
            ordering.append(k)
        k_index = ordering.index(k)
        for j in v:
            if j not in ordering:
                ordering.insert(k_index+1, j)
                continue
            j_index = ordering.index(j)
            if j_index < k_index:
                ordering = ordering[:j_index] + ordering[k_index:] + ordering[j_index:k_index]

    return ''.join(ordering)

class Test(unittest.TestCase):
    def test_medium_sample(self):
        d = ['baa', 'abcd', 'abca', 'cab', 'cad']
        k = 4

        actual = solution(d, k)
        expected = 'bdac'

        self.assertEqual(actual, expected)

    def test_small_sample(self):
        d = ['caa', 'aaa', 'aab']
        k = 3

        actual = solution(d, k)
        expected = 'cab'

        self.assertEqual(actual, expected)

unittest.main(verbosity=2)
