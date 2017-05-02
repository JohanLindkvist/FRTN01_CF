# -*- coding: utf-8 -*-
"""
Created on Mon Apr  3 11:13:54 2017

@author: Johan
"""

from Tkinter import*
import tkMessageBox
import matplotlib
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
from matplotlib.figure import Figure

from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import numpy as np
import threading
from Regul_CF import Regul_CF
import cflib
from cflib.crazyflie import Crazyflie
from cflib.crazyflie.log import LogConfig
from cflib.crazyflie.syncCrazyflie import SyncCrazyflie
from cflib.crazyflie.syncLogger import SyncLogger
import logging
import cflib.crtp  # noqa
import time

import PD_CF

logging.basicConfig(level=logging.ERROR)
# import cflib
# from cflib.crazyflie import Crazyflie




class GUI():
    
    def __init__(self, root, regul, cf): 
        
        self._cf = cf
        self.regul=regul
        self.root=root
        self.messageBox = tkMessageBox
        
        
        #Size of window
        root.geometry("1000x600+0+0") 
        #Window title
        root.title("CrazyFlie control system")
                
        #Upper left frame for parameters and reference values
        self.paramFrame = Frame(root, width = 530,height = 340, relief=SUNKEN)
        self.paramFrame.place(x = 460, y = 10, width = 530, height = 250)
        
        
        #Lower left frame for x, y and z-plots
        self.XplotFrame = Frame(root, width = 460, height = 200, relief=SUNKEN)
        self.XplotFrame.place(x = 0, y = 0, width = 460, height = 190)
        self.YplotFrame = Frame(root, width = 460, height = 200, relief=SUNKEN)
        self.YplotFrame.place(x = 0, y = 200, width = 460, height = 190)
        self.ZplotFrame = Frame(root, width = 460, height = 200, relief=SUNKEN)
        self.ZplotFrame.place(x = 0, y = 400, width = 460, height = 190)
        self.DplotFrame = Frame(root, width = 530, height = 260, relief=SUNKEN)
        self.DplotFrame.place(x = 470, y = 250, width = 530, height = 350)
        
        #String variables for input
        self.PDx_K = StringVar()
        self.Kx = 1
        self.PDx_K.set(self.Kx)
        
        self.PDx_Td = StringVar()
        self.Tdx = 1
        self.PDx_Td.set(self.Tdx)
        
        self.PDy_K = StringVar()
        self.Ky = 1
        self.PDy_K.set(self.Ky)
        
        self.PDy_Td = StringVar()
        self.Tdy = 1
        self.PDy_Td.set(self.Tdy)
        
        self.PDz_K = StringVar()
        self.Kz = 11000
        self.PDz_K.set(self.Kz)
        
        self.PDz_Td = StringVar()
        self.Tdz = 1
        self.PDz_Td.set(self.Tdz)
        
        self.x_ref = StringVar()
        self.y_ref = StringVar()
        self.z_ref = StringVar()
        self.ref = [1.00, 2.00, 3.14]
        self.x_ref.set(self.ref[0])
        self.y_ref.set(self.ref[1])
        self.z_ref.set(self.ref[2])
        
        #Input fields for pos ref
        self.ref_lbl = Label(self.paramFrame, font=('arial', 10, 'bold'), text = "Reference position", bd = 10, anchor = 'w')
        self.ref_lbl.grid(row = 0, column = 0, columnspan = 4)
        self.ref_x_lbl = Label(self.paramFrame, font=('arial', 10, 'bold'), text = "x", bd = 10, anchor = 'w')
        self.ref_x_lbl.grid(row = 1, column = 0)
        self.ref_x_entry = Entry(self.paramFrame, font=('arial', 10, 'bold'), textvariable = self.x_ref, bd = 10, bg = "powder blue", justify = 'right', width = 5)
        self.ref_x_entry.grid(row = 1, column = 1)
        self.ref_y_lbl = Label(self.paramFrame, font = ('arial', 10, 'bold'), text = "y", bd = 10, anchor = 'w')
        self.ref_y_lbl.grid(row = 2, column = 0)
        self.ref_y_entry = Entry(self.paramFrame, font=('arial', 10, 'bold'), textvariable = self.y_ref, bd = 10, bg = "powder blue", justify = 'right', width = 5)
        self.ref_y_entry.grid(row = 2, column = 1)
        self.ref_z_lbl = Label(self.paramFrame, font = ('arial', 10, 'bold'), text = "z", bd = 10, anchor = 'w')
        self.ref_z_lbl.grid(row = 3, column = 0)
        self.ref_z_entry = Entry(self.paramFrame, font=('arial', 10, 'bold'), textvariable = self.z_ref, bd = 10, bg = "powder blue", justify = 'right', width = 5)
        self.ref_z_entry.grid(row = 3, column = 1)
        
        
        #Input fields for PD parameters
        #X-axis
        self.param_lbl = Label(self.paramFrame, font=('arial', 10, 'bold'), text = "Controll parameters", bd = 10, anchor = 'w')
        self.param_lbl.grid(row = 0, column = 4, columnspan = 5)
        self.x_lbl = Label(self.paramFrame, font=('arial', 10, 'bold'), text = "x-axis:", bd = 10, anchor = 'w')
        self.x_lbl.grid(row = 1, column = 4)
        self.x_k_lbl = Label(self.paramFrame, font=('arial', 10, 'bold'), text = "K", bd = 10, anchor = 'w')
        self.x_k_lbl.grid(row = 1, column = 5)
        self.x_k_entry = Entry(self.paramFrame, font=('arial', 10, 'bold'), textvariable = self.PDx_K, bd = 10, bg = "powder blue", justify = 'right', width = 5)
        self.x_k_entry.grid(row = 1, column = 6)
        self.x_Td_lbl = Label(self.paramFrame, font=('arial', 10, 'bold'), text = "Td", bd = 10, anchor = 'w')
        self.x_Td_lbl.grid(row = 1, column = 7)
        self.x_Td_entry = Entry(self.paramFrame, font=('arial', 10, 'bold'), textvariable = self.PDx_Td, bd = 10, bg = "powder blue", justify = 'right', width = 5)
        self.x_Td_entry.grid(row = 1, column = 8)
        #y-axis
        self.y_lbl = Label(self.paramFrame, font=('arial', 10, 'bold'), text = "y-axis:", bd = 10, anchor = 'w')
        self.y_lbl.grid(row = 2, column = 4)
        self.y_k_lbl = Label(self.paramFrame, font=('arial', 10, 'bold'), text = "K", bd = 10, anchor = 'w')
        self.y_k_lbl.grid(row = 2, column = 5)
        self.y_k_entry = Entry(self.paramFrame, font=('arial', 10, 'bold'), textvariable = self.PDy_K, bd = 10, bg = "powder blue", justify = 'right', width = 5)
        self.y_k_entry.grid(row = 2, column = 6)
        self.y_Td_lbl = Label(self.paramFrame, font=('arial', 10, 'bold'), text = "Td", bd = 10, anchor = 'w')
        self.y_Td_lbl.grid(row = 2, column = 7)
        self.y_Td_entry = Entry(self.paramFrame, font=('arial', 10, 'bold'), textvariable = self.PDx_Td, bd = 10, bg = "powder blue", justify = 'right', width = 5)
        self.y_Td_entry.grid(row = 2, column = 8)
        #z-axis
        self.z_lbl = Label(self.paramFrame, font=('arial', 10, 'bold'), text = "z-axis:", bd = 10, anchor = 'w')
        self.z_lbl.grid(row = 3, column = 4)
        self.z_k_lbl = Label(self.paramFrame, font=('arial', 10, 'bold'), text = "K", bd = 10, anchor = 'w')
        self.z_k_lbl.grid(row = 3, column = 5)
        self.z_k_entry = Entry(self.paramFrame, font=('arial', 10, 'bold'), textvariable = self.PDz_K, bd = 10, bg = "powder blue", justify = 'right', width = 5)
        self.z_k_entry.grid(row = 3, column = 6)
        self.z_Td_lbl = Label(self.paramFrame, font=('arial', 10, 'bold'), text = "Td", bd = 10, anchor = 'w')
        self.z_Td_lbl.grid(row = 3, column = 7)
        self.z_Td_entry = Entry(self.paramFrame, font=('arial', 10, 'bold'), textvariable = self.PDz_Td, bd = 10, bg = "powder blue", justify = 'right', width = 5)
        self.z_Td_entry.grid(row = 3, column = 8)
                
        #Add plot to window for X-axis 
        self.f1 = Figure(figsize=(10,3), dpi=50)
        self.a1 = self.f1.add_subplot(111)
        self.a1.plot([1,2,3,4,5,6,7,8],[5,6,1,3,8,9,3,5])
        self.canvas1 = FigureCanvasTkAgg(self.f1, self.XplotFrame)
        self.canvas1.show()
        self.canvas1.get_tk_widget().pack(side=TOP, expand=True)
        self.toolbar1 = NavigationToolbar2TkAgg(self.canvas1, self.XplotFrame)
        self.toolbar1.update()
        self.canvas1._tkcanvas.pack(side=TOP, expand=True)
        self.f1.subplots_adjust(left=0.05,right=0.95)
        self.a1.set_title('X-values')
       
        #Add plot to window for Y-axis 
        self.f2 = Figure(figsize=(10,3), dpi=50)
        self.a2 = self.f2.add_subplot(111)
        self.a2.plot([1,2,3,4,5,6,7,8],[5,6,1,3,8,9,3,5])
        self.canvas2 = FigureCanvasTkAgg(self.f2, self.YplotFrame)
        self.canvas2.show()
        self.canvas2.get_tk_widget().pack(side=TOP, expand=True)
        self.toolbar2 = NavigationToolbar2TkAgg(self.canvas2, self.YplotFrame)
        self.toolbar2.update()
        self.canvas2._tkcanvas.pack(side=TOP,fill=BOTH, expand=True)
        self.f2.subplots_adjust(left=0.05,right=0.95)
        self.a2.set_title('Y-values')
        
        #Add plot to window for Z-axis 
        self.f3 = Figure(figsize=(10,3), dpi=50)
        self.a3 = self.f3.add_subplot(111)
        self.a3.plot([1,2,3,4,5,6,7,8],[5,6,1,3,8,9,3,5])
        self.canvas3 = FigureCanvasTkAgg(self.f3, self.ZplotFrame)
        self.canvas3.show()
        self.canvas3.get_tk_widget().pack(side=TOP, expand=True)
        self.toolbar3 = NavigationToolbar2TkAgg(self.canvas3, self.ZplotFrame)
        self.toolbar3.update()
        self.canvas3._tkcanvas.pack(side=TOP, expand=True)
        self.f3.subplots_adjust(left=0.05,right=0.95)
        self.a3.set_title('Z-values')
        
        #Add plot to window in 3D
        self.f3D = Figure(figsize=(12,6), dpi=50)
        self.a3D = self.f3D.gca(projection='3d')
        self.f3D.subplots_adjust(left=0, bottom=0, right=1, top=1)

        # Fake data.
        self.X = np.arange(-5, 5, 0.25)
        self.Y = np.arange(-5, 5, 0.25)
        self.X, self.Y = np.meshgrid(self.X, self.Y)
        self.R = np.sqrt(self.X**2 + self.Y**2)
        self.Z = np.sin(self.R)


        self.surf = self.a3D.plot_surface(self.X, self.Y, self.Z, cmap=cm.coolwarm, linewidth=0, antialiased=False)

        # Customize the z axis.
        self.a3D.set_zlim(-1.01, 1.01)
        self.a3D.zaxis.set_major_locator(LinearLocator(10))
        self.a3D.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))

        # Add a color bar which maps values to colors.
        self.f3D.colorbar(self.surf, shrink=0.5, aspect=5)
        
        self.canvas3D = FigureCanvasTkAgg(self.f3D, self.DplotFrame)
        self.canvas3D.show()
        self.canvas3D.get_tk_widget().pack(side=TOP, expand=True)
        self.toolbar3D = NavigationToolbar2TkAgg(self.canvas3D, self.DplotFrame)
        self.toolbar3D.update()
        self.canvas3D._tkcanvas.pack(side=TOP, expand=True)
        self.a3D.set_title('Fight Path in 3D')
        
        
        
        
        
        
        # Buttons
        self.Apply = Button(self.paramFrame, padx=6,pady=6,bd=6,fg="black", font=('arial', 10,'bold'),text = "Apply", bg="powder blue",command =self.btnApply, width = 7).grid(row=4, column = 6)
        self.GO = Button(self.paramFrame, padx=6,pady=6,bd=6,fg="black", font=('arial', 10,'bold'),text = "GO", bg="powder blue",command =self.btnGo, width = 7).grid(row=1, column = 2)
        self.Home = Button(self.paramFrame, padx=6,pady=6,bd=6,fg="black", font=('arial', 10,'bold'),text = "Home", bg="powder blue",command =self.btnHome, width = 7).grid(row=1, column = 3)
        self.Land = Button(self.paramFrame, padx=6,pady=6,bd=6,fg="black", font=('arial', 10,'bold'),text = "Land", bg="powder blue",command =self.btnLand, width = 7).grid(row=2, column = 2)
        self.Stop = Button(self.paramFrame, padx=6,pady=6,bd=6,fg="black", font=('arial', 10,'bold'),text = "Stop", bg="powder blue",command =self.btnStop, width = 7).grid(row=2, column = 3)
        self.Quit = Button(self.paramFrame, padx=6,pady=6,bd=6,fg="black", font=('arial', 10,'bold'),text = "Quit", bg="powder blue",command =self.btnQuit, width = 18).grid(row=3, column = 2, columnspan = 2)
        
        #Drop down menu File and Help    
        self.menu = Menu(root)
        self.root.config(menu=self.menu)
        self.filemenu = Menu(self.menu)
        self.menu.add_cascade(label="File", menu=self.filemenu)
        self.filemenu.add_command(label="Connect", command=self.connectCF)
        self.filemenu.add_command(label="Disconnect", command=self.Disconnect)
        self.filemenu.add_separator()
        self.filemenu.add_command(label="Exit", command=root.destroy)

        self.helpmenu = Menu(self.menu)
        self.menu.add_cascade(label="Help", menu=self.helpmenu)
        self.helpmenu.add_command(label="About...", command=self.About)
        

     #Define method for apply button (Not real method)
    def btnApply(self):
        self.Kx = float(self.PDx_K.get())
        self.Tdx = float(self.PDx_Td.get())
        self.Ky = float(self.PDy_K.get())
        self.Tdy = float(self.PDy_Td.get())
        self.Kz = float(self.PDz_K.get())
        self.Tdz = float(self.PDz_Td.get())
        PD_CF.params=[self.Kx,self.Tdx,self.Ky,self.Tdy, self.Kz, self.Tdz]
                
    #Define method for GO! button
    def btnGo(self):
        self.regul.Go()
        #print ("GO")
        self.ref[0] = float(self.x_ref.get())
        self.ref[1] = float(self.y_ref.get())
        self.ref[2] = float(self.z_ref.get()) 
        self.regul.setReference(self.ref)
    
    #Defines method for Home button
    def btnHome(self):
        #print ("Home")
        self.ref[0] = 0
        self.ref[1] = 0
        self.ref[2] = 0
        self.x_ref.set(self.ref[0])
        self.y_ref.set(self.ref[1])
        self.z_ref.set(self.ref[2])
        self.regul.setReference(self.ref)
    
    #Defines method for Land button
    def btnLand(self):
        #TODO implement method
        print ("Land")
    
    #Defines method for Stop button
    def btnStop(self):
        self.regul.stop()
        print ("Stopped")

    def btnQuit(self):
        self.regul.destroy()
        self.root.destroy()
    #Drop down menu
    
        
    def Disconnect(self):
        #LowPrio ToDo
        print ("Disconnect")
        
    def About(self):
        self.messageBox.showinfo("About", "CrazyFlie dude!")
    
    
    

    def _connection_failed(self,link_uri, msg):
        """Callback when connection initial connection fails (i.e no Crazyflie
        at the specified address)"""
        print('Connection to %s failed: %s' % (link_uri, msg))

    def _connection_lost(self,link_uri, msg):
        """Callback when disconnected after a connection has been made (i.e
        Crazyflie moves out of range)"""
        print('Connection to %s lost: %s' % (link_uri, msg))

    def _disconnected(self,link_uri):
        """Callback when the Crazyflie is disconnected (called in all cases)"""
        print('Disconnected from %s' % link_uri)
    
    def _connected(self, link_uri):
        """ This callback is called form the Crazyflie API when a Crazyflie
        has been connected and the TOCs have been downloaded."""

        # Start a separate thread to do the motor test.
        # Do not hijack the calling thread!
        #Thread(target=_ramp_motors).start()
    
    def connectCF(self):
        cflib.crtp.init_drivers(enable_debug_driver=False)
        
        self._lg_stab = LogConfig(name='Position', period_in_ms=100)
        self._lg_stab.add_variable('kalman.stateX', 'float')
        self._lg_stab.add_variable('kalman.stateY', 'float')
        self._lg_stab.add_variable('kalman.stateZ', 'float')
        
        #Scan for Crazyflies and use the first one found
        print('Looking for Crazyflie')
        self.available = cflib.crtp.scan_interfaces()
        print('Crazyflies found:')
        for i in self.available:
            print(i[0])
		    
        if len(self.available) > 0:    
            self.link_uri=self.available[0][0]
            self._cf.connected.add_callback(self._connected)
            self._cf.disconnected.add_callback(self._disconnected)
            self._cf.connection_failed.add_callback(self._connection_failed)
            self._cf.connection_lost.add_callback(self._connection_lost)
            self._cf.open_link(self.link_uri)	
            print('Connecting to %s' % self.link_uri) 
   
    def _connected(self, link_uri):
        print ('connected to crazyflie')
        try:
            self._cf.log.add_config(self._lg_stab)
            # This callback will receive the data
            self._lg_stab.data_received_cb.add_callback(self._stab_log_data)
            # This callback will be called on errors
            self._lg_stab.error_cb.add_callback(self._stab_log_error)
            # Start the logging
            self._lg_stab.start()
        except KeyError as e:
            print('Could not start log configuration,'
                  '{} not found in TOC'.format(str(e)))
        except AttributeError:
            print('Could not add Stabilizer log config, bad configuration.')

    def _stab_log_error(self, logconf, msg):
        """Callback from the log API when an error occurs"""
        print('Error when logging %s: %s' % (logconf.name, msg))

    def _stab_log_data(self, timestamp, data, logconf):
        """Callback froma the log API when data arrives"""
       
        self.regul.updatePos([data['kalman.stateX'], data['kalman.stateY'], data['kalman.stateZ']])
      

class GUI_Thread(threading.Thread):
    
    def __init__(self, threadID, name, regul,_cf):
        #Init GUI Thread   
        self.root = Tk()
        GUI(self.root, regul,_cf)
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.root.mainloop()
        
    def run(self): 
        print("Closed GUI")

