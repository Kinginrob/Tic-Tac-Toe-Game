import tkinter as tk
from tkinter import messagebox, font
import random

class TicTacToe:
    def __init__(self, master):
        self.master = master
        self.master.title("Tic Tac Toe")
        self.master.configure(bg="#282c34")  # Background color

        # Initialize game variables
        self.board = [" " for _ in range(9)]
        self.current_player = "X"
        self.ai_mode = False
        self.ai = None

        # Initialize GUI elements
        self.create_main_menu()

    def create_main_menu(self):
        custom_font = font.Font(family="Helvetica", size=24, weight="bold")

        self.menu_frame = tk.Frame(self.master, bg="#282c34")
        self.menu_frame.pack(expand=True)

        vs_player_button = tk.Button(
            self.menu_frame,
            text="Player vs Player",
            width=20,
            height=3,
            bg="#61afef",  # Button color
            fg="#e06c75",  # Text color
            font=custom_font,
            command=self.start_pvp_mode,
        )
        vs_player_button.pack(pady=10)

        vs_ai_button = tk.Button(
            self.menu_frame,
            text="Player vs AI",
            width=20,
            height=3,
            bg="#61afef",  # Button color
            fg="#e06c75",  # Text color
            font=custom_font,
            command=self.start_ai_mode,
        )
        vs_ai_button.pack(pady=10)

    def start_pvp_mode(self):
        self.ai_mode = False
        self.menu_frame.pack_forget()
        self.create_widgets()

    def start_ai_mode(self):
        self.ai_mode = True
        self.ai = AI()
        self.menu_frame.pack_forget()
        self.create_widgets()

    def create_widgets(self):
        custom_font = font.Font(family="Helvetica", size=24, weight="bold")

        self.buttons = []
        for i in range(9):
            button = tk.Button(
                self.master,
                text=" ",
                width=10,
                height=3,
                bg="#61afef",  # Button color
                fg="#e06c75",  # Text color
                font=custom_font,
                command=lambda i=i: self.on_button_click(i),
            )
            button.grid(row=i // 3, column=i % 3)
            self.buttons.append(button)

    def on_button_click(self, index):
        if self.board[index] == " ":
            # Player's move
            self.board[index] = self.current_player
            self.buttons[index].config(text=self.current_player)

            # Check for a winner or a draw
            if self.check_winner():
                messagebox.showinfo("Game Over", f"Player {self.current_player} wins!")
                self.reset_game()
            elif " " not in self.board:
                messagebox.showinfo("Game Over", "It's a draw!")
                self.reset_game()
            else:
                # Switch the current player
                self.current_player = "O" if self.current_player == "X" else "X"

                # If in AI mode, let the AI make a move
                if self.ai_mode and self.current_player == "O":
                    ai_move = self.ai.make_move(self.board)
                    self.on_button_click(ai_move)

    def check_winner(self):
        win_combinations = [
            (0, 1, 2),
            (3, 4, 5),
            (6, 7, 8),
            (0, 3, 6),
            (1, 4, 7),
            (2, 5, 8),
            (0, 4, 8),
            (2, 4, 6),
        ]

        for a, b, c in win_combinations:
            if (
                self.board[a] == self.board[b] == self.board[c]
                and self.board[a] != " "
            ):
                return True
        return False

    def reset_game(self):
        self.board = [" " for _ in range(9)]
        self.current_player = "X"
        for button in self.buttons:
            button.config(text=" ")

class AI:
    def make_move(self, board):
        # Check if AI can win
        for i in range(9):
            if board[i] == " ":
                temp_board = board.copy()
                temp_board[i] = "O"
                if self.check_winner(temp_board):
                    return i

        # Check if the player can win and block them
        for i in range(9):
            if board[i] == " ":
                temp_board = board.copy()
                temp_board[i] = "X"
                if self.check_winner(temp_board):
                    return i

        # Choose a random available move
        available_moves = [i for i in range(9) if board[i] == " "]
        return random.choice(available_moves)

    def check_winner(self, board):
        win_combinations = [
            (0, 1, 2),
            (3, 4, 5),
            (6, 7, 8),
            (0, 3, 6),
            (1, 4, 7),
            (2, 5, 8),
            (0, 4, 8),
            (2, 4, 6),
        ]

        for a, b, c in win_combinations:
            if (
                board[a] == board[b] == board[c]
                and board[a] != " "
            ):
                return True
        return False

def main():
    root = tk.Tk()
    game = TicTacToe(root)
    root.mainloop()

if __name__ == "__main__":
    main()
