from cs1robots import *
create_world()
hubo = Robot()
hubo.set_trace("red")


def turn_right():
    for i in range(3):
        hubo.turn_left()


def zigzag():
    for i in range(9):
        hubo.move()
    turn_right()
    hubo.move()
    turn_right()
    for i in range(9):
        hubo.move()
    hubo.turn_left()
    hubo.move()


for i in range(5):
    hubo.turn_left()
    zigzag()
