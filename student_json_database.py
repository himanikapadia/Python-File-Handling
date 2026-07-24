import json

while True:
    print("==== Student Database ====")
    print("1. Add Student")
    print("2. View Student")
    print("3. Search Student")
    print("4. Exit")

    choice=input("Enter Choice: ")

    if choice == "1":
        name=input("Enter name: ")
        rno=int(input("Enter Rollno: "))
        course=input("Enter Course Name: ")
        cgpa=float(input("Enter CGPA: "))

        student={
            "Name": name,
            "Rollno": rno,
            "Course": course,
            "CGPA": cgpa
        }

        try:
            # Step 1: Read existing data
            with open("student.json","r") as file:
                students = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):   
            students = []  

        students.append(student)
        with open("student.json","w") as file:
            json.dump(students,file,indent=4)

    elif choice == "2":
        with open("student.json","r") as file:
            data=json.load(file)
            print(data)

    elif choice == "3":
        name=input("Enter name to search: ")
        with open("student.json","r") as file:
            data=json.load(file)
            found=0
            for i in data:
                if i["Name"].lower()==name.lower():
                    print("Student Found: ",i)
                    found=1
                    break
            if found == 0:
                print("\nStudent Not Found!\n")

    elif choice == "4":
        print("Exited ! Student database ")
        break
    else:
        print("Invalid Choice!")