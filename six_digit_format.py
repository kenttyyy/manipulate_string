# Ask user to input numbers ranging from zero to a thousand, then add zero to complete a six digit format
# User input prompt
number = int(input("Please input a number "))

# Check if a number ranges from zero to a thousand then add zero to make it 6 digit
if 0 <= number <= 1000:
    print(f"{number:06}")

# If it is not within the range, say it is not
else:
    print("Please enter a value within the given range")

