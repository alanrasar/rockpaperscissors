import random

computerAnswer == "NIL"

def computerChoice():
  randomNum = random.randint(1,3)
  if randomNum == 1:
    computerAnswer == "rock"
  elif randomNum == 2:
    computerAnswer == "paper"
  else:
    computerAnswer == "scissors"
  
  



playerInput = input("Rock, paper or scissors?")
