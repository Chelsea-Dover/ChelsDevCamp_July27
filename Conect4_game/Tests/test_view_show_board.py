__author__ = 'Chelsea | Michael'

import unittest
from Conect4_View import View
from unittest.mock import patch
from io import StringIO


class TestViewShowBoard(unittest.TestCase):
    """make sure it prints an empty list"""

    def setUp(self):
        """Inits empty grid for testing"""
        self.theView = View()

    def tearDown(self):
        """ Closes the view """
        del self.theView

    @patch('sys.stdout', new_callable=StringIO)
    def show_the_board(self, mock_stdout):
        """visually represent the grid as a connect 4 game """
         currentBoard =
 1234567
-----------------------------
|   |   |   |   |   |   |   |
-----------------------------
|   |   |   |   |   |   |   |
-----------------------------
|   |   |   |   |   |   |   |
-----------------------------
|   |   |   |   |   |   |   |
-----------------------------
|   |   |   |   |   |   |   |
-----------------------------
|   |   |   |   |   |   |   |
-----------------------------

        self.assertEqual(mock_stdout.getvalue(), currentBoard)
        # self.assertEqual(self.angry_game.current_stage, 1)


   def test_show_the_board(self):
       """ visually represent the grid as a connect 4 game """
       self.theView.show_board()
