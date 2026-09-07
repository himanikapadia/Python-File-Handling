def read_file(filename):
    try:
        with open(filename, "r") as file:
            return file.readlines()

    except FileNotFoundError:
        print("File not found.")
        return None


def count_lines(lines):
    return len(lines)


def count_words(lines):
    words = 0

    for line in lines:
        words += len(line.split())

    return words


def count_characters(lines):
    characters = 0

    for line in lines:
        characters += len(line.strip())

    return characters


def count_empty_lines(lines):
    empty_lines = 0

    for line in lines:
        if line.strip() == "":
            empty_lines += 1

    return empty_lines