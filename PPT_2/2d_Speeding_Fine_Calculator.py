#2d_Speeding_Fine_Calculator.py
''' 🏎️ 4. Speeding Fine Calculator
Concepts: numeric comparisons, branching
Task:
Ask the user how fast they were driving. Compare it to the speed limit and:

Print “All good!” if under.

Print a warning if over, and calculate a fine based on how far over they were.

💡 Bonus: Use int(input()) for numeric input and create fine brackets. '''

speed_limit = int(input("Enter the speed limit (km/h): "))
driver_speed = int(input("Enter the driver's speed (km/h): "))

over = driver_speed - speed_limit

if over <= 0:
    print("All good – no fine.")
elif over <= 10:
    print("You were", over, "km/h over. Fine: $50")
elif over <= 20:
    print("You were", over, "km/h over. Fine: $150")
else:
    print("You were", over, "km/h over. Fine: $300")

