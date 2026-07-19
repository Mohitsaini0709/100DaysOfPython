count = 0

with open("poem.txt", "w") as f:
    f.write("""
twinkle, twinkle, little star,
How I wonder what you are!
Up above the world so high,
Like a diamond in the sky.
""")

with open("poem.txt", "r") as f:
    a = f.read()
    print(a)

count = a.lower().count("twinkle")

print(f"{count} times 'twinkle' repeat in this poem.")