import create
import time
jen = create.Create(7)
jen.toFullMode()

prog = input("Which program?")
if prog == "1":
	for x in range(4):
		jen.move(100, 20)
		if x == 3:
			break
		jen.turn(-90, 20)
elif prog == "2":
	jen.go(20, 0)
	while True:
		sensors = jen.sensors([create.LEFT_BUMP, create.RIGHT_BUMP])
		if sensors[create.LEFT_BUMP] + sensors[create.RIGHT_BUMP]:
			break
		time.sleep(0.05)
	jen.stop()