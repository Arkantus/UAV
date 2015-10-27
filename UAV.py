import time
import os
import socket

class connector:
	def __init__(self):
		pass
	def aviable(self):
		pass
	def connect(self):
		pass
	def ready(self):
		pass
	def send(self):
		pass
	def getData(self):
		pass
	def closed(self):
		pass



class logger:
	def __init__(self):
		whatTime = time.strftime("%d_%m_%Y__%H_%M_%S", time.gmtime())
		self.logfile = open("~/"+whatTime+".log")
		os.mkdir("~/"+whatTime)
		self.logerror = open("~/"+whatTime+"/errors")
		self.loginfo = open("~/"+whatTime+"/info")
		self.logwarning = open("~/"+whatTime+"/warning")
		self.logdebug = open("~/"+whatTime+"/debug")

	def logtime(self):
		return time.strftime("%H %M %S", time.gmtime())

	def info(self,msg):
		#for i in [self.logfile, self.loginfo]:
		#	i.write(msg)
		self.loginfo.write(self.logtime()+" : "+msg)
		self.logfile.write(self.logtime()+" _info_ " +" : "+msg)

	def error(self,msg):
		self.logerror.write(self.logtime()+" : "+msg)
		self.logfile.write(self.logtime()+" _error_ " +" : "+msg)

	def warning(self,msg):
		self.logwarning.write(self.logtime()+" : "+msg)
		self.logfile.write(self.logtime()+" _warning_ " +" : "+msg)

	def debug(self,msg):
		self.logdebug.write(self.logtime()+" : "+msg)
		self.logfile.write(self.logtime()+" _debug_ " +" : "+msg)
