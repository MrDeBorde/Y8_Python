#2e_Birthday_Age_Checker.py
''' 🎂 5. Birthday Age Checker
Concepts: numeric input, if statements
Task:
Ask the user for their birth year or age. Based on it:

Say if they’re old enough to vote, drive, or get a job.

Provide custom messages for milestone ages.

🗓 Stretch: Use import datetime to calculate from year of birth. '''

age = int(input("Enter your age: "))

if age < 16:
    print("Too young to drive.")
elif age < 18:
    print("You can get a learner’s licence!")
elif age <= 70:
    print("You can hold a full licence.")
else:
    print("Time to check licence renewal requirements.")



