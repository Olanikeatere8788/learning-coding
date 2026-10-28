student = []
login_student ={}

def data_d():
    a = (int)(input("Enter 1. to Register, 2. to login: "))
    if a == 1:
       registration()

    elif a == 2:
       login()
       

def registration():
    first_name = input("Enter your first name: ")
    last_name = input("Enter your last name: ")
    e_mail = input("Enter your email: ")
    pass_word = input("Enter your password: ")

    
    new_student = {}
    new_student["first name"] = first_name
    new_student["last name"] = last_name
    new_student["email"] = e_mail
    new_student["password"] = pass_word 
    student.append(new_student)
    print(f"congratulation {first_name} ,your registration is successfull")
    options()
    

def login():
    global login_student
    e = input("enter the email: ")
    p = input("enter the password: ")
    for student_data in student:
      if e == student_data["email"] and p == student_data["password"]:
       login_student = student_data
       display_login()

def display_login():
    print(f"Dear {login_student["first name"]} {login_student["last name"]},you have login successfully ")
    log_out()

def options():
    choice = int(input("Do you want to go back to the main menu? 1.yes,2.no: "))
    if choice == 1:
     data_d()
    else:
       print("bye")

def log_out():
   log = input("Do you want to log out 1.yes 2.no:")
   if log == 1:
      data_d()
   else:
      display_login()

registration()




         