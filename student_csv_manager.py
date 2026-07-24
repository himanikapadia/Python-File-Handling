import csv

while True:
    print("\n===== Student Records ====")
    print("1. Add Student")
    print("2. View Student")
    print('3. Exit')

    choice=input("Enter your Choice: ")

    if choice == "1":
        name=input("Enter name: ")
        rno=int(input("Enter Rollno: "))
        course=input("Enter Course Name: ")
        with open("students.csv","a",newline="") as file:
            writer=csv.writer(file)
            writer.writerow([name,rno,course])
            print("\nRecord Added!")

    elif choice == "2":
        with open("students.csv","r") as file:
            reader=csv.reader(file)
            print("-"*30)
            print("Name\tRollno\tCourse")
            print("-"*30)
            for i in reader:
                print("\t".join(i))
            print("-"*30)

    elif choice == "3":
        print("Exiting Student Manager! GoodBye!...")
        break

    else:
        print("Invalid Choice! ")