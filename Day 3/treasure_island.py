print('''
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
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
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

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

#Write your code below this line 👇
direction = input('You are at a crossroad, where do you want to go? Type "left" or "right"\n ').lower()

if direction == "left":
  lake_input = input('You\'ve come to a lake. There is an island in the middle of the lake. Type "wait" to wait for a boat. Type "swim" to swim across.\n ').lower()
  if lake_input == "wait":
    color = input("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose?\n ").lower()
    if color == "red":
      print("You enter a room of beasts. Game Over!")
    elif color == "yellow":
      print("You found the treasure! You win!")
    else:
      print("You chose a door that doesn't exist. Game Over!")
  else:
    print("You get attacked by a shark. Game Over!")
else:
  print("You went the wrong way and got lost. Game Over!")

OR

direction = input("You are at a fork in the road. Would you like to go left to Wessex or Right to Daneland? \n").lower()

if direction == "right":
  print("You've been captured by the Danes. Game over.")
elif direction == "left":
  print("You have come to a frozen lake. You can cross the lake by foot or by skates")
  skates = input("Would you like to cross by skates or by foot? \n").lower()
  if skates == "foot":
    print("Oh no! The ice cracked from all your weight. Game over.")
  elif skates == "skates":
    sword_color = input("You have crossed the lake, successfully. You have found three swords. Red, Yellow, and Blue. Only one will help you survive. \n").lower()
    if sword_color == "red":
      print("You have burned your hand from the heat of the sword. Game over!")
    elif sword_color == "yellow":
      print("The sword broke. You cannot protect yourself. Game over!")
    elif sword_color == "blue":
      print("Congrats! This is the correct sword. You win!")
    else:
      print("invalid. Game Over!")

  
