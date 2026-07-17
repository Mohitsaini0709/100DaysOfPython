# Write a function that counts the number of vowels (a, e, i, o, u) in a given string.

char = str(input("Entre any word here : ")).lower()
count = 0

for ch in char:
    match ch:
        case 'a':
            count +=1
        case 'e':
            count +=1
        case 'i':
            count +=1
        case 'o':
            count +=1
        case 'u':
            count +=1

print(f"Total vowel's in the word is : {count}")          
