"""
Created on Wed Apr 5 11:13:54 2017

@author: Nils
"""


#Init method

x = 'PD'
#K_x,K_xTd,K_y,K_yTd,K_z,K_zTd
params = [1,1,1,1,11000,1]
oldX=0
oldY=0
oldZ=0
output= 0
N= 10;
Beta=1
H = 0.05;
adx = params[1]/(params[1]+N*H)
ady = params[3]/(params[3]+N*H)
adz = params[5]/(params[5]+N*H) 
bdx = params[0]*adx*N
bdy = params[2]*ady*N
bdz = params[4]*adz*N
errorarray=[0,0,0]

   
# retrieve parameters
def getParam():
    return params

#calculate controlsignal, Bumpless transition
def calcOutput(pos, ref):
    
    errorarray[0] = ref[0] - pos[0]
    errorarray[1] = ref[1] - pos[1]
    errorarray[2] = ref[2] - pos[2]
    params[1] = adx*params[1]-bdx*(pos[0]-oldX)
    params[3] = ady*params[3]-bdy*(pos[1]-oldY)
    params[5] = adz*params[5]-bdz*(pos[2]-oldZ)
    outputRoll = params[0]*(Beta*errorarray[0])+params[1]
    outputPitch = params[2]*(Beta*errorarray[1])+params[3]
    outputThrust = params[4]*(Beta*errorarray[2])+params[5]
    if outputThrust > (0xFFFF-1):
        outputThrust = 65530
    if outputPitch > (0xFFFF-1):
        outputPitch = 65530
    if outputRoll > (0xFFFF-1):
        outputRoll = 65530
    return outputRoll,outputPitch,outputThrust

#update state after calculating (maybe not neccesary??)
def updateState(x,y,z):
    oldX=x
    oldY=y
    oldZ=z


    
