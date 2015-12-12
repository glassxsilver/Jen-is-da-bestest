#import create
import random
import time

#jen = create.Create(8, 3)

def movecustom(movelist=None):
	print('Enter w, a, s, or d for movement \nEnter q to finish')
	print('w and s move 15 centimeters, a and d turn 45 degrees')
	inkey = input('Enter values:\n')
	if movelist == None:
		movelist = []
		while inkey != 'q':
			if inkey == 'w' or inkey == 'a' or\
			inkey == 's' or inkey == 'd':
				movelist.append(inkey)
			inkey = input()
	for cmd in movelist:
		if cmd == 'w':
			jen.move(15, 15)
			time.sleep(1)
			jen.stop()
		elif cmd == 's':
			jen.move(-15,15)
			time.sleep(1)
			jen.stop()
		elif cmd == 'a':
			jen.turn(45)
		elif cmd == 'd':
			jen.turn(-45)
	return