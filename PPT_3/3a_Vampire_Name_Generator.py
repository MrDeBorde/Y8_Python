# 3a_Vampire_Name_Generator.py

''' 🧛 1. Vampire Name Generator
Concepts: input(), .lower(), .strip(), if/elif/else, string slicing
Task:
Ask the user for:
First name
Favourite colour
Birth month
Then generate a funny or spooky vampire name like:
"Count [First 3 letters of name][Colour]"
💡 Extension: Use .lower() and .capitalize() for formatting, and add multiple conditionals to vary the results. '''

first_name = input("What's your first name? ").strip()
colour = input("What's your favourite colour? ").strip().lower()
month = input("What month were you born in? ").strip().lower()

vampire_name = "Count " + first_name[:3].capitalize() + colour.capitalize()
print("Your vampire name is:", vampire_name)


