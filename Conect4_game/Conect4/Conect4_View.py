""" Displays data for interaction with user"""
from itertools import zip_longest

class View:
    """ THis is how the game is presented to the player"""

    def __init__(self):
        """Init's view"""


    def starting_print(self):
        """Print's rules """
        text = "Choose a column to drop your color checker."
        text += "Take turns for each move."
        text += "The object of the game is to get four of your color"
        text += "checkers either vertically, horizontally, or diagonally."
        print(text)

    def show_board(self):
        """Print's the current board"""
        # self.board = self.Model.currentBoard
        # for x in zip_longest(*self.board.split(), fillvalue=' '):
        #     print(' '.join(x))
        #print(self.test.update_board())
        # for each_column in self.test.:
        #     "\n".join(each_column)
        #     return self.test.currentBoard
        #
        # print(self.test.)
        pass


    #     """Appends whole row to grid"""
    #     for row in range(7):
    #         self.grid.append("_")
    #
    #     res = "|".join(self.grid)
    #
    #     #print(res)




    def show_turn(self):
        """Print's the turn and asks for input"""
        self.current_play = int(input("pick a collum"))
        self.current_play -=1


    def show_invalid(self):
        """Print's if players input id invalid"""

    def show_winner(self):
        """Print's if four in a row."""

    def show_tie(self):
        """Print's if no more spaces on board"""