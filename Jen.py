# import create
import time
import math
import random

class PseudoCreate:
	def __init__(self, port=0):
		self.port = port
		self.fullMode = False
		self.moveSpeed = 0
		self.turnSpeed = 0
		self.lastTime = 0
	def __str__(self):
		return "PseudoCreate {\n\tport: %d\n\tfullMode: %s\n\tmoveSpeed: %dcm/s\n\tturnSpeed: %ddeg/s\n}" % (
			self.port, self.fullMode, self.moveSpeed, self.turnSpeed)
	def __repr__(self):
		return "PseudoCreate(port=%d)" % self.port
	def toFullMode(self):
		self.fullMode = True
	def go(self, moveSpeed, turnSpeed, debug=True):
		self.moveSpeed = moveSpeed
		self.turnSpeed = turnSpeed
		# For debugging purposes
		if self.lastTime:
			print("%dms elapsed" % (1e3 * (time.clock() - self.lastTime)))
		if debug:
			self.lastTime = time.clock()
			print("Setting speeds (%dcm/s, %ddeg/s)" % (moveSpeed, turnSpeed))
		else:
			self.lastTime = 0
	def stop(self, debug=True):
		if debug:
			print("Stopping")
		self.go(0, 0, debug=False)
	def move(self, distance, speed, debug=True):
		if debug:
			print("Moving %dmm at %dcm/s" % (distance, speed))
		self.go(speed, 0, debug=False)
		time.sleep(abs(distance / speed * 0.1))
		self.stop(debug=False)
	def turn(self, angle, speed, debug=True):
		if debug:
			print("Turning %ddeg at %ddeg/s" % (angle, speed))
		self.go(0, speed, debug=False)
		time.sleep(abs(angle / speed))
		self.stop(debug=False)
	def sensors(self, sensors):
		result = {}
		for i in range(len(sensors)):
			result[sensors[i]] = not random.randrange(0, 8)
		return result

class PseudoCreateModule:
	def __init__(self):
		self.BUMPS_AND_WHEEL_DROPS = 7
		self.WALL_IR_SENSOR = 8
		self.CLIFF_LEFT = 9
		self.CLIFF_FRONT_LEFT = 10
		self.CLIFF_FRONT_RIGHT = 11
		self.CLIFF_RIGHT = 12
		self.VIRTUAL_WALL = 13
		self.LSD_AND_OVERCURRENTS = 14
		self.INFRARED_BYTE = 17
		self.BUTTONS = 18
		self.DISTANCE = 19
		self.ANGLE = 20
		self.CHARGING_STATE = 21
		self.VOLTAGE = 22
		self.CURRENT = 23
		self.BATTERY_TEMP = 24
		self.BATTERY_CHARGE = 25
		self.BATTERY_CAPACITY = 26
		self.WALL_SIGNAL = 27
		self.CLIFF_LEFT_SIGNAL = 28
		self.CLIFF_FRONT_LEFT_SIGNAL = 29
		self.CLIFF_FRONT_RIGHT_SIGNAL = 30
		self.CLIFF_RIGHT_SIGNAL = 31
		self.CARGO_BAY_DIGITAL_INPUTS = 32
		self.CARGO_BAY_ANALOG_SIGNAL = 33
		self.CHARGING_SOURCES_AVAILABLE = 34
		self.OI_MODE = 35
		self.SONG_NUMBER = 36
		self.SONG_PLAYING = 37
		self.NUM_STREAM_PACKETS = 38
		self.REQUESTED_VELOCITY = 39
		self.REQUESTED_RADIUS = 40
		self.REQUESTED_RIGHT_VELOCITY = 41
		self.REQUESTED_LEFT_VELOCITY = 42
		# others just for easy access to particular parts of the data
		self.POSE = 100
		self.LEFT_BUMP = 101
		self.RIGHT_BUMP = 102
		self.LEFT_WHEEL_DROP = 103
		self.RIGHT_WHEEL_DROP = 104
		self.CENTER_WHEEL_DROP = 105
		self.LEFT_WHEEL_OVERCURRENT = 106
		self.RIGHT_WHEEL_OVERCURRENT = 107
		self.ADVANCE_BUTTON = 108
		self.PLAY_BUTTON = 109

try:
	create = create
except:
	create = PseudoCreateModule()

def angle_diff(a1, a2):
	return ((a2 % 360) - (a1 % 360) + 180) % 360 - 180

# jen = create.Create(7)
jen = PseudoCreate(7)
jen.toFullMode()

moves = []

def random_line():
	moves.append(["turn", random.randrange(0, 360)])
	jen.turn(moves[0][1], 20)
	moves.append(["go", 0])
	jen.go(20, 0)
	while True:
		sensors = jen.sensors([create.LEFT_BUMP, create.RIGHT_BUMP])
		if sensors[create.LEFT_BUMP] + sensors[create.RIGHT_BUMP]:
			break
		moves[1][1] += 10
		# print("0.05 seconds")
		time.sleep(0.05)
	jen.stop()
	print("Total distance: %dmm" % moves[1][1])
	jen.turn(180, 20)
	jen.move(moves[1][1], 20)
	jen.turn(angle_diff(0, -180 - moves[0][1]), 20)
	print(jen)

def zigzag(length=100):
	cycles = random.randrange(2, 5)
	angle = random.randrange(10, 40)
	for i in range(cycles):
		jen.turn(angle, 20)
		jen.move(length, 20)
		jen.turn((-angle * 2), 20)
		jen.move(length, 20)
		jen.turn(angle, 20)
	# Get back to original spot.
	jen.turn(180, 20)
	jen.move(length * 2 * cycles * math.cos(angle / 180 * math.pi), 20)
	jen.turn(180, 20)