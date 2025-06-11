#2b_Hogwarts_House_Sorter.py
''' 🧙 2. Hogwarts House Sorter
Concepts: multiple if/elif conditions based on input
Task:
Ask the user a few personality questions (e.g., "Do you prefer books or sports?").
Based on their answers, sort them into one of the four Hogwarts houses.

🎯 Challenge: Use nested conditionals to make it more accurate. '''

brave   = input("Do you enjoy taking risks? (yes/no) ").strip().lower()
loyal   = input("Do you value loyalty above all? (yes/no) ").strip().lower()
clever  = input("Do you love solving puzzles? (yes/no) ").strip().lower()

# simple scoring
score_g = 0
score_r = 0
score_h = 0
score_s = 0

if brave == "yes":
    score_g += 1
    score_s += 1          # Slytherins can be daring too!
if loyal == "yes":
    score_h += 1
if clever == "yes":
    score_r += 1
    score_s += 1

# choose the highest score
if score_g >= max(score_r, score_h, score_s):
    house = "Gryffindor"
elif score_r >= max(score_g, score_h, score_s):
    house = "Ravenclaw"
elif score_h >= max(score_g, score_r, score_s):
    house = "Hufflepuff"
else:
    house = "Slytherin"

print("🎉 You belong in", house + "!")
