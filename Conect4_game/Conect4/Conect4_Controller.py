""" Controller is the one class to rule them all! It's responsible for the comunication of model and view"""
from Conect4_Model import Model
from Conect4_View import View

class Controller:
    """ Creates logic for comunication model and view"""

    def __init__(self):
        """ Inti's controller"""

    def get_board_status(self):
        """ Takes input from grid and updates view"""
        pass

    def get_move(self):
        """Takes input from view and updats grid"""
        pass

    def check_tie(self):
        """ see's if grid is full"""
        pass

    def check_winner(self):
        """ Checks to see if four in a row"""
        pass

    def check_valid(self):
        """ Checks if input is valid"""
        pass

    def main(self):
        """ Starts game and calls all helper functions"""
        pass