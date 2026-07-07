# Count how many lines are present in notes.txt.

file = open("notes.txt", "r")
lines = file.readlines()
print("Total lines =", len(lines))
file.close()



