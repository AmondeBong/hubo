from cs1robots import *


load_world("worlds/harvest3.wld")

hubo = Robot()
hubo.set_trace("red")


def turn_right():
    for i in range(3):
        hubo.turn_left()


def harvest():
    if (hubo.on_beeper()):
        hubo.pick_beeper()
    else:
        if (hubo.front_is_clear()):
            hubo.move()
        elif (hubo.left_is_clear()):
            hubo.turn_left()


hubo.move()

while (True):
    if (hubo.on_beeper()):
        harvest()
    elif (not hubo.on_beeper()):
        if (hubo.front_is_clear()):
            if (hubo._x == 2 and hubo._y != 1):
                turn_right()
                hubo.move()
                harvest()
            else:
                hubo.move()
        elif (hubo.left_is_clear()):
            hubo.turn_left()
            hubo.move()
            harvest()
            hubo.turn_left()
        elif (hubo._x == 2 and hubo._y == 6):
            break
