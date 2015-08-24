"""
Model holds all the data. So it will hold the grid, and the players
"""

class Model:
    """ This class will hold the grid(list) and the players(Dict of lists)"""

    def __init__(self):
        """This init's the class"""
        self.players = {1: ["Player_a", "\u25CF"], 2: ["Player_b", "\u25CB"]}
        self.current_player = 1
        self.playing_player = self.players[1]
        self.row = 6
        self.column = 7
        self.grid = [[" "] * self.row for x in range(self.column)]
        #For testing v
        # print(self.grid)
        #For testing ^
    #
    def update_board(self, selection):
        """ update the board based on players move """
        conversion = int(selection)
        new_move = self.grid[selection]

        if new_move[0] != " " :
            return True

        adjustment = -1
        while new_move[adjustment] != " ":
            adjustment -= 1

        new_move[adjustment] = self.playing_player[1]
        return False

    def swap_player(self):
        """ If statement that + or sed on - bawhat current_player is"""

        if self.current_player ==  1:
            self.current_player += 1
        else:
            self.current_player -= 1
        self.playing_player = self.players[self.current_player]
        return self.playing_player