filename = input("Enter File Name: ").strip()

if not filename:
    print("Error: No file name provided.")
else:
    try:
        with open(filename, "r", encoding="utf-8") as file:
            print("Current Cursor Position:", file.tell())

            data = file.read()
            print("Cursor Position After Reading:", file.tell())

            # File metrics
            print("\n--- File Summary ---")
            print("Total Lines     :", len(data.splitlines()))
            print("Total Words     :", len(data.split()))
            print("Total Characters:", len(data))

            # Rewind and preview
            file.seek(0)
            print("\nCursor After seek(0):", file.tell())

            first_line = file.readline().rstrip("\r\n")
            if first_line:
                print(f"First Line: {first_line}")
            elif not data:
                print("First Line: [File is empty]")
            else:
                print("First Line: [Blank line]")

    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
    except PermissionError:
        print(f"Error: Permission denied accessing '{filename}'.")
    except UnicodeDecodeError:
        print("Error: File contains binary data or unsupported character encoding.")