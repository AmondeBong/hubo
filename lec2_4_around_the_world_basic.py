import time
from cs1robots import *
# load_world("hubo/worlds/8queens.wld")
# load_world("../worlds/amazing2.wld")
load_world("hubo/worlds/amazing2.wld")

hubo = Robot(beepers=1)
time.sleep(1.0)

hubo.drop_beeper()

while not hubo.on_beeper():
    if hubo.front_is_clear():
        hubo.move()
    else:
        hubo.turn_left()
    time.sleep(0.5)
