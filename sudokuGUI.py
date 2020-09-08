from tkinter import *
from tkinter import messagebox
import tkinter.font as tkFont
import copy
from sudoku import solveSudoku

# GUI for solving a 9 x 9 sudoku board
class GUI:
    def __init__(self):
        global root
        root = Tk()
        root.after_idle(self.main_menu)
        root.winfo_toplevel().title("Sudoku Solver")
        root.resizable(0,0)
        root.iconbitmap(r'sudoku.ico')
        self.create_entries()
        self.create_solve_button()
        root.mainloop()

    def main_menu(self):
        messagebox.showinfo("Welcome!", "Enter any valid sudoku board and click solve to see the solution.")

    # Create the text entries and grid
    def create_entries(self):
        global entries
        fontstyle = tkFont.Font(size=40)
        entries = [[Text(root, height=1, width=1, relief="solid", selectborderwidth=3, font=fontstyle, padx=20) for x in range(9)] for y in range(9)]

        for j in range(9):
            for i in range(9):
                entries[j][i].grid(row=i, column=j)

    # Create the solve button
    def create_solve_button(self):
        solve = Button(root, text="Solve", font=tkFont.Font(size=15), command=self.solve_the_board)
        solve.grid(row=9, column=7)

    # Solve the given board by the user
    def solve_the_board(self):
        board = self.get_current_board()
        solver = solveSudoku(board)

        if solver.check_valid_board() == False:
            messagebox.showwarning("Invalid Input", "Not a valid board")
            return

        solvedBoard = solver.solved_board()
        if solvedBoard == False:
            messagebox.showwarning("Invalid Input", "Unsolvable board")
            return

        self.show_solved_board(solvedBoard)

    # Show the new solved board on the grid
    def show_solved_board(self, solvedBoard):
        for x in range(9):
            for y in range(9):
                #entries[x][y].delete("1.0", "end")
                entries[x][y].insert(INSERT, solvedBoard[x][y])

    # Assign the current board to a variable
    def get_current_board(self):
        board = [[0 for x in range(9)] for y in range(9)]
        for j in range(9):
            for i in range(9):
                if entries[j][i].get("1.0", "end") == "\n":
                    pass
                elif entries[j][i].get("1.0", "end")[0].isdigit() == False:
                    messagebox.showwarning("Invalid Input", "Board must only have numbers between 1-9")
                    return
                elif int(entries[j][i].get("1.0", "end")) < 1 or int(entries[j][i].get("1.0", "end")) > 9:
                    messagebox.showwarning("Invalid Input", "Board must only have numbers between 1-9")
                    return
                elif int(entries[j][i].get("1.0", "end")) >= 1 and int(entries[j][i].get("1.0", "end")) <= 9:
                    board[j][i] = int(entries[j][i].get("1.0", "end"))

        return board

def main():
    gui = GUI()

if __name__ == "__main__":
    main()