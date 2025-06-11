
# 3d_Favourite_Colour_Response_Bot.py
''' 🎨 4. Favourite Colour Response Bot
Concepts: input(), .lower(), in, logical operators
Task:
Ask the user their favourite colour and give a response:

“Blue” → “Cool and calm.”

“Red” → “Bold choice!”

Support multiple variants (e.g. “light blue”, “Blue”, “ BLUE ”)

🎨 Stretch: Build responses based on whether colour contains "blue", "green", etc. '''

colour = input("What's your favourite colour? ").strip().lower()

if "blue" in colour:
    print("Cool and calm, like the sea!")
elif "red" in colour:
    print("Bold and powerful!")
elif "green" in colour:
    print("Fresh and full of life!")
else:
    print("That's a unique choice!")


