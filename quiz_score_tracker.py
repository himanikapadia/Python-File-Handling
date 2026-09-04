def save_score(name, score):
    with open("quiz_scores.txt", "a") as file:
        file.write(f"{name},{score}\n")


def show_scores():
    print("\n🏆 Previous Scores")

    try:
        with open("quiz_scores.txt", "r") as file:
            scores = file.readlines()

            if not scores:
                print("No scores yet.")
                return

            for score in scores:
                name, points = score.strip().split(",")
                print(f"{name}: {points}/3")

    except FileNotFoundError:
        print("No previous scores found.")


print(" Python Mini Quiz")

name = input("Enter your name: ")
score = 0

questions = [
    ("What keyword is used to create a class in Python?", "class"),
    ("Which symbol is used for comments in Python?", "#"),
    ("Which function is used to open a file?", "open")
]

for question, answer in questions:
    print("\n" + question)
    user_answer = input("Your answer: ").strip().lower()

    if user_answer == answer:
        print(" Correct!")
        score += 1
    else:
        print(" Wrong!")

print(f"\n Your score: {score}/3")

save_score(name, score)
show_scores()