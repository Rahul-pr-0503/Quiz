import tkinter as tk
from tkinter import messagebox

questions = [
    {"question": "What is phishing?", "answers": ["A cyber attack", "A sport", "A type of software", "A programming language"], "correct": 0},
    {"question": "What does a firewall do?", "answers": ["Blocks unauthorized access", "Cleans your computer", "Speeds up the internet", "Monitors emails"], "correct": 0}
]

class QuizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Cybersecurity Quiz")
        self.score = 0
        self.current_question = 0
        
        self.question_label = tk.Label(root, text="", font=("Arial", 14))
        self.question_label.pack(pady=20)
        
        self.buttons = []
        for i in range(4):
            btn = tk.Button(root, text="", font=("Arial", 12), width=30, command=lambda i=i: self.check_answer(i))
            btn.pack(pady=5)
            self.buttons.append(btn)
        
        self.score_label = tk.Label(root, text="Score: 0", font=("Arial", 12))
        self.score_label.pack(pady=20)
        
        self.load_question()
    
    def load_question(self):
        if self.current_question < len(questions):
            q = questions[self.current_question]
            self.question_label.config(text=q["question"])
            for i, answer in enumerate(q["answers"]):
                self.buttons[i].config(text=answer)
        else:
            messagebox.showinfo("Game Over", f"Your final score: {self.score}")
            self.root.quit()
    
    def check_answer(self, index):
        if index == questions[self.current_question]["correct"]:
            self.score += 1
        self.current_question += 1
        self.score_label.config(text=f"Score: {self.score}")
        self.load_question()

if __name__ == "__main__":
    root = tk.Tk()
    app = QuizApp(root)
    root.mainloop()
