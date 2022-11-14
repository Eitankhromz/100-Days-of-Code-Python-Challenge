def turn_right():
    turn_left()
    turn_left()
    turn_left()

def jump():
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()

for step in range (6):
    jump()

#OR

# def turn_right():
#     turn_left()
#     turn_left()
#     turn_left()

# def jump():
#     move()
#     turn_left()
#     move()
#     turn_right()
#     move()
#     turn_right()
#     move()
#     turn_left()
# steps = 0
# while steps < 6:
#     if at_goal():
#         break
#     else:
#         jump()
#         steps+=1


OR

def turn_around():
    turn_left()
    turn_left()

def turn_right():
    turn_left()
    turn_left()
    turn_left()

def hurdle():
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()

for jumps in range(6):
    hurdle()
OR

number_of_hurdles = 6
while number_of_hurdles > 0:
    hurdle()
    number_of_hurdles-=1
