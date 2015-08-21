__author__ = 'Chelsea | Michael'

import unittest
from Conect4_Model import Model
from unittest.mock import patch

class TestModelUpdateBoard(unittest.TestCase):

    def setUp(self):
        """ Init's current player and players"""
        self.theModel = Model()
        self.theModel.grid = []

    def tearDown(self):
        """ Closes the model """
        del self.theModel

    def test_update_board_first_list_append_0(self):
        """ take input from user and change index on board """
        self.theModel.update_board()
        self.currentBoard = self.theModel.make_board()
        self.currentBoard[0].append("x")
        self.assertEqual(self.currentBoard[0], ["x"])
        print(self.currentBoard)

if __name__ == '__main__':
    unittest.main()
