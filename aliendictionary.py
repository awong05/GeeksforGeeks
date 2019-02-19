"""
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
"""

import unittest
from collections import defaultdict

class Graph(object):
    def __init__(self):
        self.adjacency_list = defaultdict(list)

    def add_edge(self, start, end):
        self.adjacency_list[start].append(end)

    def topological_sort(self):
        stack = []
        visited = defaultdict(bool)
        for k in [k for k in self.adjacency_list.keys()]:
            if not visited[k]:
                self.topological_sort_util(k, visited, stack)
        return stack[::-1]

    def topological_sort_util(self, k, visited, stack):
        visited[k] = True
        for v in self.adjacency_list[k]:
            if not visited[v]:
                self.topological_sort_util(v, visited, stack)
        stack.append(k)

def solution(D, K):
    graph = Graph()
    for i in range(len(D) - 1):
        first_word = D[i]
        second_word = D[i+1]
        for j in range(min(len(first_word), len(second_word))):
            if first_word[j] != second_word[j]:
                graph.add_edge(first_word[j], second_word[j])
                break
    return ''.join(graph.topological_sort())


class Test(unittest.TestCase):
    def test_large_sample(self):
        d = [
            'bf',
            'biifablhhfekcjfhdklefkiihffedfjkklldcbfdldddbf',
            'bikjidjifidghfklddjchiebjbibdjadlgji',
            'bkblijbgjbkillhcblbjacadceahebbcafichcjedhbajlfkei',
            'bldgbfhkfdbcihbdkfejkdgikeclih',
            'cbielkdheejdicfjfeclbdliidkdcfifdgehlleikkdb',
            'cccfckhbglgfi',
            'cjjgibfkgegchldfaclliejhhcbjickadahbcdkialldfb',
            'eclbbfcjdfecfdkiblddaceclddfkaabjgalgiggacjdegf',
            'efdjhebdfebhhccahifhaififjbadhc',
            'eghcflfgkllde',
            'eidbdkcjicecjaiddfdcjkfj',
            'ejifhhdiclkkejdhidkhbhjdihbdkckfkgiidhadjdje',
            'elacahafeeghdgkic',
            'fag',
            'fbeidhlbfhcbjebaegidflileilejkijdfjdkiclabdfjeejeg',
            'gebfadchbgcikgkfifaga',
            'gialjghjjhhedflkkdjlhajdkhdakhadkkajgllgllbghk',
            'helekchjgeb',
            'iehdjcjefggkcafllgedfhjhhiahgc',
            'ike',
            'ikgjliklfblbagfafe',
            'ilfeajblklchcebejiggjhfbdcla',
            'jdlfbhdfjbdblgcceihcgiaachlhlhjhcglhcaf',
            'jeahcekiahlkidflijakdj',
            'jfhgbkchhgckahefbjcgaceibkiehallgiffddchacigefa',
            'jhlfhckghgkgfb',
            'kfcahfciklbakdgehkgfadggdcjcfaijkjlffjf',
            'kiidkhfcclldfceahaabjfgdi',
            'kjbchgcbbdghhk',
            'lfkdjkkeebibdidhjfkldkhecllebheehjhcaileeggafii',
            'lhd',
            'lkkkldcfbfekbjdfalhiddaiegkf',
            'lljjjgj'
        ]
        k = 12

        actual = solution(d, k)
        expected = 'adbcefghijkl'

        self.assertEqual(actual, expected)

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
