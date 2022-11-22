from cs1robots import *

# load_world("worlds/trash1.wld")
load_world("worlds/trash2.wld")

hubo = Robot()
hubo.set_trace("red")


def turn_right():
    for i in range(3):
        hubo.turn_left()


hubo.move()
while (True):
    if (hubo.on_beeper()):
        hubo.pick_beeper()
        hubo.carries_beepers()
        continue
    else:
        if (hubo.front_is_clear()):
            hubo.move()
        elif (hubo.right_is_clear()):
            turn_right()
        else:
            for i in range(2):
                hubo.turn_left()

    if (hubo._x == 1 and hubo._y == 2):
        hubo.drop_beeper()
        break
