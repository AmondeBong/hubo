
from cs1robots import *
create_world()
hubo = Robot(orientation='N', avenue=7, street=4)
hubo.set_trace("red")


def turn_right():
    for i in range(3):
        hubo.turn_left()


while (True):

    if (hubo.facing_north()):
        hubo.turn_left()
        hubo.turn_left()
    elif (hubo._x == 1):
        hubo.turn_left()
        hubo.move()
    elif (hubo._y == 1):
        turn_right()
        hubo.move()
    elif (hubo._x == 10):
        turn_right()
        hubo.move()
    elif (hubo.front_is_clear()):
        hubo.move()

    if (hubo._x == 1 and hubo._y == 1):
        break
