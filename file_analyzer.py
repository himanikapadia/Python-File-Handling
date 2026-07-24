filename = input("Enter File Name: ")
try:
    with open(filename, "r") as file:

        # Initial cursor position
        print("Current Cursor Position:", file.tell())

        # Read complete file
        data = file.read()

        # Cursor after reading
        print("Cursor Position After Reading:", file.tell())

        # Count lines
        print("Total Lines:", len(data.splitlines()))

        # Count words
        print("Total Words:", len(data.split()))

        # Count characters
        print("Total Characters:", len(data))

        # Move cursor back to beginning
        file.seek(0)

        print("\nCursor After seek():", file.tell())

        print("First Line:")
        print(file.readline())

except FileNotFoundError:
    print("File not found!")