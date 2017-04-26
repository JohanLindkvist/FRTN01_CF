"""
Created on Wed Apr 5 11:13:54 2017

@author: Nils
"""
import threading
import time
class PD_CF(threading.Thread):
    
    #Init method
    def __init__(self, threadID, name):
    self.x = 'PD'
    threading.Thread.__init__(self)
    self.threadID = threadID
    self.name = name
    #K_x,K_xTd,K_y,K_yTd,K_z,K_zTd
    self.params = [0,0,0,0,0,0]
    self.oldX=0
    self.oldY=0
    self.oldZ=0
    self.output= 0
    self.N= 10;
    self.Beta=1
    self.H = 0.05;
    self.adx = params[1]/(params[1]+N*H)
    self.ady = params[3]/(params[3]+N*H)
    self.adz = params[5]/(params[5]+N*H) 
    self.bdx = params[0]*adx*N
    self.bdy = params[2]*ady*N
    self.bdz = params[4]*adz*N

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
        
    # retrieve parameters
    def getParam():
        return params
    
    #calculate controlsignal, Bumpless transition
    def calcOutput(newPosarray, yrefarray):
        errorarray = yrefarray - newPosarray
        params[1] = adx*params[1]-bdx*(newPosarray[0]-oldX)
        params[3] = ady*params[3]-bdy*(newPosarray[1]-oldY)
        params[5] = adz*params[5]-bdz*(newPosarray[2]-oldZ)
        outputX = params[0]*(Beta*errorarray[0])+params[1]
        outputY = params[2]*(Beta*errorarray[1])+params[3]
        outputZ = params[4]*(Beta*errorarray[2])+params[5]
        return outputX,outputY,outputZ
        # TODO

    #update state after calculating (maybe not neccesary??)
    def updateParam(x,y,z):
        oldX=x
        oldY=y
        oldZ=z
    
    