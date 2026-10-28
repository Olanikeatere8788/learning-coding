
#a =int(input("enter a number : "))

#def add5():
#   global a
#    a=a+5
#   print(a)
#   
#   sol =print("Do you want to add 5 again?")
#   sol_2= (input("1.yes 2.no : "))
#   if sol_2 == "1" or  sol_2== "yes":
#        add5()
#    else:
#        print ("Bye, thanks for coming")
#add5()


person = []
print("what do you want to do?")
def choice ():
    choice = int(input("enter 1 to add a new person,2.to remove a peson, 3. to display all person: "))
    if choice ==1:
       my_name = input ("enter your name: ")
       my_dept = input("enter your dept: ")
       student={}
       student["name"] = my_name
       student["dept"] = my_dept
       person.append(student)
       print(person)
       print (f"[name] added succesfully")
       perform()
    
    elif choice == 2:
      index = int(input("enter the index of the person you want to remove: "))
      person.pop(index)
      print (f"[index]remove successfully")
      print (person)
      perform()

    elif choice == 3:
      for a in person:
        print(f"my name is {a["name"]} and I studied {a["dept"]}")  
      perform()

def perform():
     perform = int(input("Do you want to do anything else 1. yes 2. no: "))
     if perform == 1:
      choice()
     else:
      print("thanks for coming bye")  

    
choice()     