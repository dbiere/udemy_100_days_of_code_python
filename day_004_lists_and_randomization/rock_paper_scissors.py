from random import randint

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

choices = [rock, paper, scissors]

user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors: "))
if user_choice not in range(0,3):
  print("That's not a valid choice. Ending game.")
  quit()

print(choices[user_choice])
print()

computer_choice = randint(0, 2)

print("Computer chose:")
print()
print(choices[computer_choice])
print()

if user_choice == computer_choice:
  print("It's a draw!")
elif computer_choice > user_choice or (computer_choice == 0 and user_choice == 2):
  print("The computer wins!")
else:
  print("You win!")
print()

