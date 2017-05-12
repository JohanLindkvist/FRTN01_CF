
"""
Created on Mon Apr  3 11:13:54 2017

@authors:
  
Nils Espfors
Johan Lindqvist
Michael Gabassi
Emil Wåreus

"""


# This class is not currently used. The skeleton could be used to implement 
# a reference-generator. 

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
        
