import glob

file_list = glob.glob("letters/*.txt")
str = "python"
list = []
for filename in file_list:
    with open(filename, 'r') as f:
        letter = f.read().strip("\n")
    if letter in str:
            list.append(letter)

print(list)