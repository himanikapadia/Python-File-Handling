def save_score(name, score):
    with open("scores.txt", "a") as file:
        file.write(f"{name},{score}\n")


def display_scores():
    print("\n🏆 High Scores")

    try:
        with open("scores.txt", "r") as file:
            scores = file.readlines()

            if not scores:
                print("No scores yet.")
                return

            for score in scores:
                name, points = score.strip().split(",")
                print(f"{name}: {points}")

    except FileNotFoundError:
        print("No scores yet.")


print("🎮 High Score Tracker")

name = input("Enter your name: ")
score = input("Enter your score: ")

save_score(name, score)
display_scores()