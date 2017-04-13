"template for controller"
import time
import PD_CF



def __init__(self):
    self.x = 'Regul'
    

    
def setParameters(params):
    PD_CF.params=params
    
    
def setReference(ref):
    
    
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
    

    
    