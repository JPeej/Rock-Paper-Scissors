rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

import random

#List for user options
rps = [rock, paper, scissors]

#Getting user input and storing rps value in variable rps_user.
rps_user = rps[(int(input("What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors.")))]

#Getting computer's random choice and storing it in variable rps_comp.
rps_comp = rps[random.randint(0, 2)]

#Detereming which ASCII art to display for your choice.
if rps_user == rock:
  print(rock)
elif rps_user == paper:
  print(paper)
else:
  print(scissors)

print("Computer choose:")

#Determining which ASCII art to display the computer's choice.
if rps_comp == rock:
  print(rock)
elif rps_comp == paper:
  print(paper)
else:
  print(scissors)

#Determining who won.
if rps_user == rock and rps_comp == scissors:
  print("You win!")
elif rps_user == paper and rps_comp == rock:
  print("You win!")
elif rps_user == scissors and rps_comp == paper:
  print("You win!")
elif rps_user == rps_comp:
  print("You tied!")
else:
  print("You lost!")
