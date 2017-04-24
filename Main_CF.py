"main class to call other classes"
from Regul_CF import Regul_CF
import CF_GUI 
import threading
from tkinter import*

def __init__(self):
    self.x = 'Main method'

    
    
def main():
    #Create threads
    #regulator = multiprocessing.Process(target=regulate ,)
    #monitor = multiprocessing.Process(target=regulate,)
    
    regul = Regul_CF(1, "Regul Treahd")
   
    regul.start()
    GUI = CF_GUI.GUI_Thread(2, "GUI Tread")
    
    
    
 
    #Start threads
    #regulator.start()
    #monitor.start()

    #GUI.start()
    print("Tjenaaa")     
    regul.destroy()
    
    
    
def terminateAll():
    #terminate all of the processes
    pass

if __name__ == "__main__": main()