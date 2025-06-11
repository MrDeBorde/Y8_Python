# 1b_Calculator.py 

''' Custom Calculator
→ A simple calculator that asks for two numbers and an operation (add, subtract, multiply, divide) and returns the result.

 '''

 

# A simple calculator that asks for two numbers and an operation  

# (add, subtract, multiply, divide) and returns the result. 

 

print ("I am an amazing calculator") 

NUM1 = input ("Please enter a number? ") 

OP = input("please enter an operator ( +,-,/,*) ?") 

NUM2 = input ("please input a second number? ") 

 

# this processes the inputs without using conditions (that would be later) 
# given as a suggestion to the task 

# These 3 lines given as assistance ?
#For the calculator you can use this code to process your inputs, 
#which joins the inputs into a string and then evaluates the result
INPUTS = [NUM1, OP, NUM2] 
EXPRESSION = ''.join(INPUTS) 
RESULT = eval(EXPRESSION) 


print ("the answer is") 
ANSWER = print(RESULT) 

 

''' Example Output 

I am an amazing calculator 

Please enter a number? 4 

please enter an operator ( +,-,/,*) ?+ 

please input a second number? 4 

the answer is 

8  '''