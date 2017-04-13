"main class to call other classes"
from Regul_CF import regulate
import GUI_CF
import multiprocessing


def __init__(self):
    self.x = 'Main method'

    
    
def main():
    #Create threads
    regulator = multiprocessing.Process(target=regulate ,args=('Regulator',4,))
    monitor = multiprocessing.Process(target=regulate, args=('Monitor',8,))
    GUI = multiprocessing.Process(target=GUI_CF.main, args=('Monitor',8,))
 
    #Start threads
    regulator.start()
    monitor.start()
    GUI.start()
         
    
    
def terminateAll():
    #terminate all of the processes
    pass

if __name__ == "__main__": main()