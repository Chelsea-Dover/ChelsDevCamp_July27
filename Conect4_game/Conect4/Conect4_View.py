""" The View displays data for interaction with user """

from itertools import zip_longest

class View:
    """ THis is how the game is presented to the player"""

    def __init__(self):
        """Init's view"""
        self.outcome = ""
        self.adjustment = -1

    def starting_print(self):
        """Print's rules """
        text = "Choose a column to drop your color checker."
        text += "Take turns for each move."
        text += "The object of the game is to get four of your color"
        text += "checkers either vertically, horizontally, or diagonally."
        print(text)

    def show_board(self, board):
        """Show the current board """
        print()
        print(" 1 2 3 4 5 6 7")
        for each_row in range(6):
             print("|", "|".join(column[each_row] for column in board), "|",sep='')
        print("---------------")
        print(" ^           ^ ")

    def show_turn(self, playing_player):
        """Print's the turn and asks for input"""
        inputNeeded = True
        players_move = 0
        while inputNeeded:
            # Prompt the user for their move
            players_move = input("Your turn, {}. What Column do you want to put your checker? (Please put in 1-7):  "
                  .format(playing_player[0]))

            # Make sure that they give an int, and convert it to an int
            try:
                conversion = int(players_move)
            except ValueError:
                conversion = 8
                print("That's not a valid input. ")

            # Check that it's in the range of 1-7
            if conversion not in range(1, 8):
                print("There is no column by that name. ")
            else:
                inputNeeded = False
                players_move = conversion -1

        # Return the player's move choice
        return players_move

    def show_winner(self, playing_player):
        """Print's if four in a row."""
        print("Yay! {} won! (^-^)".format(playing_player))

    def show_tie(self):
        """Print's if no more spaces on board"""
        print("Yay! It's a tie! (^-^)")