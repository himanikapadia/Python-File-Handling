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

def show_statistics(filename):
    lines = read_file(filename)

    if lines is None:
        return

    print("\n📊 FILE STATISTICS")
    print("=" * 30)

    print(f"📄 File name      : {filename}")
    print(f"📑 Total lines    : {count_lines(lines)}")
    print(f"📝 Total words    : {count_words(lines)}")
    print(f"🔤 Total characters: {count_characters(lines)}")
    print(f"⬜ Empty lines    : {count_empty_lines(lines)}")

    print("=" * 30)


print("📂 File Statistics Tool")

filename = input("Enter file name: ")

show_statistics(filename)