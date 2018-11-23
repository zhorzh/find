import unittest


def find_number(list_of_integers):
    counters = {}
    for index, item in enumerate(list_of_integers):
        if item in counters.keys():
            if counters[item] == 2:
                return item
            counters[item] += 1
        else:
            counters[item] = 1
    else:
        return None


class TestFindNumber(unittest.TestCase):
    def test_initial_list(self):
        test_list = [1, 8, 4, 6, 7, 3, 27, 42, 33, 5, 9, 7, 58, 9, 7, 85, 0, 1]
        self.assertEqual(find_number(test_list), 7)

    def test_two_numbers(self):
        test_list = [0, 1, 2, 1, 2, 1, 2, 0]
        self.assertEqual(find_number(test_list), 1)

    def test_empty_list(self):
        test_list = []
        self.assertEqual(find_number(test_list), None)

    def test_none(self):
        test_list = [1, 2, 3]
        self.assertEqual(find_number(test_list), None)


if __name__ == '__main__':
    unittest.main()
