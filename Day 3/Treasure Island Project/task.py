print(r'''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

direction = input("You are at a crossroad. Where do you want to go? ").lower()
if direction == "right":
    print("Fall into a hole! Game Over!")
elif direction == "left":
    action = input("You come to a lake. Do you want to 'swim' or 'wait'? ").lower()
    if action == 'swim':
        print("Attack by trout! Game Over!")
    elif action == 'wait':
        door = input("Which door you want to choose. red, yellow, blue ").lower()
        if door == 'red':
            print("Burn by Fire! Game Over!")
        elif door == 'blue':
            print("Attack by Monsters! Game Over!")
        elif door == 'yellow':
            print("You found the treasure! Congratulations!")
        else:
            print("Choose only from red, blue, yellow")
    else:
        print("Choose only from swim and wait")
else:
    print("Choose only from right and left")
