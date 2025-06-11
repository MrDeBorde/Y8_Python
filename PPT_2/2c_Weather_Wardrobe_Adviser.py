#2c_Weather_Wardrobe_Adviser.py
''' 🧊 3. Weather Wardrobe Adviser
Concepts: if, input(), number/string logic
Task:
Ask the user for the current temperature. Based on the number:

Print a message like: "It’s cold—wear a jacket!" or "Nice day! A T-shirt is fine."

🧥 Extension: Add other questions like “Is it raining?” and provide an umbrella warning. '''

temp = int(input("What's the temperature (°C)? "))
rain = input("Is it raining? (yes/no) ").strip().lower()

if temp < 5:
    advice = "It's icy – wear a heavy coat"
elif temp < 15:
    advice = "Chilly – grab a jumper"
elif temp < 25:
    advice = "Mild – long sleeves are fine"
else:
    advice = "Hot – T-shirt weather!"

if rain == "yes":
    advice += " and don't forget an umbrella!"

print(advice + ".")

