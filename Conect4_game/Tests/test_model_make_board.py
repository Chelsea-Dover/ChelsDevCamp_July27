__author__ = 'Chelsea'

import unittest


class TestModelMakeBoard(unittest.TestCase):
    """make sure it prints an empty list"""

    def setUp(self):
        """Inits empty grid for testing"""
        self.grid = []


    def test_print_empty_list(self):
        """makes sure grid is empty"""

        self.assertEqual(0, len(self.grid), "len_should_be_zero")

    def test_append_item_to_list(self):
        """Append item to grid. Test grid length"""
        self.grid.append("x")

        self.assertEqual(1, len(self.grid))

    def test_make_row(self):
        """Appends whole row to grid"""
        for row in range(7):
            self.grid.append("_")

        res = "|".join(self.grid)

        #print(res)

        self.assertEqual(7, len(self.grid))

    def test_make_board(self):
        """Appends whole board to grid"""

        for row in range(6):
            for collum in range(7):
                self.grid.append("|_|")
            self.grid.append("\n")
        res = "".join(self.grid)

        #print(res)

        self.assertEqual(48, len(self.grid))

if __name__ == '__main__':
    unittest.main()
