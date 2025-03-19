# Converts fullname into pascal case
# Prompt to enter fullname using incorrect casing

fullname = input("Please enter fullname in incorrect casing ")

# Makes the proper casing first
casing = fullname.title()

# Then proceeds to merging to make it pascal case by removing space
pascal = casing.replace(" ","")

# Prints the result
print(pascal)