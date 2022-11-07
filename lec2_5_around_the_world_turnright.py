import time
from cs1robots import*
load_world("../worlds/amazing2.wld")
#load_world("../worlds/amazing3.wld")

hubo = Robot(beepers = 1)

def turn_right():
  for i in range(3):
    hubo.turn_left()

hubo.drop_beeper()
hubo.move()
while not hubo.on_beeper():
  if hubo.right_is_clear():
    turn_right()
    
  elif hubo.front_is_clear():
    hubo.move()
  else:
    hubo.turn_left()
  time.sleep(0.5)
