# Jen Master File
# ~18 seconds to turn 360 degrees

import create
import random
import time
from math import pi, cos, fabs

jen = create.Create(3, 3)

def angle_diff(a1, a2):
	return ((a2 % 360) - (a1 % 360) + 180) % 360 - 180

def movecircle(radius_m, forward=1, speed_cmps=20): # forward should be 1 or -1
	circum_cm = fabs((2 * pi * radius_m) * 100)
	circum_movetime_sec = fabs(circum_cm / speed_cmps)
	deg_per_sec = -360 / circum_movetime_sec * forward # Negative = turn clockwise
	radius_movetime_sec = fabs(radius_m / speed_cmps)
	
	jen.move((radius_m * 100 * forward), speed_cmps)
	time.sleep(radius_movetime_sec)
	jen.stop()
	jen.turn(-90 * forward, 90)
	jen.go(speed_cmps * forward, deg_per_sec)
	time.sleep(circum_movetime_sec)
	jen.turn(-90 * forward, 90)
	jen.move((radius_m * 100 * forward), speed_cmps)
	time.sleep(radius_movetime_sec)
	jen.stop()
	return

def random_line():
	moves = []
	moves.append(["turn", random.randrange(0, 360)])
	if moves[0][1] > 180:
		moves[0][1] = (moves[0][1] - 180) * -1
	jen.turn(moves[0][1], 90)
	tim = fabs(moves[0][1] / 90)
	time.sleep(tim)
	moves.append(["go", 0])
	jen.go(20, 0)
	while True:
		sensors = jen.sensors([create.LEFT_BUMP, create.RIGHT_BUMP])
		if sensors[create.LEFT_BUMP] + sensors[create.RIGHT_BUMP]:
			break
		moves[1][1] += 1
		time.sleep(0.05)
	jen.stop()
	jen.turn(180, 90)
	time.sleep(2)
	jen.move(moves[1][1], 30)
	tim = moves[1][1] / 30
	time.sleep(tim)
	jen.turn(angle_diff(0, -180 - moves[0][1]), 90)
	time.sleep(angle_diff(0, -180 - moves[0][1]) / 90)
	#print(jen) # Why?
	return

def zigzag(length_cm=100, randmode = 1, cycles=None):
	angle = 45
	if cycles==None:
		cycles = random.randrange(2, 5)
	if randmode == 1:
		angle = random.randrange(10, 40)
	for i in range(cycles):
		jen.turn(angle, angle)
		jen.move(length_cm, 90)
		jen.turn((-angle * 2), angle)
		jen.move(length_cm, 90)
		jen.turn(angle, angle)
	# Get back to original spot.
	jen.turn(180, 90)
	jen.move(length_cm * 2 * cycles * cos(angle / 180 * pi), 20)
	jen.turn(180, 90)

def movecustom(livemode, movelist=None):
	print('Enter w, a, s, or d for movement \nEnter q to finish')
	print('w and s move 15 centimeters, a and d turn 45 degrees')
	if livemode == 0: # list mode
		if movelist == None: # when not given a list, make list
			inkey = input('Enter values:\n')
			movelist = []
			while inkey != 'q':
				if inkey == 'w' or inkey == 'a' or\
				inkey == 's' or inkey == 'd':
					movelist.append(inkey)
				inkey = input()
		for cmd in movelist: # always executes if in list mode
			doinput(cmd)
	else: # live mode
		inkey = input('Enter values:\n')
		while inkey != 'q': # doesn't matter if input isn't w/a/s/d
			doinput(inkey)
			inkey = input()
	return

def doinput(movekey): # receives anything, only moves if string of w/a/s/d
	if movekey == 'w':
		jen.move(15, 15) # move forwards 15cm in 1 second
		jen.stop()
	elif movekey == 's':
		jen.move(-15,15) # move backwards 15cm in 1 second
		jen.stop()
	elif movekey == 'a':
		jen.turn(45, 90) # turn 45* CCW
	elif movekey == 'd':
		jen.turn(-45, 90) # turn 45* CW
	return
