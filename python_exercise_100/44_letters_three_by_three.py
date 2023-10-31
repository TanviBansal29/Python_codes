import string

with open("letterss.txt" , 'w') as file:
    for letter1, letter2, letter3 in zip(string.ascii_lowercase[0::3], string.ascii_lowercase[1::3], string.ascii_lowercase[2::3]):
        file.write(letter1+letter2+letter3+"\n")