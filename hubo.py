from cs1robots import *
create_world()
hubo = Robot()


def turn_right():
    for i in range(3):
        hubo.turn_left()


hubo.set_trace("red")
hubo.move()
hubo.turn_left()
hubo.move()
turn_right()
hubo.move()
