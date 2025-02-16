questions = [
    {"question": "What is phishing?", "answers": ["A cyber attack", "A sport", "A type of software", "A programming language"], "correct": 0},
    {"question": "What does a firewall do?", "answers": ["Blocks unauthorized access", "Cleans your computer", "Speeds up the internet", "Monitors emails"], "correct": 0}
]

def quiz():
    score = 0
    for q in questions:
        print(q["question"])
        for i, ans in enumerate(q["answers"]):
            print(f"{i + 1}. {ans}")
        
        try:
            answer = int(input("Enter the number of your answer: ")) - 1
            if answer == q["correct"]:
                score += 1
                print("Correct!\n")
            else:
                print("Wrong answer.\n")
        except ValueError:
            print("Invalid input. Moving to next question.\n")
    
    print(f"Game Over! Your final score: {score}/{len(questions)}")

if __name__ == "__main__":
    quiz()
