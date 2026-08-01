import os
a = input("Entre Your Folder name To check Ites exist or not : ")
if (os.path.exists(a) == True):
    print("Path Alredy Exist!")
else :
    os.mkdir(a) 
    print("Folder Created Successfully!")

