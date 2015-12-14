# Jen Master File

import create
import random
import time
from math import pi

jen = create.Create(8, 3)

def movecircle(radius_m, speed_cmps):
	circum_cm = (2 * pi * radius_m) * 100
	circum_movetime_sec = circum_cm / speed_cmps
	deg_per_sec = -360 / circum_movetime_sec # Negative = turn clockwise
	radius_movetime_sec = radius_m / speed_cmps

	jen.move((radius_m * 100), speed_cmps)
	time.sleep(radius_movetime_sec)
	jen.stop()
	jen.turn(-90)
	jen.go(speed_cmps, deg_per_sec)
	time.sleep(circum_movetime_sec)
	jen.stop()
	jen.turn(-90)
	jen.move((radius_m * 100), speed_cmps)
	time.sleep(radius_movetime_sec)
	jen.stop()
	return

def moverandom():
	moves.append(["turn", random.randrange(0, 360)])
	jen.turn(moves[0][1], 20)
	moves.append(["go", 0])
	jen.go(20, 0)
	while True:
		sensors = jen.sensors([create.LEFT_BUMP, create.RIGHT_BUMP])
		if sensors[create.LEFT_BUMP] + sensors[create.RIGHT_BUMP]:
			break
		moves[1][1] += 10
		time.sleep(0.05)
	jen.stop()
	jen.turn(180, 20)
	jen.move(moves[1][1], 20)
	jen.turn(angle_diff(moves[0][1] + 180, 0), 20)