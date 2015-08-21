__author__ = 'Chelsea'

import unittest


class TestModelSwapPlayer(unittest.TestCase):

    def setUp(self):
        """ Init's current player and players"""
        self.players = {1: ["Player_a", "x"], 2: ["Player_b", "o"]}

    def test_change_to_player_a(self):
        """Testing if current player 1 gets self.players 1 values"""
        self.current_player = 1
        self.playing_player = self.players[self.current_player]

        self.assertEqual(self.playing_player, ["Player_a", "x"])

    def test_change_to_player_b(self):
        """Testing if the current player is 2 get self.player 2 value"""
        self.current_player = 2
        self.playing_player = self.players[self.current_player]

        self.assertEqual(self.playing_player, ["Player_b", "o"])


if __name__ == '__main__':
    unittest.main()
