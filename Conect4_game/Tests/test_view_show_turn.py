__author__ = 'Chelsea | Michael'

import unittest
from Conect4_View import View
from unittest.mock import patch
from io import StringIO


class TestModelShowTurn(unittest.TestCase):
    """make sure it prints an empty list"""

    def setUp(self):
        """Inits empty grid for testing"""
        self.theView = View()

    def tearDown(self):
        """ Closes the view """
        del self.theView

    def test_show_turn_player_a(self):
        pass