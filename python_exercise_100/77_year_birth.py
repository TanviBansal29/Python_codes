from datetime import datetime

age = int(input("What's your age? "))
year_birth = datetime.now().year - age
print("We think you were born back in %s" % year_birth)