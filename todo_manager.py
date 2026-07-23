import os
def add_task():
    with open("tasks.txt","a")as file:
        task=input("Enter your task:")
        file.write(task+"\n")
        print("Task Added Successfully!")

def view_task():
    if not os.path.exists("tasks.txt") or os.path.getsize("tasks.txt") == 0:
        print("\nNo Tasks available")
    else:
        n=1
        print("\n====== To Do Tasks ======")
        with open("tasks.txt","r") as file:
            for i in file:
                print(f"{n}. {i.strip()}")
                n+=1
        print("="*30)

while True:
    print("---- To-Do Manager ----")
    print("1. Add Tasks")
    print("2. View Tasks")
    print("3. Exit")
    choice=input("Enter Your Choice: ")
    if choice == "1":
        add_task()
    elif choice == "2":
        view_task()
    elif choice == "3":
        print("Exited")
        break
    else:
        print("Invalid Choice")
    print()
