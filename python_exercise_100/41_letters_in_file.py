import string

with open("letter.txt" , 'w') as file:
    for letter in string.ascii_lowercase:
        file.write(letter + "\n")