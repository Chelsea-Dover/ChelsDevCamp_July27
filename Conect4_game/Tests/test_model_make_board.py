__author__ = 'Chelsea | Michael'

import unittest
from Conect4_Model import Model


class TestModelMakeBoard(unittest.TestCase):
    """make sure it prints an empty list"""

    def setUp(self):
        """Inits empty grid for testing"""
        self.test_grid = Model()

    def tearDown(self):
        """ Closes the model """
        del self.test_grid

    def test_make_board_length_7(self):
        """makes sure grid is empty"""
        self.assertEqual(7, len(self.test_grid.grid), "len_should_be_seven")

    def test_make_board_inner_list_length_6(self):
        """ confirms the zero index length equal to 6 """
        self.assertEqual(6, len(self.test_grid.grid[0]))


if __name__ == '__main__':
    unittest.main()
