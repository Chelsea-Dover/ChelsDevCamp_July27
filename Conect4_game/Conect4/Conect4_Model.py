"""
Model holds all the data. So it will hold the grid, and the players
"""

class Model:
    """ This class will hold the grid(list) and the players(Dict of lists)"""

    def __init__(self):
        """This init's the class"""
        self.grid = []
        self.players = {1: ["Player_a", "x"], 2: ["Player_b", "o"]}
        self.current_player = 1


    def update_board(self):
        """ updates board based on players move"""
        pass

    def swap_player(self):
        """ If statment that + or - based on what current_player is"""
        self.playing_player = self.players[self.current_player]

        if self.current_player ==  1:
            self.current_player +=1
        else:
            self.current_player -=1

    def testing_1_2_3(self):
        self.n_cols = int(self.n_cols)
        self.fn_rows = int(self.n_rows)

        self.matrix = [[0 for x in range(self.n_cols)] for y in range(self.n_rows)]
        print(self.matrix)  #for testing purposes