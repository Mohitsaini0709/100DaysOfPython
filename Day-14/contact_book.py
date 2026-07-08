# Contact Book
# 1. Add Contact
# 2. View Contacts
# 3. Search Contact
# 4. Exit

dic = {}

while True:
    
    user = int(input('''
1. Add Contact
2. View Contacts
3. Search Contact
4. Exit
'''))
    if(user == 1):
        name = input('Entre Name :')
        contact = int(input("Entre Contact Number Here : "))
        dic.update({name : contact})
        f = open("contacts.txt","w")
        f.write(str(dic))
        f.close()
        print("\nContact Will be added Succesfully !")
    elif(user == 2):
        f = open("contacts.txt","r")
        read = f.read()
        print("Your Contact List Is Here !")
        print(read)
        f.close()
    elif(user == 3):
        search_name = input("Search a name Here to find Contact : ")
        if search_name in dic:
            print(f"Name : {search_name}")
            print(f"Contact : {dic[search_name]}")
        else:
            print("Contact Not Found!")

    elif(user == 4 ):
        break 

    else:
        print("Invalid Input")       