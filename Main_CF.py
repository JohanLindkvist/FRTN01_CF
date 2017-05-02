"main class to call other classes"
from Regul_CF import Regul_CF
from Monitor_CF import Monitor
import CF_GUI 
import threading
from threading import Thread
from Tkinter import*
import cflib
from cflib.crazyflie import Crazyflie
#Supposed to remove an error 
import logging
logging.basicConfig(level=logging.ERROR)
        

def _connected(link_uri):
    """ This callback is called form the Crazyflie API when a Crazyflie
    has been connected and the TOCs have been downloaded."""

    # Start a separate thread to do the motor test.
    # Do not hijack the calling thread!
    #Thread(target=_ramp_motors).start()

def _connection_failed(link_uri, msg):
    """Callback when connection initial connection fails (i.e no Crazyflie
    at the specified address)"""
    print('Connection to %s failed: %s' % (link_uri, msg))

def _connection_lost(link_uri, msg):
    """Callback when disconnected after a connection has been made (i.e
    Crazyflie moves out of range)"""
    print('Connection to %s lost: %s' % (link_uri, msg))

def _disconnected(link_uri):
    """Callback when the Crazyflie is disconnected (called in all cases)"""
    print('Disconnected from %s' % link_uri)

def connectCF(_cf, link_uri):

    _cf.connected.add_callback(_connected)
    _cf.disconnected.add_callback(_disconnected)
    _cf.connection_failed.add_callback(_connection_failed)
    _cf.connection_lost.add_callback(_connection_lost)
    _cf.open_link(link_uri)	
    print('Connecting to %s' % link_uri) 

def __init__(self):
    self.x = 'Main method'
        

#Are we using this?? /Emil    
def terminateAll():
    #terminate all of the processes
    pass
    cflib.crtp.init_drivers(enable_debug_driver=False)
    # Scan for Crazyflies and use the first one found
    print('Looking for Crazyflie')
    available = cflib.crtp.scan_interfaces()
    print('Crazyflies found:')
    for i in available:
        print(i[0])
    if len(available) > 0:
		_cf = Crazyflie()
		connectCF(_cf,available[0][0])
		regul = Regul_CF(1, "Regul Thread",_cf)
		monitor = Monitor(2, "Monitor Thread")
		monitor.start()
		regul.start()
		GUI = CF_GUI.GUI_Thread(2, "GUI Tread",regul)
		return 0
    else:
		print("hello stupid world")
    regul.destroy()
    monitor.destroy()

if __name__ == "__main__":
    _cf = Crazyflie()
    regul = Regul_CF(1, "Regul Thread", _cf)
	#monitor = Monitor(2, "Monitor Thread")
	#monitor.start()
    regul.start()
    GUI = CF_GUI.GUI_Thread(2, "GUI Tread",regul,_cf)
    regul.destroy()
	#monitor.destroy()
		  
