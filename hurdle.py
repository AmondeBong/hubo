from cs1robots import *
load_world("hubo/worlds/hurdles1.wld")
hubo = Robot()
hubo.set_trace("red")


def turn_right():
    for i in range(3):
        hubo.turn_left()


def hurdle_1():
    hubo.move()
    hubo.turn_left()
    hubo.move()
    turn_right()
    hubo.move()
    turn_right()
    hubo.move()
    hubo.turn_left()


while (hubo.front_is_clear()):
    for i in range(4):
        hurdle_1()
    hubo.move()
    turn_right()
    hubo.pick_beeper()
