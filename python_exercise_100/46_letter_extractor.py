import glob

letters = []
file_list = glob.glob("letters/*.txt")

for filename in file_list:
    with open(filename , 'r') as file:
        letters.append(file.read().strip("\n"))


print(letters)
