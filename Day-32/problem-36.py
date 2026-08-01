# Count Files and Folders
import os

a = int(input('''
1. Create a folder
2. Delete Your folder
3. create a file
4. count exist file or Folder 
'''))

if a == 1 :
    user = input("Enter Your Folder Name Here :- ")
    os.mkdir(user)
    print("Folder Create Succesfully !")
elif a == 2 :
    user = input("Enter Your Folder WHich You Want To Delete :- ")
    os.rmdir(user)
    print("Folder Create Succesfully !")
elif a == 3 :
    user = input("Enter Your file Name :- ")
    with open(f"{user}.txt", "w") as file:
        pass 
elif a == 4 :
    item = os.listdir()
    print(f"Folder or file = {len(item)}")
    print(item)

