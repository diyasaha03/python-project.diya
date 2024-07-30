import tkinter as tk
from tkinter import simpledialog, messagebox

class BankApp:
    def __init__(self, root):
        self.balance = 1000  # Set initial balance to 1000
        self.root = root
        self.root.title("Bank Transaction System")

        self.label = tk.Label(root, text="Select an option:", font=("Arial", 14))
        self.label.pack(pady=10)

        self.withdraw_button = tk.Button(root, text="Withdraw", command=self.withdraw, width=20)
        self.withdraw_button.pack(pady=5)

        self.deposit_button = tk.Button(root, text="Deposit", command=self.deposit, width=20)
        self.deposit_button.pack(pady=5)

        self.balance_button = tk.Button(root, text="Balance", command=self.check_balance, width=20)
        self.balance_button.pack(pady=5)

        self.exit_button = tk.Button(root, text="Exit", command=root.quit, width=20)
        self.exit_button.pack(pady=5)

    def withdraw(self):
        amount = simpledialog.askinteger("Withdraw", "Enter amount to withdraw:")
        if amount is not None:
            if amount > self.balance:
                messagebox.showwarning("Warning", "Insufficient funds in your account.")
            else:
                self.balance -= amount
                messagebox.showinfo("Success", f"You have withdrawn ${amount}.00.\nNew balance: ${self.balance}.00")

    def deposit(self):
        amount = simpledialog.askinteger("Deposit", "Enter amount to deposit:")
        if amount is not None:
            self.balance += amount
            messagebox.showinfo("Success", f"Thank you for depositing.\nNew balance: ${self.balance}")

    def check_balance(self):
        messagebox.showinfo("Balance", f"Your bank account balance is: ${self.balance}.00")

if __name__ == "__main__":
    root = tk.Tk()
    app = BankApp(root)
    root.mainloop()