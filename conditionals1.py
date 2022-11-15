from cs1robots import *


load_world("worlds/harvest3.wld")

hubo = Robot()
hubo.set_trace("red")


def turn_right():
    for i in range(3):
        hubo.turn_left()


def con(i: int):

    for i in range(i):
        if (not hubo.on_beeper()):
            if hubo.front_is_clear():
                hubo.move()
            elif hubo.left_is_clear():
                hubo.turn_left()
                hubo.move()
            elif hubo.right_is_clear():
                turn_right()
                hubo.move()

        if (hubo.on_beeper()):
            hubo.pick_beeper()


con(7)
for i in range(2):
    hubo.turn_left()
    con(5)
    turn_right()
    con(1)
    turn_right()
    con(6)
hubo.turn_left()
con(4)
