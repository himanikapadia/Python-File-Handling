from collections import Counter


def count_words(filename):
    try:
        with open(filename, "r") as file:
            content = file.read().lower()

        words = content.split()
        return Counter(words)

    except FileNotFoundError:
        print("File not found.")
        return None


def display_frequency(frequency):
    print("\nWORD FREQUENCY")
    print("-" * 25)

    for word, count in frequency.items():
        print(f"{word}: {count}")


filename = input("Enter file name: ")

frequency = count_words(filename)

if frequency is not None:
    display_frequency(frequency)