"template for controller"
import time
import threading
import PD_CF
import cflib
from cflib.crazyflie import Crazyflie

from cflib.crazyflie.log import LogConfig
from cflib.crazyflie.syncCrazyflie import SyncCrazyflie
from cflib.crazyflie.syncLogger import SyncLogger
import logging
import cflib.crtp  # noqa
import time
from datetime import datetime

class Regul_CF(threading.Thread):
    
    def __init__(self, threadID, name, _cf):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.ref=[0,0,0]
        self.pos=[0, 0, 0]
        self._cf=_cf
        self.go = False        
        
    def run(self):
        print("Starting " + self.name)
        self.run=True
        
        while(self.run):
            if(self.go):
                #self.pos = _cf.getPos(TODO)  //Activate when Ankare
                output = PD_CF.calcOutput(self.pos,self.ref)
                self._cf.commander.send_setpoint(output[0],output[1],0,output[2])
                PD_CF.updateState(self.pos)
            else:
                self._cf.commander.send_setpoint(0,0,0,0)
            time.sleep(0.005)
        self._cf.commander.send_setpoint(0, 0, 0, 0)
        # Make sure that the last packet leaves before the link is closed
        # since the message queue is not flushed before closing
        
        time.sleep(0.01)
        self._cf.close_link()        
    
    def Go(self):
        self.go = True
    
    def setParameters(self,params):
        PD_CF.params=params
    
    def destroy(self):
        self.run=False
        
    def setReference(self,ref):
        self.ref=ref
        
    def getPos(self):
        return self.pos

    def updatePos(self,  newPos):
        self.pos=newPos

    def land(self):
		#TODO
        pass
	
    def stop(self):
        self.go = False


