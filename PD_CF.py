"""
Created on Wed Apr 5 11:13:54 2017

@author: Michael
"""


Kx=0
Ky=0
Kz=0

Tdx=0
Tdy=0
Tdz=0

params = [Kx, Ky, Kz, Tdx, Tdy, Tdz]

D=0
y=0



#Init method
def __init__(self):
    self.x = 'PD'
    print(params)
    
    
#calculate controlsignal
def calcOutput(): 
    print(params)