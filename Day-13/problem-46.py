# Question 4: Append Data
# Append the following lines to notes.txt:
# JavaScript
# Go
# Now print the entire file.

f = open("notes.txt","a")
f.write("Javascript\n")
f.close()

a = open("notes.txt","r")
z = a.read()
print(z)
a.close()