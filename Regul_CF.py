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
        self.land = False
        self.output = []
        self.landOutput = []
        
    def run(self):
        print("Starting " + self.name)
        self.run=True
        
        while(self.run):
            if(self.go):
                #self.pos = _cf.getPos(TODO)  //Activate when Ankare
                self.output = PD_CF.calcOutput(self.pos,self.ref)
                self._cf.commander.send_setpoint(self.output[0],self.output[1],0,self.output[2])
                PD_CF.updateState(self.pos)
                self.landOutput = self.output
            elif(self.land):
                self.landOutput = [self.landOutput[0], self.landOutput[1],  self.landOutput[2]*0.99]
                self._cf.commander.send_setpoint(self.landOutput[0],self.landOutput[1],0,self.landOutput[2])
                PD_CF.updateState(self.pos)
            else:
                self._cf.commander.send_setpoint(0,0,0,0)
            time.sleep(0.033)
        self._cf.commander.send_setpoint(0, 0, 0, 0)
        # Make sure that the last packet leaves before the link is closed
        # since the message queue is not flushed before closing
        
        time.sleep(0.033)
        self._cf.close_link()        
    
    def Go(self):
        self.go = True
        self.land = False
    
    def Land(self):
        self.go = False
        self.land = True

    def setParameters(self,params):
        PD_CF.params=params
        print(PC_CF.params)
    
    def destroy(self):
        self.run=False
        
    def setReference(self,ref):
        self.ref=ref
        
    def getPos(self):
        return self.pos

    def updatePos(self,  newPos):
        self.pos=newPos
	
    def stop(self):
        self.go = False
        self.land = False


