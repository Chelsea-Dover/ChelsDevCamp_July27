__author__ = 'Chelsea'

import unittest


class TestModelSwapPlayer(unittest.TestCase):

    def setUp(self):
        """ Init's current player and players"""
        self.players = {1:["Player_a", "red"], 2:["Player_b", "yellow"]}



    def test_change_to_player_a(self):
        """Testing if current player 1 gets self.players 1 values"""
        self.current_player = 1
        self.playing_player = self.current_player[self.players]



        self.assertEqual(self.playing_player, 1)

    def test_change_to_player_b(self):
        self.playing_player = self.current_player[self.players]



        self.assertEqual(self.playing_player, 2)



if __name__ == '__main__':
    unittest.main()
