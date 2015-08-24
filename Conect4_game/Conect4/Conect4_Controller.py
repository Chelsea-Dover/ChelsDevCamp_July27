""" Controller is the one class to rule them all! It's responsible for the comunication of model and view"""
from Conect4_View import View
from Conect4_Model import Model
import time

class Controller:
    """ Creates logic for comunication model and view"""

    def __init__(self):
        """ Inti's controller"""
        # self.current_board = self.something_model.make_board()
        # print(self.current_board)
        #self.current_move = self.View.current_play
        self.view = View()
        self.model = Model()
        self.board = self.model.grid
        self.valid = self.model.isValidMove


    def get_board_status(self):
        """ Takes input from grid and updates view"""
        #self.model.updateboard
        pass

    def get_move(self):
        move_needed = True

        while move_needed:
            """Takes input from view and updates grid"""
            move = self.view.show_turn()

            move_needed = self.model.update_board(move)


    def check_tie(self):
        """ see's if grid is full"""
        pass

    def check_winner(self):
        """ Checks to see if four in a row"""
        pass

    #def check_valid(self):
     #   """ Checks if input is valid"""

    def main(self):
        """ Starts game and calls all helper functions"""
        self.model.make_board()
        print(self.model.grid)
        self.get_move()
        print(self.board)

