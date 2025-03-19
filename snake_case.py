# Makes incorrect casing into a pascal case
# Ask the user to input fullname in incorrect casing
fullname = input("Please enter your name in incorrect casing ")

# Makes the letters all lower case
lower = fullname.lower()

# Then replaces space with underscore
snake = lower.replace(" ","_")
