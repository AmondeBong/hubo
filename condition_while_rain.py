from cs1robots import *


load_world("worlds/rain2.wld")

hubo = Robot(beepers=10, avenue=3, street=6, orientation="E")
hubo.set_trace("red")


def turn_right():
    for i in range(3):
        hubo.turn_left()


hubo.turn_left()
hubo.move()

while (True):

    if (hubo.front_is_clear() and hubo.left_is_clear()):
        hubo.drop_beeper()
        hubo.move()

    elif (hubo.front_is_clear()):
        hubo.move()

    elif (not hubo.front_is_clear() and not hubo.left_is_clear()):
        turn_right()
        if (hubo.facing_north() and not hubo.left_is_clear()):
            hubo.move()
            hubo.turn_left()

    if (hubo._x == 3 and hubo._y == 5):
        turn_right()
        hubo.move()
        hubo.turn_left()
        break
