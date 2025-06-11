#1a_Chatbot.py 

''' Write a “Getting to Know You” chatbot
→ Create a program that asks for your name, age, and favourite hobby, then prints a personalised message. '''

 

print ("Hello, I am a chatbot, tell me about yourself") 

NAME = input("What is your name? ") 

AGE = input("How old are you? ") 

HOBBY = input("What is a hobby of yours? ") 

 
print ("Nice to meet you " + NAME) 

print ( HOBBY + " is an interesting pastime for a " + AGE + " year old") 

 

''' Example output 

Hello, I am a chatbot, tell me about yourself 

What is your name? Mike 

How old are you? 36 

What is a hobby of yours? Fishing 

Nice to meet you Mike 

Fishing is an interesting pastime for a 36 year old  '''