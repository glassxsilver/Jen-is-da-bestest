import create
import random
import time

jen = create.Create(8, 3)

def movecustom(livemode, movelist=None):
	print('Enter w, a, s, or d for movement \nEnter q to finish')
	print('w and s move 15 centimeters, a and d turn 45 degrees')
	inkey = input('Enter values:\n')
	if livemode == 0: # list mode
		if movelist == None: # when not given a list, make list
			movelist = []
			while inkey != 'q':
				if inkey == 'w' or inkey == 'a' or\
				inkey == 's' or inkey == 'd':
					movelist.append(inkey)
				inkey = input()
		for cmd in movelist: # always executes if in list mode
			doinput(cmd)
	else: # live mode
		while inkey != 'q': # doesn't matter if input isn't w/a/s/d
			# inkey=input().....shouldn't the user be putting in keys if its live mode? 
					# Or is it all the keys they initially put in?
			doinput(inkey)
	return

def doinput(movekey): # receives anything, only moves if string of w/a/s/d
	if movekey == 'w':
		jen.move(15, 15) # move forwards 15cm in 1 second
		time.sleep(1)
		jen.stop()
	elif cmd == 's':
		jen.move(-15,15) # move backwards 15cm in 1 second
		time.sleep(1)
		jen.stop()
	elif cmd == 'a':
		jen.turn(45) # turn 45* CCW
	elif cmd == 'd':
		jen.turn(-45) # turn 45* CW
	return
