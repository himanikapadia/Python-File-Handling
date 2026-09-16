FILENAME = "scores.txt"


def save_score(name, score):
    with open(FILENAME, "a", encoding="utf-8") as file:
        file.write(f"{name},{score}\n")


def display_scores():
    print("\n🏆 High Scores (Top 5)")

    try:
        with open(FILENAME, "r", encoding="utf-8") as file:
            lines = file.readlines()

        if not lines:
            print("No scores yet.")
            return

        # Turn each line into a pair: (name, integer_score)
        score_list = []
        for line in lines:
            if "," in line:
                name, points = line.strip().split(",")
                score_list.append((name, int(points)))

        # Sort by points from highest to lowest
        score_list.sort(key=lambda item: item[1], reverse=True)

        # Show the top 5 with rank numbers
        for rank, (name, points) in enumerate(score_list[:5], start=1):
            print(f"{rank}. {name} - {points} pts")

    except FileNotFoundError:
        print("No scores yet.")


# --- Main Program ---
print("🎮 High Score Tracker")

name = input("Enter your name: ").strip()
score_input = input("Enter your score: ").strip()

# Check that the inputs are valid before saving
if name and score_input.isdigit():
    save_score(name, int(score_input))
    display_scores()
else:
    print("Invalid input! Please enter a valid name and a numeric score.")