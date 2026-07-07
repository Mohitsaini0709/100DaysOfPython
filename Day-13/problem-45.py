# Create a file named notes.txt.
# Write the following into it:
# Python
# Java
# C++

f = open("notes.txt", "w")
f.write('''
Python
Java
C++
''')
f.close()