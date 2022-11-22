from cs1robots import *


load_world("worlds/hurdles3.wld")

hubo = Robot()
hubo.set_trace("red")


def turn_right():
    for i in range(3):
        hubo.turn_left()


def jump_one_hurdle():

    hubo.turn_left()
    hubo.move()
    turn_right()
    hubo.move()
    turn_right()
    hubo.move()
    hubo.turn_left()


while (not hubo.on_beeper()):

    if (hubo.front_is_clear()):
        hubo.move()
        if (hubo.on_beeper()):
            hubo.pick_beeper()
    elif (hubo.left_is_clear()):
        jump_one_hurdle()
        if (hubo.on_beeper()):
            hubo.pick_beeper()
