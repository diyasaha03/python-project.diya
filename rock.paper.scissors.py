import tkinter as tk
from tkinter import messagebox
import random

def get_computer_choice():
    options = ["rock", "paper", "scissors"]
    return random.choice(options)

def check_win(player, computer):
    if player == computer:
        return "It's a tie!"
    elif player == "rock":
        if computer == "scissors":
            return "Rock smashes scissors! You win!"
        else:
            return "Paper covers rock! You lose."
    elif player == "paper":
        if computer == "rock":
            return "Paper covers rock! You win!"
        else:
            return "Scissors cuts paper! You lose."
    elif player == "scissors":
        if computer == "paper":
            return "Scissors cuts paper! You win!"
        else:
            return "Rock smashes scissors! You lose."

def on_choice(player_choice):
    computer_choice = get_computer_choice()
    result = check_win(player_choice, computer_choice)
    messagebox.showinfo("Result", f"You chose {player_choice}, computer chose {computer_choice}\n{result}")

# Set up the main application window
root = tk.Tk()
root.title("Rock Paper Scissors")

# Create buttons for user choices
rock_button = tk.Button(root, text="Rock", command=lambda: on_choice("rock"), width=15, height=3)
paper_button = tk.Button(root, text="Paper", command=lambda: on_choice("paper"), width=15, height=3)
scissors_button = tk.Button(root, text="Scissors", command=lambda: on_choice("scissors"), width=15, height=3)

# Arrange buttons in a grid
rock_button.grid(row=0, column=0, padx=20, pady=20)
paper_button.grid(row=0, column=1, padx=20, pady=20)
scissors_button.grid(row=0, column=2, padx=20, pady=20)

# Run the application
root.mainloop()