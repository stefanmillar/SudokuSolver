import sys
import copy
import math

# Solves a given 9 x 9 sudoku board
class solveSudoku:
    def __init__(self, sudokuBoard):
        global board
        global originalBoard
        originalBoard = copy.deepcopy(sudokuBoard)
        board = copy.deepcopy(sudokuBoard)

    # Return the solved board
    def solved_board(self):
        while self.check_completed() == False:
            if self.add_number() == False:
                return False

        return board

    # Check the board is completed
    def check_completed(self):
        for i in range(9):
            for j in range(9):
                if board[i][j] == 0:
                    return False

        return True

    def check_valid_board(self):
        for i in range(9):
            for j in range(9):
                if self.check_valid(i, j, board[i][j]) == False and board[i][j] != 0:
                    return False

        return True

    # Check if the indicating number and coordinate is valid on the board
    def check_valid(self, x, y, num):
        if self.check_row(x, y, num) == True and self.check_column(x, y, num) == True and self.check_box(x, y, num) == True:
            return True

        return False

    # Check to see if the number is valid in it's row
    def check_row(self, x, y, num):
        for i in range(9):
            if board[i][y] == num and i != x:
                return False

        return True

    # Check to see the number is valid in it's coordinate
    def check_column(self, x, y, num):
        for i in range(9):
            if board[x][i] == num and i != y:
                return False

        return True

    # Check to see the number is valid in it's 3x3 box
    def check_box(self, x, y, num):
        xinit = math.floor(x / 3) * 3
        yinit = math.floor(y / 3) * 3
        
        for i in range(3):
            for j in range(3):
                if i + xinit == x and j + yinit == y:
                    pass
                elif board[i + xinit][j + yinit] == num:
                    return False

        return True

    # Add number to the board
    def add_number(self):
        i = 0
        j = 0

        # Find next number on board to be filled
        while board[i][j] > 0 and board[i][j] < 10:
            i += 1
            if i == 9:
                i = 0
                j += 1

        if self.add(i, j, 1) == False:
            return False

    # Add a valid number to the given coordanites. If no valid number found, backtrack to previous coordanite to find a new number
    def add(self, x, y, num):
        board[x][y] = 0

        # Find a valid number
        for i in range(num, 10):
            if self.check_valid(x, y, i) == True:
                board[x][y] = i
                return

        # No valid number found go to previous spot to find new number
        if x != 0:
            coor = self.find_previous_spot(x - 1, y)
            self.add(coor[0], coor[1], board[coor[0]][coor[1]] + 1)
        elif x == 0 and y != 0:
            coor = self.find_previous_spot(8, y - 1)
            self.add(coor[0], coor[1], board[coor[0]][coor[1]] + 1)
        else:
            if(num > 9):
                return False
            self.add(0, 0, num + 1)

    # Find's the next previous spot for backtracking that's not one of the original numbers
    def find_previous_spot(self, x, y):
        while originalBoard[x][y] != 0:
            if x == 0 and y != 0:
                x = 8
                y -= 1
            elif x != 0:
                x -= 1
            else:
                x = 0
                y = 0
                break

        coor = [x, y]
        return coor

    # Print the board
    def print_board(self):
        for x in range(9):
            for y in range(9):
                print(board[y][x], end=' ')

            print("")
