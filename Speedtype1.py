import tkinter as tk
import time
from tkinter import messagebox
import random

# Sample texts categorized by difficulty
TEXTS = {
    "Low": "The quick brown fox jumps over the lazy dog.",
    "Medium": "Typing speed depends on practice and accuracy.",
    "Hard": "Complex algorithms optimize performance in computing."
}

class TypingSpeedTest:
    def __init__(self, root):
        self.root = root
        self.root.title("Typo.in - Typing Speed Tester")
        self.root.geometry("800x500")
        self.root.configure(bg="#121212")

        self.selected_text = tk.StringVar(value="Low")
        self.text_to_type = TEXTS[self.selected_text.get()]
        self.typed_text = ""
        self.start_time = None
        self.username = ""
        self.correct_chars = 0
        self.total_chars = 0

        self.create_ui()

    def create_ui(self):
        # App Name
        self.title_label = tk.Label(self.root, text="Typo.in", font=("Arial", 24, "bold"), fg="white", bg="#121212")
        self.title_label.pack(pady=10)

        # Username Entry
        self.username_label = tk.Label(self.root, text="Enter your name:", font=("Arial", 12), fg="white", bg="#121212")
        self.username_label.pack()
        self.username_entry = tk.Entry(self.root, font=("Arial", 12))
        self.username_entry.pack(pady=5)

        # Difficulty Selection
        self.category_label = tk.Label(self.root, text="Select Difficulty:", font=("Arial", 12), fg="white", bg="#121212")
        self.category_label.pack()
        self.category_menu = tk.OptionMenu(self.root, self.selected_text, *TEXTS.keys(), command=self.update_text)
        self.category_menu.pack(pady=5)

        # Typing Instruction
        self.instruction_label = tk.Label(self.root, text="Start typing below:", font=("Arial", 14, "bold"), fg="#cccccc", bg="#121212")
        self.instruction_label.pack(pady=5)

        # Text to Type
        self.display_label = tk.Label(self.root, text=self.text_to_type, font=("Arial", 14), fg="white", bg="#121212")
        self.display_label.pack(pady=5)

        # Typing Input Box
        self.input_text = tk.Text(self.root, font=("Arial", 14), height=3, wrap="word")
        self.input_text.pack(pady=5, padx=20, fill="x")
        self.input_text.bind("<KeyRelease>", self.check_typing)

        # Typing Speed Display
        self.speed_label = tk.Label(self.root, text="Speed: 0 WPM", font=("Arial", 14, "bold"), fg="white", bg="#121212")
        self.speed_label.pack()

        # Restart Button
        self.restart_button = tk.Button(self.root, text="Restart", font=("Arial", 12), command=self.restart_test)
        self.restart_button.pack(pady=10)

        # Fancy Leaderboard
        self.leaderboard_label = tk.Label(self.root, text=" 🏆Leaderboard ", font=("Arial", 16, "bold"), fg="#FFD700", bg="#121212")
        self.leaderboard_label.pack()
        self.leaderboard_text = tk.Text(self.root, font=("Arial", 12), height=5, state="disabled", bg="#1e1e1e", fg="#FFD700")
        self.leaderboard_text.pack(pady=5, padx=20, fill="x")

    def update_text(self, _):
        self.text_to_type = TEXTS[self.selected_text.get()]
        self.display_label.config(text=self.text_to_type)
        self.restart_test()

    def check_typing(self, event):
        if self.start_time is None:
            self.start_time = time.time()
        typed = self.input_text.get("1.0", "end-1c")
        self.input_text.tag_remove("correct", "1.0", "end")
        self.input_text.tag_remove("wrong", "1.0", "end")
        
        self.correct_chars = 0
        self.total_chars = len(typed)

        for i, char in enumerate(typed):
            if i < len(self.text_to_type):
                expected_char = self.text_to_type[i]
                if char == expected_char:
                    self.input_text.tag_add("correct", f"1.{i}", f"1.{i+1}")
                    self.correct_chars += 1
                else:
                    self.input_text.tag_add("wrong", f"1.{i}", f"1.{i+1}")
        
        self.input_text.tag_config("correct", foreground="green")
        self.input_text.tag_config("wrong", foreground="red")
        
        self.update_speed(typed)
        
        if typed.endswith("."):
            self.calculate_results()

    def update_speed(self, typed):
        time_elapsed = max(time.time() - self.start_time, 1)  # Avoid division by zero
        words = len(typed.split())
        wpm = round((words / time_elapsed) * 60)
        self.speed_label.config(text=f"Speed: {wpm} WPM")

    def calculate_results(self):
        time_taken = time.time() - self.start_time
        words = len(self.text_to_type.split())
        wpm = round((words / time_taken) * 60)
        accuracy = round((self.correct_chars / self.total_chars) * 100, 2) if self.total_chars > 0 else 0 

        messagebox.showinfo("Typing Speed Test", f"{self.username_entry.get()}\nSpeed: {wpm} WPM\nAccuracy: {accuracy}%")
        self.update_leaderboard(self.username_entry.get(), wpm, accuracy)

    def update_leaderboard(self, name, wpm, accuracy):
        self.leaderboard_text.config(state="normal")
        self.leaderboard_text.insert("end", f"{name}: {wpm} WPM, {accuracy}% Accuracy\n")
        self.leaderboard_text.config(state="disabled")

    def restart_test(self):
        self.input_text.delete("1.0", "end")
        self.speed_label.config(text="Speed: 0 WPM")
        self.start_time = None
        self.correct_chars = 0
        self.total_chars = 0

if __name__ == "__main__":
    root = tk.Tk()
    app = TypingSpeedTest(root)
    root.mainloop()
