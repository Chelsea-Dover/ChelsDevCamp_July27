__author__ = 'Chelsea | Michael'

import unittest
from Conect4_Model import Model
from unittest.mock import patch
from io import StringIO


class TestModelMakeBoard(unittest.TestCase):
    """make sure it prints an empty list"""

    def setUp(self):
        """Inits empty grid for testing"""
        self.theModel = Model()

    def tearDown(self):
        """ Closes the view """
        del self.test_grid

    @patch('sys.stdout', new_callable=StringIO)
    def show_the_board(self, mock_stdout):
        """ visually represent the grid as a connect 4 game """
        # self.currentBoard =

        self.assertEqual(mock_stdout.getvalue(), currentBoard)
        # self.assertEqual(self.angry_game.current_stage, 1)