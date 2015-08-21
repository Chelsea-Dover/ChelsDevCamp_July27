__author__ = 'Chelsea'

import unittest
from itertools import zip_longest


class TestModelMakeBoard(unittest.TestCase):
    """make sure it prints an empty list"""

    def setUp(self):
        """Inits empty grid for testing"""
        self.grid = []


    def test_print_empty_list(self):
        """makes sure grid is empty"""

        self.assertEqual(0, len(self.grid), "len_should_be_zero")

    def test_append_item_to_list(self):
        """Append item to grid. Test grid length"""
        self.grid.append("x")

        self.assertEqual(1, len(self.grid))

    def update_board(self):

if __name__ == '__main__':
    unittest.main()
