import tkinter as tk
from tkinter import messagebox

class TicTacToe:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Tic Tac Toe")
        self.current_player = "X"
        self.buttons = [[tk.Button(self.window, text="", font='normal 20', width=5, height=2,
                                   command=lambda r=i, c=j: self.click(r, c))
                         for j in range(3)] for i in range(3)]
        for i in range(3):
            for j in range(3):
                self.buttons[i][j].grid(row=i, column=j)
        self.window.mainloop()

    def click(self, row, col):
        if not self.buttons[row][col]["text"]:
            self.buttons[row][col]["text"] = self.current_player
            if self.check_winner():
                messagebox.showinfo("Tic Tac Toe", f"Player {self.current_player} wins!")
                self.reset()
            elif self.check_draw():
                messagebox.showinfo("Tic Tac Toe", "It's a draw!")
                self.reset()
            else:
                self.current_player = "O" if self.current_player == "X" else "X"

    def check_winner(self):
        for i in range(3):
            if self.buttons[i][0]["text"] == self.buttons[i][1]["text"] == self.buttons[i][2]["text"] != "":
                return True
            if self.buttons[0][i]["text"] == self.buttons[1][i]["text"] == self.buttons[2][i]["text"] != "":
                return True
        if self.buttons[0][0]["text"] == self.buttons[1][1]["text"] == self.buttons[2][2]["text"] != "":
            return True
        if self.buttons[0][2]["text"] == self.buttons[1][1]["text"] == self.buttons[2][0] != "":
            return True
        return False

    def check_draw(self):
        for row in self.buttons:
            for button in row:
                if not button["text"]:
                    return False
        return True

    def reset(self):
        for row in self.buttons:
            for button in row:
                button["text"] = ""

if __name__ == "__main__":
    TicTacToe()