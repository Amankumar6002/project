# project
import random
Stone = '''   
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)'''

# print("""
#     _______
# ---'   ____)
#       (_____)
#       (_____)
#       (____)
# ---.__(___)
# """)

paper = '''     
     _______
---'    ___ )____
           ______)
          _______)
         _______)
---.__________)'''

# print("""
#      _______
# ---'    ____)____
#            ______)
#           _______)
#          _______)
# ---.__________)
# """)

scissor = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)'''
game_image = [Stone, paper, scissor]
user_choice = int(input("Enter your choice: 0 for Stone, 1 for paper, 2 for scissor: "))
print(game_image[user_choice])
computer_choice = random.randint(0, 2)
print("computer choice")
print(game_image[computer_choice])
if user_choice >= 3 or user_choice < 0:
    print("enter valid choice! you lose")
else:
    if computer_choice == user_choice:
        print("it's draw")
    elif computer_choice == 0 and user_choice == 2:
        print("you lose!")
    elif computer_choice == 2 and user_choice == 0:
        print("you win.")
    elif computer_choice > user_choice:
        print("you lose!")
    elif computer_choice < user_choice:
        print("you win")
