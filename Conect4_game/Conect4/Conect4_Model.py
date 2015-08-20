"""
Model holds all the data. So it will hold the grid, and the players
"""

class Model:
    """ This class will hold the grid(list) and the players(Dict of lists)"""

    def __init__(self):
        """This init's the class"""
        self.grid = []
        self.players = {1:["Player_a", "red"], 2:["Player_b", "yellow"]}
        self.current_player = 1


    def update_board(self):
        """ updates board based on players move"""
        pass

    def swap_player(self):
        """ If statment that + or - based on what current_player is"""
        self.players_value = self.self.current_player[self.players]
        pass