# Project: College Notes Organizer
from add_subject import add_subject
from view_subject import view_subject
from add_notes import add_notes

print("="*30 , "College Notes Organizer" , "="*30)
user = int(input(''' 
    Menu - 
        1. Add Subject
        2. View Subjects
        3. Add Note
        4. Exit
'''))

if user == 1:
    add_subject()
elif user == 2:
    view_subject()
elif user == 3:
    add_notes()
elif user == 4:
    print("Thank You!")
else:
    print("Invalid Choice!")    
