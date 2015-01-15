import UAV
import IO
from RPIO import PWM

global looper

@asyncio.coroutine
def runAsyncLoopSensorsSend():
	while True:
		yield from asyncio.sleep(0.01)
		sensors = IO.Sensors.read()
		if uc.ready():
			uc.send(sensors)

@asyncio.coroutine
def runAsyncLoopEffectorRcv():
	action = UAV.effector()
	action = yield from uc.getData()
	UAV.act(action)
	if action.stop():
		global looper = False
	return runAsyncLoopEffectorRcv()

def main():

	uc = UAV.connector()
	ul = UAV.logger()

	while( not uc.aviable() ):
		ul.error("No connection found")
	uc.connect(ue, UAV.remote)

	runAsyncLoopSensorsSend(uc)
	runAsyncLoopEffectorRcv(uc)

	while(not uc.closed()):
		continue

	if uc.broken():
		pass
		#ICi c'est caca
	else:
		ul.info('End Session')



		