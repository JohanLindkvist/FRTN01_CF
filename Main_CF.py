"main class to call other classes"
from Regul_CF import Regul_CF
from Monitor_CF import Monitor
import CF_GUI 
import threading
from tkinter import*

def __init__(self):
    self.x = 'Main method'

    
    
def main():
    #Create threads
    #regulator = multiprocessing.Process(target=regulate ,)
    #monitor = multiprocessing.Process(target=regulate,)
    
    regul = Regul_CF(1, "Regul Thread")
    monitor = Monitor(2, "Monitor Thread")
    
    monitor.start()
    regul.start()
    GUI = CF_GUI.GUI_Thread(2, "GUI Tread",regul)
    
    
    
 
    #Start threads
    #regulator.start()
    #monitor.start()

    #GUI.start()
    print("Tjenaaa")     
    regul.destroy()
    monitor.destroy()
    
    
    
def terminateAll():
    #terminate all of the processes
    pass

if __name__ == "__main__": main()