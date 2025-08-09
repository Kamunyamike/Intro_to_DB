adjective_1 = input("Enter an appropriate first adjective: ")
adjective_2 = input("Enter an appropriate second adjective: ")
adjective_3 = input("Enter an appropriate third adjective: ")
adjective_4 = input("Enter an appropriate fourth adjective: ") # Added parentheses and string

# Corrected story concatenation using f-string (recommended)
story = f"On a beautiful {adjective_1} day, I went to the zoo. I saw a funny {adjective_2} monkey swinging from the trees. Then, I spotted a majestic {adjective_3} tedd lounging in the sun. What a wild and {adjective_4} experience!"

# Corrected comparison operators (==)
if adjective_1.lower() == "sunny": # Changed = to ==
    story += "\nOh, it was a Sunny day of course."
elif adjective_1.lower() == "rainy": # Changed = to ==
    story += "\nThe drops were beautiful still."
else:
    story += "\nThe day was just awesome cool."

print(story)