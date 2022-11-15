from cs1robots import *


load_world("worlds/harvest3.wld")

hubo = Robot(beepers=6)
hubo.set_trace("red")


def turn_right():
    for i in range(3):
        hubo.turn_left()


def con(i: int):

    for i in range(i):
        if (not hubo.on_beeper()):
            if hubo.front_is_clear():
                hubo.drop_beeper()

            elif hubo.left_is_clear():
                hubo.drop_beeper()
                hubo.turn_left()

            elif hubo.right_is_clear():
                hubo.drop_beeper()
                turn_right()

        if (hubo.on_beeper()):
            if hubo.front_is_clear():
                hubo.move()
            elif hubo.left_is_clear():
                hubo.turn_left()
            elif hubo.right_is_clear():
                turn_right()


def turn_up():
    for j in range(1):
        hubo.turn_left()
        con(5)
        turn_right()
        con(1)
        turn_right()


hubo.move()
con(7)
turn_up()
con(7)
turn_up()
con(6)
hubo.turn_left()
con(6)
