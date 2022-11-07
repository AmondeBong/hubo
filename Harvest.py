from cs1robots import *
load_world("hubo/worlds/harvest1.wld")
hubo = Robot()
hubo.set_trace("red")


def turn_right():
    for i in range(3):
        hubo.turn_left()


def Harvest():
    while (hubo.front_is_clear()):
        hubo.move()
        if (hubo.on_beeper()):
            hubo.pick_beeper()
    hubo.turn_left()
    hubo.move()
    if (hubo.on_beeper()):
        hubo.pick_beeper()
    hubo.turn_left()
    while (hubo.front_is_clear()):
        hubo.move()
        if (hubo.on_beeper()):
            hubo.pick_beeper()
    turn_right()
    hubo.move()
    turn_right()


for i in range(6):
    Harvest()
