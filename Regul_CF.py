"template for controller"
import time
import threading
import PD_CF
import cflib
from cflib.crazyflie import Crazyflie


class Regul_CF(threading.Thread):
    
    def __init__(self, threadID, name, _cf):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.ref=[0,0,0]
		self._cf=_cf
  
	def run(self):
		print("Starting " + self.name)
		self.run=True
		while(self.run):
			self.pos = _cf.getPos(TODO)
			output = PD_CF.calcOutput([0,0,0],self.ref)
			self._cf.commander.send_setpoint(output(0),output(1),0,output(2))

	def setParameters(self,params):
		PD_CF.params=params
    
    def destroy(self):
        self.run=False
        
    def setReference(self,ref):
		self.ref=ref
        
    def getPos(self):
		return self.pos

    def land(self):
		
		#TODO
		pass
	
    def stop(self):
	#TODO
	pass
		
    
    