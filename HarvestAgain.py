from cs1robots import *

global count

load_world("hubo/worlds/harvest2.wld")

hubo = Robot()
hubo.set_trace("red")

count = 0


def turn_right():
    for i in range(3):
        hubo.turn_left()


def climb_up_one_stair():
    hubo.turn_left()
    hubo.move()


def harvest_left(i: int):
    for i in range(i):
        if (hubo.on_beeper()):
            hubo.pick_beeper()
        turn_right()
        hubo.move()
        hubo.turn_left()
        hubo.move()
    if (hubo.on_beeper()):
        hubo.pick_beeper()


def harvest_left2(i: int):
    for i in range(i):
        turn_right()
        hubo.move()
        hubo.turn_left()
        hubo.move()
        if (hubo.on_beeper()):
            hubo.pick_beeper()


def harvest_right(i: int):

    for i in range(i):
        hubo.turn_left()
        hubo.move()
        turn_right()
        hubo.move()
        if (hubo.on_beeper()):
            hubo.pick_beeper()


def harvest_down(i: int):
    for i in range(i):
        turn_right()
        hubo.move()
        hubo.turn_left()
        hubo.move()
        if (hubo.on_beeper()):
            hubo.pick_beeper()


def harvest_up(i: int):
    for i in range(i):
        hubo.turn_left()
        hubo.move()
        turn_right()
        hubo.move()
        if (hubo.on_beeper()):
            hubo.pick_beeper()


#######################################################
climb_up_one_stair()
count += 1
for i in range(5):
    hubo.move()

count += 5

harvest_left(5)
count += 2*5


turn_right()
hubo.move()
turn_right()
hubo.move()
if (hubo.on_beeper()):
    hubo.pick_beeper()
count += 2


harvest_right(4)
count += 2*4
harvest_down(5)
count += 2*5


turn_right()
hubo.move()
turn_right()
hubo.move()
if (hubo.on_beeper()):
    hubo.pick_beeper()

count += 2

harvest_up(3)
count += 2*3

harvest_left2(4)
count += 2*4

turn_right()
hubo.move()
turn_right()
hubo.move()
if (hubo.on_beeper()):
    hubo.pick_beeper()
count += 2


harvest_right(2)
count += 2*2
harvest_down(3)
count += 2*3

turn_right()
hubo.move()
turn_right()
hubo.move()
if (hubo.on_beeper()):
    hubo.pick_beeper()
count += 2

harvest_up(1)
harvest_left2(2)
count += 2*3

turn_right()
hubo.move()
turn_right()
hubo.move()
if (hubo.on_beeper()):
    hubo.pick_beeper()
harvest_down(1)

count += 2
count += 2*1

print(count)
