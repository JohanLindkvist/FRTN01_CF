"""
Created on Wed Apr 5 11:13:54 2017

@author: Nils
"""


#Init method

x = 'PD'
#K_x,K_xTd,K_y,K_yTd,K_z,K_zTd
params = [0,0,0,0,50000, 0]
oldX=0
oldY=0
oldZ=0
Dx=0
Dy=0
Dz=0
output= 0
N= 10;
Beta=1
H = 0.005;
adx = params[1]/(params[1]+N*H)
ady = params[3]/(params[3]+N*H)
adz = params[5]/(params[5]+N*H) 
bdx = params[0]*adx*N
bdy = params[2]*ady*N
bdz = params[4]*adz*N
#errorarray=[0,0,0]

   
# retrieve parameters
#def getParam():
#    return params

#calculate controlsignal, Bumpless transition
def calcOutput(pos, ref):
    global Dx,  Dy,  Dz,  oldX,  oldY,  oldZ,  adx,  ady, adz,  bdx,  bdy,  bdz,  params,  beta
    errorarray[0] = ref[0] - pos[0]
    errorarray[1] = ref[1] - pos[1]
    errorarray[2] = ref[2] - pos[2]
    Dx = adx*Dx-bdx*(pos[0]-oldX)
    Dy = ady*Dy-bdy*(pos[1]-oldY)
    Dz = adz*Dz-bdz*(pos[2]-oldZ)
    outputRoll = params[0]*(Beta*errorarray[0])+Dx
    outputPitch = params[2]*(Beta*errorarray[1])+Dy
    outputThrust = params[4]*(Beta*errorarray[2])+Dz
    if outputThrust > (0xFFFF-1):
        outputThrust = 65530
    elif (outputThrust < 10000):
         print ("error: ",  outputThrust)
         outputThrust = 10001
    if outputPitch > (0xFFFF-1):
        outputPitch = 65530
    if outputRoll > (0xFFFF-1):
        outputRoll = 65530
    #print (outputRoll,  outputPitch,  outputThrust)
    #print(pos)
    return outputRoll,outputPitch,outputThrust

#update state after calculating (maybe not neccesary??)
def updateState(pos):
    global oldX,  oldY,  oldZ
    oldX=pos[0]
    oldY=pos[1]
    oldZ=pos[2]

def updateParams():
    global adx,  ady,  adz,  bdx,  bdy,  bdz, params,  N,  H
    adx = params[1]/(params[1]+N*H)
    ady = params[3]/(params[3]+N*H)
    adz = params[5]/(params[5]+N*H) 
    bdx = params[0]*adx*N
    bdy = params[2]*ady*N   
    bdz = params[4]*adz*N