def turn_right():
    for movement in range(0,3):
        turn_left()
        
        
def jump():
    turn_left()
    move()
    for movement in range(0,2):
        turn_right()
        move()
    turn_left()
    
def main():
    while not at_goal():
        # Keep turning right
        if wall_in_front and right_is_clear():
            turn_right()
            move()
            continue
        if wall_on_right and front_is_clear():
            move()
            continue
        if front_is_clear() and right_is_clear():
            turn_right()
            move()
            continue
        
        if wall_in_front and wall_on_right():
            turn_left()
            continue


main()