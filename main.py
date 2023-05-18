#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

from art import logo
from replit import clear
import random

def final_answer(size,randomnumber):
  while size>=0:
    print(f"You have {size} attempts remaining to guess the number.")
    guess = int(input("Make a guess: "))
    if(guess>randomnumber):
     
      if(size>1):
        print("Too high.")
        print("Guess agin")
        
      size-=1
    elif(guess<randomnumber):
      if(size>1):
        print("Too low.")
        print("Guess agin")
      size-=1
    elif(guess==randomnumber):
      print(f"You got it! The answer was {randomnumber}.")
      size==0
      break
    if(size==0 and guess==randomnumber):
      print(f"Pssst, the correct answer is {randomnumber}")
      break
    elif(size==0 and guess!=randomnumber):
      print("You've run out of guesses, you lose.")
      break


      
def check_answer(level,randomnumber):
  hard_size=5
  easy_size=10
  if(level=="hard"):
    final_answer(hard_size,randomnumber)
  else:
    final_answer(easy_size,randomnumber)
def logo1():
  print(logo)
  print("Welcome to the Number Guessing Game!")
  print("I'm thinking of a number between 1 and 100.")

  
randomnumber=random.randint(1,100)
while True:
 
  logo1()
  level = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
  clear()
  # logo1()
  if(level=="hard"):
    check_answer(level,randomnumber)
    
  elif(level=="easy"):
    check_answer(level,randomnumber)
    pass
  else:
    print("You write some wrong")
  