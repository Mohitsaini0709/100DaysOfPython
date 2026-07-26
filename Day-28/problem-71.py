try:
    student = {
        "name": "Mohit",
        "age": 19
    }

    print(student["class"])

except KeyError:
    print("Key Not Found!")

except:
    print("Some other error occurred!")