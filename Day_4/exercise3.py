# 🚨 Don't change the code below 👇
row1 = ["⬜️","⬜️","⬜️"]
row2 = ["⬜️","⬜️","⬜️"]
row3 = ["⬜️","⬜️","⬜️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")
# 🚨 Don't change the code above 👆

#Write your code below this row 👇
vertical = int(position[0])
horizontal = position[1]

if horizontal == "1":
    row1[vertical-1] = "X"
elif horizontal =="2":
    row2[vertical-1] = "X"
else:
    row3[vertical-1] = "X"

#OR

column = int(position[0]) #2
row = int(position[1]) #3

#variable[row][column]
map[row - 1][column - 1] ="X"

#Write your code above this row 👆

# 🚨 Don't change the code below 👇
print(f"{row1}\n{row2}\n{row3}")
