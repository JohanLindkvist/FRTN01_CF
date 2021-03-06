"""
Created on Mon Apr  3 11:13:54 2017

@authors:
  
Nils Espfors
Johan Lindqvist
Michael Gabassi
Emil Wåreus

"""

import time
import threading
import PD_CF
import cflib
from cflib.crazyflie import Crazyflie
from Tkinter import END
from cflib.crazyflie.log import LogConfig
from cflib.crazyflie.syncCrazyflie import SyncCrazyflie
from cflib.crazyflie.syncLogger import SyncLogger
import logging
import cflib.crtp  # noqa
import time
from datetime import datetime

logging.basicConfig(level=logging.ERROR)

class Regul_CF(threading.Thread):
    
    
    
    def __init__(self, threadID, name, _cf):
        threading.Thread.__init__(self)
        self.IsConnected = False
        self.threadID = threadID
        self.name = name
        self.ref=[0,0,0]
        self.pos=[0, 0, 0]
        self._cf=_cf
        self.go = False
        self.land = False
        self.output = []
        self.t0 = int(time.time())
        
        
    def run(self):
        print("Starting " + self.name)
        self.run=True
        
        while(self.run):
           
            if(self.go):
               
                self.output = PD_CF.calcOutput(self.pos,self.ref)
                self._cf.commander.send_setpoint(self.output[0],self.output[1],0,self.output[2])
                PD_CF.updateState(self.pos)
            elif(self.land):
                self.ref = [self.ref[0], self.ref[1],  self.ref[2]*0.95]
                self.output = PD_CF.calcOutput(self.pos,self.ref)
                self._cf.commander.send_setpoint(self.output[0],self.output[1],0,self.output[2])
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
        
    
    def _connection_failed(self,link_uri, msg):
        """Callback when connection initial connection fails (i.e no Crazyflie
        at the specified address)"""
        self.GUI.T.delete('1.0',  END)
        temp = 'Connection to ' + link_uri  +' failed: ' + msg
        self.GUI.T.insert(END,  temp)
        #print('Connection to %s failed: %s' + (link_uri, msg))

    def _connection_lost(self,link_uri, msg):
        """Callback when disconnected after a connection has been made (i.e
        Crazyflie moves out of range)"""
        self.GUI.T.delete('1.0',  END)
        temp = 'Connection to ' +  link_uri + ' lost: ' +  msg
        self.GUI.T.insert(END,  temp)
        #print('Connection to %s lost: %s' % (link_uri, msg))

    def _disconnected(self,link_uri):
        """Callback when the Crazyflie is disconnected (called in all cases)"""
        self.GUI.T.delete('1.0',  END)
        temp = 'Disconnected from ' + link_uri
        self.GUI.T.insert(END,  temp)
        #print('Disconnected from %s' % link_uri)
    
    def _connected(self, link_uri):
        """ This callback is called form the Crazyflie API when a Crazyflie
        has been connected and the TOCs have been downloaded."""

        # Start a separate thread to do the motor test.
        # Do not hijack the calling thread!
        #Thread(target=_ramp_motors).start()
    
    def connectCF(self):
        cflib.crtp.init_drivers(enable_debug_driver=False)
        
        self._lg_stab = LogConfig(name='Position', period_in_ms=100)
        self._lg_stab.add_variable('kalman.stateX', 'float')
        self._lg_stab.add_variable('kalman.stateY', 'float')
        self._lg_stab.add_variable('kalman.stateZ', 'float')
        
        #Scan for Crazyflies and use the first one found
        self.GUI.T.delete('1.0',  END)
        temp = 'Looking for Crazyflie'
        self.GUI.T.insert(END,  temp)
        #print('Looking for Crazyflie')
        self.available = cflib.crtp.scan_interfaces()
        self.GUI.T.delete('1.0',  END)
        temp = 'Crazyflies found'
        self.GUI.T.insert(END,  temp)
        #print('Crazyflies found:')
        for i in self.available:
            self.GUI.T.insert(END,  i[0])
            #print(i[0])

        if len(self.available) > 0:    
            self.link_uri=self.available[0][0]
            self._cf.connected.add_callback(self._connected)
            self._cf.disconnected.add_callback(self._disconnected)
            self._cf.connection_failed.add_callback(self._connection_failed)
            self._cf.connection_lost.add_callback(self._connection_lost)
            self._cf.open_link(self.link_uri)	
            self.IsConnected = True
            self.GUI.T.delete('1.0',  END)
            temp = 'Connecting to ' +  self.link_uri
            self.GUI.T.insert(END,  temp)
            #print('Connecting to %s' % self.link_uri) 
            
    def IsConnected(self):
        return self.IsConnected
        
    
    def _connected(self, link_uri):
        self.GUI.T.delete('1.0',  END)
        temp = 'Connected to Crazyflie'
        self.GUI.T.insert(END,  temp)
       
        try:
            self._cf.log.add_config(self._lg_stab)
            
            # This callback will receive the data
            self._lg_stab.data_received_cb.add_callback(self._stab_log_data)
            # This callback will be called on errors
            self._lg_stab.error_cb.add_callback(self._stab_log_error)
            # Start the logging
            self._lg_stab.start()
        except KeyError as e:
            print('Could not start log configuration,'
                  '{} not found in TOC'.format(str(e)))
        except AttributeError:
            print('Could not add Stabilizer log config, bad configuration.')

    def _stab_log_error(self, logconf, msg):
        """Callback from the log API when an error occurs"""
        print('Error when logging %s: %s' % (logconf.name, msg))

    def _stab_log_data(self, timestamp, data, logconf):
        """Callback froma the log API when data arrives"""
        #print([data['kalman.stateX'], data['kalman.stateY'], data['kalman.stateZ']]) #Uncomment this line to print the pos      
        self.pos = [data['kalman.stateX'], data['kalman.stateY'], data['kalman.stateZ']]
        
      
    def setGUI(self,  GUI):
        print("Init Regul GUI")
        self.GUI = GUI


