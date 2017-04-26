"template for controller"
import time
import threading
import PD_CF


class Regul_CF(threading.Thread):
    
    def __init__(self, threadID, name):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.ref=[0,0,0]
        
  
    def run(self):
        print("Starting " + self.name)
        self.run=True
        i=0
        while(self.run==True):
            print("Regulating")
            self.regulate("regulatdor",300)
            i=i+1
            time.sleep(1)
        
        print("Exiting " + self.name)
        
    def setParameters(self,params):
        PD_CF.params=params
    
    def destroy(self):
        self.run=False
        
    def setReference(self,ref):
        
    
        self.ref=ref
        
    def getPos():
        pass
    
    def regulate(self, name, stop):
        i=0
        while(self.run):
            i=i+1
            print(PD_CF.calcOutput([0,0,0],self.ref))
            time.sleep(0.5)
            if i==stop:
                break
    

    
    