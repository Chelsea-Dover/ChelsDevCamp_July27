__author__ = 'Chelsea | Michael'

import unittest
from Conect4_Model import Model


class TestModelMakeBoard(unittest.TestCase):
    """make sure it prints an empty list"""

    def setUp(self):
        """Inits empty grid for testing"""
        self.grid = []
        self.test_grid = Model()

    def tearDown(self):
        """ Closes the model """
        del self.test_grid

    def test_print_empty_list(self):
        """makes sure grid is empty"""

        self.assertEqual(0, len(self.test_grid.grid), "len_should_be_zero")

    def test_append_item_to_list(self):
        """Append item to grid. Test grid length"""
        self.grid.append("x")

        self.assertEqual(1, len(self.grid))
    #
    # def test_make_row(self):
    #     """Appends whole row to grid"""
    #     for row in range(7):
    #         self.grid.append("_")
    #
    #     res = "|".join(self.grid)
    #
    #     #print(res)
    #
    #     self.assertEqual(7, len(self.grid))

    def test_make_board(self):
        """Appends whole board to grid"""
        self.test_grid.make_board()

        self.assertEqual(48, len(self.test_grid.grid))

if __name__ == '__main__':
    unittest.main()
