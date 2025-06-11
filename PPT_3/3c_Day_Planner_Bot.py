
# 3c_Day_Planner_Bot.py
''' 📅 3. Day Planner Bot
Concepts: strings, .lower(), conditionals
Task:
Ask what day of the week it is and suggest an activity:

“Monday = start a new project”

“Friday = movie night!”

Include a default response if input is misspelled.

📆 Stretch: Accept partial matches like “mon” using in keyword.
 '''

 day = input("What day is it today? ").strip().lower()

if "mon" in day:
    print("Start a new project today!")
elif "tue" in day:
    print("Keep up the momentum.")
elif "wed" in day:
    print("Halfway there!")
elif "thu" in day:
    print("Plan for tomorrow.")
elif "fri" in day:
    print("Movie night?")
elif "sat" in day or "sun" in day:
    print("Enjoy the weekend!")
else:
    print("Hmm, that doesn't sound like a day of the week.")

