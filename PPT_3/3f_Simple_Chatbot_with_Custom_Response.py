# 3f_Simple_Chatbot_with_Custom_Responses.py
''' 🎭 6. Simple Chatbot with Custom Responses
Concepts: if, string matching, .strip(), .lower()
Task:
Create a chatbot that:

Responds differently to different greetings (“hi”, “hello”)

Gives responses based on mood (“I’m sad” → “I hope things get better”)

🧠 Stretch: Add 5+ recognisable inputs and use in logic to respond even to full sentences. '''

user_input = input("Say something: ").strip().lower()

if "hi" in user_input or "hello" in user_input:
    print("Hi there!")
elif "how are you" in user_input:
    print("I'm just a bot, but I'm doing great!")
elif "sad" in user_input:
    print("I'm sorry to hear that. Want to talk about it?")
elif "bye" in user_input:
    print("Goodbye! Come back soon.")
else:
    print("Hmm, I’m not sure what to say to that.")


