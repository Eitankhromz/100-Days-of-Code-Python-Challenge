def turn_right():
    turn_left()
    turn_left()
    turn_left()

def jump():
    turn_right()
    move()
    
while front_is_clear():
    move() 
turn_left()
    
while not at_goal():
    if right_is_clear():
        jump()
    elif wall_in_front():
       turn_left()
    elif wall_on_right():
        move()
    
