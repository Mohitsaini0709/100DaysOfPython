
students =[]

while True:
    search_menu = int(input("""
1. Add Student
2. Show Student
3. Search Student
4. Update Student
5. Delete Student
6. Exit

Enter your choice: """))
     
    if (search_menu==1):
        std_name = input("Entre Student Name :")
        students.append(std_name)
        print ("Student Name Added Succesfully ! \n")

    elif(search_menu==2):
        print(students)    

    elif(search_menu==3):
        search = input("Search Student Name :")
        if(search in students):
            print(f"{search} is found")
        else:
            print(f"{search} is not found!")

    elif(search_menu==4):
        old_name = input("Entre Old Name Of Student :")
        if old_name in students:
            new_name = input("Entre New Name Of Student :")

            index = students.index(old_name)
            students[index] = new_name

            print("Student updated successfully.\n")

        else:
            print("Student not found.\n")


    elif(search_menu==5):    
            delete_name = input("Entre Delete Name : ")

            if (delete_name in students):
                students.remove(delete_name)
                print("Student Nmae delete Succesfully! \n")

            else:
                print("Student Nmae not found! \n")



    elif(search_menu==6):  
        break

    else:
        print("Invalid Number ! Please Entre A Valid Number \n")






          
     













