import random
import math

print("Welcome to the Lucky Math Quiz Game!\nYou will get random math problems. Try to answer correctly!")
score = 0
Question = 3

for i in range(Question):
  num = random.randint(2, 10)
  operation = random.choice(["sqrt", "factorial", "square"])
  print(f"\n\n\nQuestion {i+1}")
  if operation == "sqrt":
    print(f"What is the square root of {num*num}? (Round to 2 decimals)")
    ans = input("Your answer: ").strip()
    if ans.replace(".", "", 1).isdigit() and float(ans) == round(math.sqrt(num*num), 2):
      print("Correct!")
      score += 1
    else:
      print(f"Wrong! Correct answer: {round(math.sqrt(num*num), 2)}")
  elif operation == "factorial":
    print(f"What is the factorial of {num}?")
    ans = input("Your answer: ").strip()
    if ans.isdigit() and int(ans) == math.factorial(num):
      print("Correct!")
      score += 1
    else:
      print(f"Wrong! Correct answer: {math.factorial(num)}")
    
  elif operation == "square":
    print(f"What is {num} squared?")
    ans = input("Your answer: ").strip()
    if ans.isdigit() and int(ans) == num**2:
      print("Correct!")
      score += 1
    else:
      print(f"Wrong! Correct answer: {num**2}")
print(f"\n\nYour final score is: {score}/{Question}")
