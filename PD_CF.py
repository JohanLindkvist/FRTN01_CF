"""
Created on Wed Apr 5 11:13:54 2017

@author: Nils
"""


#Init method

x = 'PD'
#K_x,K_xTd,K_y,K_yTd,K_z,K_zTd
params = [11,1.1,11, 1.1,10000, 1.4]
oldX=0
oldY=0
oldZ=0
Dx=0
Dy=0
Dz=0
output= 0
N= 8;
Beta=1
H = 0.033;
adx = params[1]/(params[1]+N*H)
ady = params[3]/(params[3]+N*H)
adz = params[5]/(params[5]+N*H) 
bdx = params[0]*adx*N
bdy = params[2]*ady*N
bdz = params[4]*adz*N
errorarray=[0,0,0]
I = 4
ZTi=300
   
# retrieve parameters
#def getParam():
#    return params

#calculate controlsignal, Bumpless transition
def calcOutput(pos, ref):
    global Dx,  Dy,  Dz,  oldX,  oldY,  oldZ,  adx,  ady, adz,  bdx,  bdy,  bdz,  params,  beta, errorarray, I, ZTi
    errorarray[0] = ref[0] - pos[0]
    errorarray[1] = ref[1] - pos[1]
    errorarray[2] = ref[2] - pos[2]
    Dx = adx*Dx-bdx*(pos[0]-oldX)
    Dy = ady*Dy-bdy*(pos[1]-oldY)
    Dz = adz*Dz-bdz*(pos[2]-oldZ)
    outputPitch = params[0]*(Beta*errorarray[0])+Dx
    outputRoll = params[2]*(Beta*errorarray[1])+Dy
    outputThrust = params[4]*(Beta*errorarray[2]+I)+ Dz
    if outputThrust > (65001):
        print ('Thrust to High: ',  outputThrust)
        outputThrust = 65000
    elif (outputThrust < 35000):
         print ('Thrust to low: ',  outputThrust)
         outputThrust = 35001
    if outputPitch > (11):
        print ('Pitch to High: ',  outputPitch)
        outputPitch = 10
    elif (outputPitch < -11):
        print ("Pitch to low: ",  outputPitch)
        outputPitch = -10
    if outputRoll > (11):
        print ("Roll to High: ",  outputRoll)
        outputRoll = 10
    elif outputRoll < -11:
        print ("Roll to low: ",  outputRoll)
        outputRoll = -10
    #print (-outputRoll,  outputPitch,  outputThrust)
    #print(pos)
    return -outputRoll,outputPitch,outputThrust

#update state after calculating (maybe not neccesary??)
def updateState(pos):
    global oldX,  oldY,  oldZ, I, errorarray, ZTi
    I = I + errorarray[2]/ZTi
    #print(I)
    if (I > 70000/params[4]):
        print("Antiwindup activated!")
        I =  70000/params[4]
    elif (I < 0):
        I =0
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
