#2f_Build-a-Pizza_Menu.py
''' 🍕 6. Build-a-Pizza Menu
Concepts: string matching, multiple if conditions
Task:
Ask the user what toppings they want. Based on their input:

Display what kind of pizza it is (e.g., "Cheese + Ham = Hawaiian!")

Print an error message if they choose an odd combination.

🧠 Stretch: Let them pick 2–3 ingredients and use nested if statements. '''

print("Pick two toppings for your pizza:")
topping1 = input("First topping: ").strip().lower()
topping2 = input("Second topping: ").strip().lower()

# Hawaiian check
if ("ham" in (topping1 + topping2)) and ("pineapple" in (topping1 + topping2)):
    pizza = "Hawaiian"
# Classic Veggie
elif ("mushroom" in topping1 or topping2) and ("capsicum" in topping1 or topping2):
    pizza = "Veggie Delight"
# Meat Lovers
elif ("pepperoni" in topping1 or topping2) and ("bacon" in topping1 or topping2):
    pizza = "Meat Lovers"
else:
    pizza = None

if pizza:
    print("Great choice – that's a", pizza, "pizza!")
else:
    print("Hmm… that combination isn't on our menu.")
