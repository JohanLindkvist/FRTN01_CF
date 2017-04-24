"Template for monitor-class"
import threading
import time

class Monitor(threading.Thread):
            
    def __init__(self, threadID, name):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        
    def run(self):
        print("Starting " + self.name)
        self.run=True
        i=0
        while(self.run==True):
            print("Monitor number %d" % i)
            i=i+1
            time.sleep(1)
        
        print("Exiting " + self.name)
        
    def destroy(self):
        self.run=False
        
    '''    
    def Home(self):
        #Todo
    def Go(self):
        #Todo 
    def Stop(self):
        #Todo
    def Land(self):
        #Todo
    def SetPDParam(self):
        #Todo
    def Plot2D(self):
        #Todo
    def Plot3D(self):
        #Todo
    def GetPos(self):
        #Todo
    def SetPos(self):
        #Todo
    def SetRef(self):
    '''
        