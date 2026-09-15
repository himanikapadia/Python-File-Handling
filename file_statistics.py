def get_file_stats(filename):
    try:
        with open(filename, "r", encoding="utf-8") as file:
            lines = file.readlines()
    except FileNotFoundError:
        print("Error: File not found.")
        return

    # Calculate all stats directly from the loaded lines
    total_lines = len(lines)
    total_words = sum(len(line.split()) for line in lines)
    total_chars = sum(len(line.strip()) for line in lines)
    empty_lines = sum(1 for line in lines if line.strip() == "")

    print("\n" + "=" * 30)
    print("       FILE STATISTICS")
    print("=" * 30)
    print(f"File name       : {filename}")
    print(f"Total lines     : {total_lines}")
    print(f"Total words     : {total_words}")
    print(f"Total characters: {total_chars}")
    print(f"Empty lines     : {empty_lines}")
    print("=" * 30)


print("File Statistics Tool")
filename = input("Enter file name: ").strip()

if filename:
    get_file_stats(filename)
else:
    print("No filename entered.")