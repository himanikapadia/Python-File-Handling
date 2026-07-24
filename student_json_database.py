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

        with open("student.json","w") as file:
            students=[]
            students.append(student)
            json.dump(students,file,indent=4)

    elif choice == "2":
        with open("student.json","r") as file:
            data=json.load(file)
            print(data)

    elif choice == "4":
        print("Exited ! Student database ")
        break
    else:
        print("Invalid Choice!")