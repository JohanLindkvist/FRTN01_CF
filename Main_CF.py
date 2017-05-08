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

if __name__ == "__main__":
    _cf = Crazyflie()
    regul = Regul_CF(1, "Regul Thread", _cf)
	#monitor = Monitor(2, "Monitor Thread")
	#monitor.start()
    regul.start()
    GUI = CF_GUI.GUI_Thread(2, "GUI Tread",regul,_cf)
    regul.destroy()
	#monitor.destroy()
		  
