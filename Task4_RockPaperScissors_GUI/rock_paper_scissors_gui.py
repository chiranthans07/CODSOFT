import random
import tkinter as tk

# Game choices
choices = ["Rock", "Paper", "Scissors"]

user_score = 0
computer_score = 0

# Function to play game
def play(user_choice):
    global user_score, computer_score

    computer_choice = random.choice(choices)
    computer_label.config(text="Computer chose: " + computer_choice)

    if user_choice == computer_choice:
        result_label.config(text="It's a Tie!", fg="#3498db")

    elif (
        (user_choice == "Rock" and computer_choice == "Scissors") or
        (user_choice == "Paper" and computer_choice == "Rock") or
        (user_choice == "Scissors" and computer_choice == "Paper")
    ):
        user_score += 1
        result_label.config(text="You Win!", fg="#2ecc71")

    else:
        computer_score += 1
        result_label.config(text="Computer Wins!", fg="#e74c3c")

    score_label.config(text=f"Your Score: {user_score}    Computer Score: {computer_score}")


# Main window
window = tk.Tk()
window.title("Rock Paper Scissors")
window.geometry("500x400")
window.configure(bg="#1e1e2f")
window.resizable(False, False)

# Title
title_label = tk.Label(
    window,
    text="Rock Paper Scissors",
    font=("Helvetica", 20, "bold"),
    bg="#1e1e2f",
    fg="white"
)
title_label.pack(pady=15)

# Score label
score_label = tk.Label(
    window,
    text="Your Score: 0    Computer Score: 0",
    font=("Helvetica", 12),
    bg="#1e1e2f",
    fg="white"
)
score_label.pack(pady=10)

# Button frame
button_frame = tk.Frame(window, bg="#1e1e2f")
button_frame.pack(pady=20)

# Buttons
rock_button = tk.Button(
    button_frame,
    text="Rock",
    width=12,
    height=2,
    font=("Helvetica", 12),
    bg="#3498db",
    fg="white",
    command=lambda: play("Rock")
)
rock_button.grid(row=0, column=0, padx=10)

paper_button = tk.Button(
    button_frame,
    text="Paper",
    width=12,
    height=2,
    font=("Helvetica", 12),
    bg="#9b59b6",
    fg="white",
    command=lambda: play("Paper")
)
paper_button.grid(row=0, column=1, padx=10)

scissors_button = tk.Button(
    button_frame,
    text="Scissors",
    width=12,
    height=2,
    font=("Helvetica", 12),
    bg="#e67e22",
    fg="white",
    command=lambda: play("Scissors")
)
scissors_button.grid(row=0, column=2, padx=10)

# Computer choice label
computer_label = tk.Label(
    window,
    text="",
    font=("Helvetica", 14),
    bg="#1e1e2f",
    fg="white"
)
computer_label.pack(pady=15)

# Result label
result_label = tk.Label(
    window,
    text="",
    font=("Helvetica", 16, "bold"),
    bg="#1e1e2f"
)
result_label.pack(pady=10)

window.mainloop()
