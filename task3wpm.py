import tkinter as tk
import random
import time

class TypingSpeedTester:
    def __init__(self, root):
        self.root = root
        self.root.title("Typing Speed Tester")
        self.root.geometry("400x350")

        self.label = tk.Label(root, text="Type the following:")
        self.text_display = tk.Label(root, wraplength=350)
        self.input_box = tk.Entry(root)
        self.start_button = tk.Button(root, text="Start", command=self.start_typing_test)
        self.result_label = tk.Label(root, text="WPM: 0")
        self.feedback_label = tk.Label(root, text="")
        self.new_trial_button = tk.Button(root, text="New Trial", command=self.new_trial)
        self.made_by_label = tk.Label(root, text="MADE BY ARYAN DUBEY")

        self.label.pack(pady=10)
        self.text_display.pack(pady=10)
        self.input_box.pack()
        self.start_button.pack(pady=10)
        self.result_label.pack()
        self.feedback_label.pack()
        self.new_trial_button.pack()
        self.made_by_label.pack()

        self.typing_started = False
        self.start_time = 0
        self.text_to_type = ""

    def generate_random_text(self):
        random.seed()
        return "HEY CODER TEST YOUR SKILLS HERE."

    def start_typing_test(self):
        if not self.typing_started:
            self.typing_started = True
            self.text_to_type = self.generate_random_text()
            self.text_display.config(text=self.text_to_type)
            self.input_box.delete(0, "end")
            self.input_box.config(state="normal")
            self.start_time = time.time()
            self.start_button.config(text="Finish")
        else:
            self.typing_started = False
            self.input_box.config(state="disabled")
            self.start_button.config(state="disabled")
            self.finish_typing_test()

    def new_trial(self):
        self.typing_started = False
        self.input_box.config(state="normal")
        self.start_button.config(state="normal")
        self.result_label.config(text="WPM: 0")
        self.feedback_label.config(text="")
        self.start_button.config(text="Start")

    def finish_typing_test(self):
        end_time = time.time()
        typed_text = self.input_box.get()
        text_length = len(self.text_to_type)
        time_taken = end_time - self.start_time
        wpm = int((text_length / 5) / (time_taken / 60))

        accuracy = self.calculate_accuracy(self.text_to_type, typed_text)
        result_text = f"WPM: {wpm} | Accuracy: {accuracy}%"
        self.result_label.config(text=result_text)

        if accuracy < 90:
            self.feedback_label.config(text="Better Luck Next Time")

    def calculate_accuracy(self, original, typed):
        original_words = original.split()
        typed_words = typed.split()
        correct_words = [word1 for word1, word2 in zip(original_words, typed_words) if word1 == word2]
        accuracy = (len(correct_words) / len(original_words)) * 100
        return round(accuracy, 2)

if __name__ == "__main__":
    root = tk.Tk()
    app = TypingSpeedTester(root)
    root.title("Typing Speed Tester by Aryan Dubey")
    root.configure(bg="black")
    root.mainloop()
