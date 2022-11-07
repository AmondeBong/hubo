from pyrsistent import v
from cs1robots import *

load_world("hubo/worlds/harvest2.wld")

hubo = Robot()
hubo.set_trace("red")

count = 0


def turn_right():
    for i in range(3):
        hubo.turn_left()


def move():
    count += 1
    hubo.move()
    print(count)


def climb_up_one_stair():
    hubo.turn_left()
    hubo.move()


climb_up_one_stair()
for i in range(5):
    hubo.move()
