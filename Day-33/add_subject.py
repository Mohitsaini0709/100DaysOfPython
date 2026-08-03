import os

def add_subject():

    try:
        # Subjects folder check
        if not os.path.exists("Subjects"):
            os.mkdir("Subjects")

        # User input
        user = input("Enter Your Subject Name: ").strip().title()

        # Empty subject check
        if user == "":
            print("Subject name cannot be empty!")
            return

        # Full path
        path = os.path.join("Subjects", user)

        # Subject already exists?
        if os.path.exists(path):
            print("Subject already exists!")
        else:
            os.mkdir(path)
            print(f"{user} Subject Created Successfully!")

    except Exception as e:
        print(e)