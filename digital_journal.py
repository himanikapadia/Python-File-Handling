
print("====== Welcome to Digi-Journal =====")
print("Write Today's Journal")
data=input("~Start Writing~\n")
try:
        with open("journal.txt","a") as file:
                file.write(data + "\n")
        print("Saved!")
        choice=input("Do you want to read all journal entries? (yes/no): ")
        if choice.lower() == "yes":
                with open("journal.txt","r") as file:
                        print("\n===== Your Journal =====")
                        print(file.read())
        elif choice.lower() == "no":
                print("Thank you for using Digi-Journal!")
        else:
                print("Invalid Choice!")
except FileNotFoundError:
        print("No journal entries found.")