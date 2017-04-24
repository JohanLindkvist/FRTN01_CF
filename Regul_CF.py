"template for controller"
import time
import threading
import PD_CF


class Regul_CF(threading.Thread):
        
    def __init__(self, threadID, name):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
    
    def run(self):
        print("Starting " + self.name)
        
        i=0
        while(True):
            print("Regul number %d" % i)
            i=i+1
            time.sleep(1)
        
        print("Exiting " + self.name)
        
    def setParameters(params):
        PD_CF.params=params
        
        
    def setReference(ref):
        pass
        
    def getPos():
        pass
    
    def regulate(name, stop):
        i=0
        while(True):
            i=i+1
            print(i, name)
            time.sleep(0.5)
            if i==stop:
                break
    

    
    