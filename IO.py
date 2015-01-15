import RPi.GPIO as GPIO
from RPIO import PWM

class initBoard:
	def __init__(self):
		GPIO.setmode(GPIO.BCM/BOARD)
		#for descp, pin in GPIOMAP.e:
		#	GPIO.setup(pin,GPIO.OUT)
		for descp, pin in GPIOMAP.s:
			GPIO.setup(pin,GPIO.IN)
		PWM...

class Sensors:
	def __init__(self):
		pass
	def read(self):
		pass

class Effector:
	def __init__(self):
		pass
	def execute(self,rhs):
		pass

class Signaling:
	def __init__(self):
		pass
	def display(self,rhs):
		pass

GPIOMAP={'e':{'leftWing':12,'rightWing':13, 'queue':14,'deriv':15,'motor':16},'s':{
'accl':17, 'gyro':18,'alti':19,'GPS':20},'err':{}}
	
# servo = PWM.Servo()

# # Set servo on GPIO17 to 1200µs (1.2ms)
# servo.set_servo(17, 1200)

# # Set servo on GPIO17 to 2000µs (2.0ms)
# servo.set_servo(17, 2000)

# # Clear servo on GPIO17
# servo.stop_servo(17)