# 3e_Mirror_Talk_Bot.py
''' 🪞 5. Mirror Talk Bot
Concepts: string manipulation, slicing, reversing
Task:
Take a user input string and print it backward as a mysterious “mirror reply.”

Example: "Hello" → "olleH"

🔁 Stretch: Detect if the message is a palindrome and respond specially (“Whoa! That’s a palindrome!”). '''


message = input("Say something to the mirror: ").strip()
reversed_message = message[::-1]
print("Mirror says:", reversed_message)

if message.lower() == reversed_message.lower():
    print("Wow! That's a palindrome!")
