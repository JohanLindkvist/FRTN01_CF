"main class to call other classes"
from Regul_CF import regulate
import CF_GUI
import multiprocessing


def __init__(self):
    self.x = 'Main method'

    
    
def main():
    #Create threads
    #regulator = multiprocessing.Process(target=regulate ,)
    #monitor = multiprocessing.Process(target=regulate,)
    GUI = multiprocessing.Process(target=CF_GUI.__init__,)
 
    #Start threads
    #regulator.start()
    #monitor.start()
    GUI.start()
         
    
    
def terminateAll():
    #terminate all of the processes
    pass

if __name__ == "__main__": main()