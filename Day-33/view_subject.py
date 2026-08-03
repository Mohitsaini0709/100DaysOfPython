import os

def view_subject():

    try:
       
        if os.path.exists("Subjects"):

            subjects = os.listdir("Subjects")

            if len(subjects) == 0:
                print("No Subjects Found!")

            else:
                
                print("\n===== Subjects =====\n")
                print(f"{subjects}")

        else:
            print("Subjects folder does not exist!")

    except Exception as e:
        print(e)