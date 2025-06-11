
# 3b_Password_Strength_Checker.py
''' 🕵️ 2. Password Strength Checker
Concepts: string length, in, not in, logical operators
Task:
Ask the user to input a password, then evaluate:

Is it at least 8 characters?

Does it include both letters and numbers?

Does it include a special character?

Give them a score out of 3 and suggestions to improve.

🔐 Stretch: Use .isdigit(), .isalpha(), .isalnum() for more robust checking. '''


password = input("Enter your password: ")

score = 0

if len(password) >= 8:
    score += 1
if any(char.isdigit() for char in password) and any(char.isalpha() for char in password):
    score += 1
if any(char in "!@#$%^&*()" for char in password):
    score += 1

print("Password strength:", score, "/ 3")

if score < 3:
    print("Try making it longer and mixing letters, numbers, and symbols.")



