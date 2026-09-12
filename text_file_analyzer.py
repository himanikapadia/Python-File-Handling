from collections import Counter


def read_file(filename):
    try:
        with open(filename, "r") as file:
            return file.read()

    except FileNotFoundError:
        print("File not found.")
        return None


def analyze_text(content):
    words = content.lower().split()

    total_lines = len(content.splitlines())
    total_words = len(words)
    total_characters = len(content)

    vowels = 0
    digits = 0

    for character in content.lower():
        if character in "aeiou":
            vowels += 1

        if character.isdigit():
            digits += 1

    cleaned_words = []

    for word in words:
        word = word.strip(".,!?;:\"'()[]{}")
        if word:
            cleaned_words.append(word)

    word_count = Counter(cleaned_words)

    if word_count:
        most_common_word, frequency = word_count.most_common(1)[0]
    else:
        most_common_word = "None"
        frequency = 0

    return {
        "lines": total_lines,
        "words": total_words,
        "characters": total_characters,
        "vowels": vowels,
        "digits": digits,
        "most_common_word": most_common_word,
        "frequency": frequency
    }


def display_result(filename, result):
    print("\nTEXT FILE ANALYZER")
    print("=" * 35)
    print(f"File name       : {filename}")
    print(f"Total lines     : {result['lines']}")
    print(f"Total words     : {result['words']}")
    print(f"Total characters: {result['characters']}")
    print(f"Total vowels    : {result['vowels']}")
    print(f"Total digits    : {result['digits']}")
    print(
        f"Most common word: "
        f"{result['most_common_word']} "
        f"({result['frequency']} times)"
    )
    print("=" * 35)


def main():
    print("Welcome to Text File Analyzer")

    filename = input("Enter file name: ")
    content = read_file(filename)

    if content is None:
        return

    result = analyze_text(content)
    display_result(filename, result)


main()