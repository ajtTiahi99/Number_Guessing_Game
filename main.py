from art import logo
import random


def evaluate(guess,random_number):
  if random_number > guess:
    print("Too low")
    return False
  if random_number<guess:
    print("Too high")
    return False
  if random_number==guess:
    return True

print(logo)
print("Welcome to the Number Guessing Game!")
print("Guess the number I have in mind between 1 and 100.")
random_number = random.randint(1,100)
user_mode = input("Choose a difficulty level - 'Easy' or 'Hard': ").title()
if user_mode=='Easy':
  cnt = 10
  while cnt>0:
    print(f"You have {cnt} attempts to guess the number.")
    try:
      guess = int(input("Make a guess: "))
    except ValueError:
        print("You did not type anything! Try again")
        continue

    if evaluate(guess,random_number):
      print("You got it ! Guessed number is correct.")
      break
    cnt-=1
  if cnt==0:
    print("You have run out of Guesses. You Lose!")
elif user_mode=="Hard":
  cnt = 5
  while cnt>0:
    print(f"You have {cnt} attempts to guess the number.")
    try:
      guess = int(input("Make a guess: "))
    except ValueError:
        print("You did not type anything! Try again")
        continue

    if evaluate(guess,random_number):
      print("You got it ! Guessed number is correct.😁")
      break
    cnt-=1
  if cnt==0:
    print("You have run out of Guesses. You Lose!😟")
