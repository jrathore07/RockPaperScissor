from random import randint
import tkinter as tk
from tkinter import messagebox
import time
score=[]

# Create the main window
root = tk.Tk()
root.title("Rock Paper Scissors")
root.geometry("300x200")

def play_game():
    choices = ["rock", "paper", "scissors"]
    computer_choice = choices[randint(0, 2)]
    user_choice = user_choice_var.get()
    
    if not user_choice:
        messagebox.showerror("Error", "Please select a choice!")
        return
        
    result = ""
    if user_choice == computer_choice:
        result = "It's a tie!"
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "paper" and computer_choice == "rock") or \
         (user_choice == "scissors" and computer_choice == "paper"):
        result = "You win!"
    else:
        result = "You lose!"
        
    messagebox.showinfo("Result", f"Computer chose: {computer_choice}\n{result}")

# Create radio buttons for choices
user_choice_var = tk.StringVar()
tk.Radiobutton(root, text="Rock", variable=user_choice_var, value="rock").pack()
tk.Radiobutton(root, text="Paper", variable=user_choice_var, value="paper").pack()
tk.Radiobutton(root, text="Scissors", variable=user_choice_var, value="scissors").pack()

# Create play button
tk.Button(root, text="Play", command=play_game).pack(pady=10)

# Create quit button
tk.Button(root, text="Quit", command=root.destroy).pack()
try:
    with open("rockpaperscissor.txt", "r") as f:
        score=[int(line.strip()) for line in f.readlines() if line.strip().isdigit()]
except FileNotFoundError:
        print("No previous scores found. Starting fresh.")
while True:
    highscore=min(score) if score else float("inf")
    print("Welcome to the Rock, Paper, Scissors game!")
    choices = ["rock", "paper", "scissors"]
    computer_choice = choices[randint(0, 2)]
    user_choice = input("Enter your choice (rock, paper, scissors): ").strip().lower()
    while user_choice not in choices:
        print("Invalid choice! Please choose rock, paper, or scissors.")
        user_choice = input("Enter your choice (rock, paper, scissors): ").strip().lower()
    print(f"Computer chose: {computer_choice}")
    if user_choice == computer_choice:
        print("It's a tie!")
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "paper" and computer_choice == "rock") or \
         (user_choice == "scissors" and computer_choice == "paper"):
        print("You win!")
    else:
        print("You lose!")
    with open("rockpaperscissor.txt", "a") as f:   
        f.write(f"{user_choice} vs {computer_choice}\n")
    if user_choice == computer_choice:
        print(f"New high score! You beat the previous high score of {highscore} attempts.")
    play_again = input("Do you want to play again? (yes/no): ").strip().lower()
    if play_again != 'yes':
        print("Thanks for playing!")
        break
    print("Starting a new game...")
    time.sleep(3)
