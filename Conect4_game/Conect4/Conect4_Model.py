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


    def make_board(self):
        """ make the initial board """
        for row in range(6):
            for column in range(7):
                self.grid.append("|_")
            self.grid.append("|\n")
        glue = "".join(self.grid)
        print(glue)

    def update_board(self):
        """ update the board based on players move """
        pass

    def swap_player(self):
        """ If statement that + or - based on what current_player is"""
        self.playing_player = self.players[self.current_player]

        if self.current_player ==  1:
            self.current_player +=1
        else:
            self.current_player -=1
