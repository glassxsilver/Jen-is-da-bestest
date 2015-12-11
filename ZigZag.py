import create
import random
import time


jen = create.Create()


def zigzag(length=15):
  angle = random.choice(range(1,180))
  cycles = random.choice(range(1,11))
  for i in range(cycles):
    if i ==0:
      jen.turn(angle, 20)
    jen.move(length,20)
    jen.turn((-angle*2),20)
    jen.move((2*length),20)
    jen.turn((angle*2),20)
    jen.move(length,20)
    if i ==cycles-1:
      jen.turn((180-angle),20)
    jen.stop()
  # Get back to original spot.
  jen.stop()
  return
	
		
