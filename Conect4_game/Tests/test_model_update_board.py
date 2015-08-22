__author__ = 'Chelsea | Michael'

import unittest
from Conect4_Model import Model
from unittest.mock import patch

class TestModelUpdateBoard(unittest.TestCase):

    def setUp(self):
        """ Init's current player and players"""
        self.model = Model()
        self.model.grid = []

    def tearDown(self):
        """ Closes the model """
        del self.model

    def test_update_board_first_list_append_0(self):
        """ take input from user and change index on board """

        self.player_input = "1"

        self.model.update_board()
        self.assertEqual(self.model.test[int(self.player_input)][0], "x")


if __name__ == '__main__':
    unittest.main()
