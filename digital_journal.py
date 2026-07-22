
print("====== Welcome to Digi-Journal =====")
print("Write Today's Journal")
data=input("~Start Writting~\n")
with open("journal.txt","a") as file:
        file.write(data)
print("Saved!")
str=input("Do you want to read all journal entries? (yes/no): ")
if str.lower() == "yes":
        with open("journal.txt","r") as file:
            data=file.read()
            print(data)
elif str.lower() == "no":
       exit()
else:
       print("Invalid Choice!")