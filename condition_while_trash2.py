from cs1robots import *

# load_world("worlds/trash1.wld")
load_world("worlds/yardwork.wld")

hubo = Robot()
hubo.set_trace("red")


def turn_right():
    for i in range(3):
        hubo.turn_left()


while (True):
    if (hubo.on_beeper()):
        hubo.pick_beeper()
        hubo.carries_beepers()
        continue
    else:
        if (hubo.front_is_clear()):
            hubo.move()
        elif (hubo._x == 10):
            hubo.turn_left()
            hubo.move()
            if (hubo.on_beeper()):
                hubo.pick_beeper()
                hubo.carries_beepers()
            hubo.turn_left()

        elif (hubo._x == 1 and hubo._y != 1):
            turn_right()
            hubo.move()
            if (hubo.on_beeper()):
                hubo.pick_beeper()
                hubo.carries_beepers()
            turn_right()

    if (hubo._x == 1 and hubo._y == 10):
        while (hubo.on_beeper()):
            hubo.pick_beeper()
            hubo.carries_beepers()
        hubo.turn_left()
        for i in range(10):
            hubo.move()
    if (hubo._x == 1 and hubo._y == 1):
        hubo.drop_beeper()
        break
