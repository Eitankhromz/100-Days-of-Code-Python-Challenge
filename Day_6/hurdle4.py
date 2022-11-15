def turn_right():
    turn_left()
    turn_left()
    turn_left()

def jump():
    turn_right()
    move()
    turn_right()
    move()
    
while not at_goal():
    if right_is_clear():
        jump()
    elif front_is_clear():
        move()
    elif wall_in_front():
        turn_left()

  OR

def turn_around():
    turn_left()
    turn_left()

def turn_right():
    turn_left()
    turn_left()
    turn_left()

def hurdle():
    turn_left()
    
    while wall_on_right():
        move()
        
    turn_right()
    move()
    turn_right()
    
    while front_is_clear():
        move()
    
    turn_left()
    
    
while not at_goal():
    if wall_in_front():
        hurdle()
    else:
        move()
    
    
    
    
