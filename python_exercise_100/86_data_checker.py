checklist = ["Portugal", "Germany", "Munster", "Spain"]

with open("countries-clean.txt", "r") as file:
    content = file.readlines()

content = [i.rstrip('\n') for i in content]
checked = [i for i in content if i in checklist]

print(checked)