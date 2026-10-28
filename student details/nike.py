


student = {}
def dictionary():
    print("welcome to my school.")
    print("what do you want to do?")
def option():
    choice = int(input("enter 1.to add the name of the student,2.to add the department, 3. to delete the name of the student, 4. to delete the department: "))
    if choice ==1:
        name = input("enter your name: ")
        student["name"] = name
        print(student)
        perform()
    elif choice == 2:
       dept = input("enter your department: ")
       student["dept"] = dept
       print(student) 
       perform()
    elif choice == 3:
        student.pop("name")
        print("name deleted sucessfully")
        print(student)
        perform()
    elif choice == 4:
        student.pop("dept")
        print("dept deleted sucessfully")
        print(student)
        perform()
def perform():
    a=int(input("do you want to perform any other function? 1. yes 2.no: "))
    if a == 1:
        option()
    else:
        print("bye for now")     
dictionary()
option()        
