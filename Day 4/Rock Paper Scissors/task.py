import random

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

# my method
'''     
list_item = [0, 1, 2]

random_list = random.randint(list_item[0], len(list_item)-1)

choose_one = input("Enter your choice. 0 for rock, 1 for paper, 2 for scissors: ")
if choose_one == '0':
    if random_list == list_item[0]:
        print("You choose rock, Computer choose rock. Draw Game!")
    elif random_list == list_item[1]:
        print("You choose rock, Computer choose paper. You Lose!")
    elif random_list == list_item[2]:
        print("You choose rock, Computer choose scissors. You Win!")
    else:
        print("Enter only 0, 1, or 2.")

elif choose_one == '1':
    if random_list == list_item[0]:
        print("You choose paper, Computer choose rock. You Win!")
    elif random_list == list_item[1]:
        print("You choose paper, Computer choose paper. Draw Game!")
    elif random_list == list_item[2]:
        print("You choose paper, Computer choose scissors. You Lose!")
    else:
        print("Enter only 0, 1, or 2.")

elif choose_one == '2':
    if random_list == list_item[0]:
        print("You choose scissor, Computer choose rock. You Lose!")
    elif random_list == list_item[1]:
        print("You choose scissor, Computer choose paper. You Win!")
    elif random_list == list_item[2]:
        print("You choose scissor, Computer choose scissors. Draw Game!")
    else:
        print("Enter only 0, 1, or 2.")

else:
    print("Enter only 0, 1, or 2.")
'''

# by pycharm
game_image = [rock, paper, scissors]
             # 0      1        2
user_choice = int(input("Enter your choice. 0 for rock, 1 for paper, 2 for scissors: "))

# user choose:
if user_choice >= 0 and user_choice <=2:
    print("You chose")
    print(game_image[user_choice])
else:
    print("Choose only 0, 1, or 2.")

# computer choose:
computer_choice = random.randint(0, 2)
print("Computer chose")
print(game_image[computer_choice])

# condition
if user_choice == 0 and computer_choice == 2:
    print("You win!")
elif computer_choice == 0 and user_choice == 2:
    print("You lose!")
elif user_choice > computer_choice:
    print("You win!")
elif computer_choice > user_choice:
    print("You lose!")
elif user_choice == computer_choice:
    print("Draw!")
elif user_choice >= 3 or user_choice < 0:
    print("Invalid choice! Quit the game.")
else:
    print("Enter only 0, 1, or 2.")


























