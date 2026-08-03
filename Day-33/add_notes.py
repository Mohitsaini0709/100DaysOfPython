import os

def add_notes():

    try:

        user = input("Enter Your Subject Name To add Notes : ")  
        path = os.path.join("Subjects", user)
        notes_name = input("Enter Your Notes file Name  : ")
        notes = input("Enter Your Notes here  : ")
        file_path = os.path.join(path, f"{notes_name}.txt")


        if os.path.exists(path):
            
            with open(f"{file_path}","w") as f:
             a = f.write(notes)
            print(a) 
            print("Notes Saved Succesfully")    

        else:
            print("These subject Doesn't Exist")

    except Exception as e:
       print(e)        



        
        