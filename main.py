
import random


def load_questions(path):
    questions = []

    with open(path, "r") as file:
        for line in file:
            line = line.strip()

            if "|" in line:
                question, answer = line.split("|", 1)

                questions.append({
                    "question": question,
                    "answer": answer
                })
            elif line:
                print("Skipping invalid line:", line)

    return questions


def ask_question(q):
    print("\n" + q["question"])

    user_answer = input("Your answer: ")

    if user_answer.strip().lower() == q["answer"].strip().lower():
        print("Correct answer!")
        return True
    else:
        print("Wrong answer!")
        print("Correct answer:", q["answer"])
        return False


def play_game():
    questions = load_questions("questions.txt")

    if not questions:
        print("No valid questions found!")
        return

    random.shuffle(questions)

    print("\n===== WELCOME TO QUIZCRAFT =====")

    while True:
        try:
            num_questions = int(
                input(f"How many questions? (1-{len(questions)}): ")
            )

            if 1 <= num_questions <= len(questions):
                break
            else:
                print("Please enter a valid number.")

        except ValueError:
            print("Please enter a number.")

    selected_questions = questions[:num_questions]

    score = 0
    wrong_questions = []

    for q in selected_questions:
        if ask_question(q):
            score += 1
        else:
            wrong_questions.append(q)

    total = len(selected_questions)
    percentage = (score / total) * 100

    print("\n===== QUIZ RESULTS =====")
    print("Total questions:", total)
    print("Your score:", score)
    print("Percentage:", percentage, "%")

    print("\n===== WRONG QUESTIONS =====")

    if wrong_questions:
        for q in wrong_questions:
            print(q["question"])
            print("Correct answer:", q["answer"])
    else:
        print("No wrong answers! Excellent!")


while True:
    play_game()

    choice = input("\nPlay again? (y/n): ").strip().lower()

    if choice != "y":
        print("Thanks for playing QuizCraft!")
        break
