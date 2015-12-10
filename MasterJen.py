# Jen Master File

import create
import random
import time
from math import pi

jen = create.Create(7, FULL_MODE)

def movecircle(radius_m, speed_cmps):
	circum_cm = (2 * pi * radius_m) * 100
	circum_movetime_sec = circum_cm / speed_cmps
	deg_per_sec = -360 / circum_movetime_sec # Negative = turn clockwise
	radius_movetime_sec = radius_m / speed_cmps

	jen.move((radius_m * 1000), speed_cmps)
	time.sleep(radius_movetime_sec)
	jen.turn(-90)
	jen.go(speed_cmps, deg_per_sec)
	time.sleep(circum_movetime_sec)
	jen.turn(-90)
	jen.move((radius_m * 1000), speed_cmps)
	time.sleep(radius_movetime_sec)
	return