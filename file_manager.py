import os

while True:
    print("==== File Manager ====")
    print("1. Create Folder")
    print("2. Delete Folder")
    print("3. Delete File")
    print("4. Check File Exists")
    print("5. List Files")
    print("6. Exit")
    print("="*20)

    choice=input("Enter your choice: ")

    if choice == "1":
        fname=input("Enter Folder Name: ")
        try:
            os.mkdir(fname)
            print(f"{fname} Created Successfully!")
        except FileExistsError:
            print(f"{fname} already Exits!")
    elif choice == "2":
        fname=input("Enter Folder name to Delete: ")
        try:
            os.rmdir(fname) # Removes Empty Folder
            print(f"{fname} Deleted Successfully!")
        except FileNotFoundError:
            print(f"{fname} does not Exists!")
        except OSError:
            print(f"{fname} is not empty, cannot Delete.")

    elif choice == "3":
        fname=input("Enter File name to Delete: ")
        try:
            os.remove(fname)
            print(f"{fname} Deleted Successfully!")
        except FileNotFoundError:
            print(f"{fname} does not Exists!")

    elif choice == "4":
        fname=input("Enter File to be Checked: ")
        try:
            os.path.exists(fname)
            print(f"{fname} Exists!")
        except FileExistsError:
            print(f"{fname} Does not Exists!")

    elif choice == "5":
        try:
            files=os.listdir(".") # current Directory
            for i in files:
                print("- ",i)
        except FileNotFoundError:
            print("Path Does not Exists!")

    elif choice == "6":
        print("Exiting File Manager. Goodbye!")
        break

    else:
        print("Invalid choice, please try again.")
