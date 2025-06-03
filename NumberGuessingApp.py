import tkinter as tk
from tkinter import messagebox
import random
import pygame
import threading

# Initialize pygame mixer for background music
def play_music():
    pygame.mixer.init()
    pygame.mixer.music.load("background_music.mp3")  # Place your mp3 file in the same directory
    pygame.mixer.music.play(-1)  # Loop indefinitely

def stop_music():
    pygame.mixer.music.stop()

class NumberGuessingApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Number Guessing Game")
        self.root.geometry("500x400")
        self.root.resizable(False, False)
        self.root.configure(bg="#22223b")

        self.secret_number = random.randint(1, 100)
        self.attempts = 0

        # Title
        self.title_label = tk.Label(root, text="🎲 Guess The Number! 🎲", font=("Arial", 22, "bold"), fg="#f2e9e4", bg="#22223b")
        self.title_label.pack(pady=20)

        # Instructions
        self.instruction_label = tk.Label(root, text="I'm thinking of a number between 1 and 100. Can you guess it?", font=("Arial", 12), fg="#c9ada7", bg="#22223b")
        self.instruction_label.pack(pady=10)

        # Entry
        self.entry = tk.Entry(root, font=("Arial", 16), width=10, justify='center')
        self.entry.pack(pady=10)
        self.entry.focus()

        # Guess Button
        self.guess_button = tk.Button(root, text="Guess", font=("Arial", 14, "bold"), bg="#4a4e69", fg="#f2e9e4", command=self.check_guess)
        self.guess_button.pack(pady=10)

        # Feedback
        self.feedback_label = tk.Label(root, text="", font=("Arial", 14), fg="#9a8c98", bg="#22223b")
        self.feedback_label.pack(pady=10)

        # Attempts
        self.attempts_label = tk.Label(root, text="Attempts: 0", font=("Arial", 12), fg="#c9ada7", bg="#22223b")
        self.attempts_label.pack(pady=5)

        # Restart Button
        self.restart_button = tk.Button(root, text="Restart", font=("Arial", 12), bg="#22223b", fg="#f2e9e4", command=self.restart_game)
        self.restart_button.pack(pady=5)

        # Exit Button
        self.exit_button = tk.Button(root, text="Exit", font=("Arial", 12), bg="#c9ada7", fg="#22223b", command=self.exit_game)
        self.exit_button.pack(pady=5)

        # Start background music in a separate thread
        threading.Thread(target=play_music, daemon=True).start()

        # Bind Enter key to guess and Shift key to restart
        self.root.bind('<Return>', lambda event: self.check_guess())
        self.root.bind('<Shift_L>', lambda event: self.restart_game())
        self.root.bind('<Shift_R>', lambda event: self.restart_game())

    def check_guess(self):
        guess = self.entry.get()
        if not guess.isdigit():
            self.feedback_label.config(text="Please enter a valid integer!", fg="#e63946")
            return
        guess = int(guess)
        self.attempts += 1
        self.attempts_label.config(text=f"Attempts: {self.attempts}")
        if guess < self.secret_number:
            self.feedback_label.config(text="Too Low! Try again.", fg="#f1faee")
        elif guess > self.secret_number:
            self.feedback_label.config(text="Too High! Try again.", fg="#f1faee")
        else:
            self.feedback_label.config(text="🎉 Congratulations! You guessed it! 🎉", fg="#06d6a0")
            messagebox.showinfo("Winner!", f"Congratulations! You guessed the number in {self.attempts} attempts.")
            self.guess_button.config(state=tk.DISABLED)

    def restart_game(self):
        self.secret_number = random.randint(1, 100)
        self.attempts = 0
        self.attempts_label.config(text="Attempts: 0")
        self.feedback_label.config(text="")
        self.entry.delete(0, tk.END)
        self.guess_button.config(state=tk.NORMAL)

    def exit_game(self):
        stop_music()
        self.root.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = NumberGuessingApp(root)
    root.mainloop()
