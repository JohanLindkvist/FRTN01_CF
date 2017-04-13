# -*- coding: utf-8 -*-
"""
Created on Mon Apr  3 11:13:54 2017

@author: Johan
"""

from tkinter import*
import tkinter.messagebox
import matplotlib
from matplotlib import style 
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
from matplotlib.figure import Figure

import PD_CF


class GUI:

    def __init__(self,root):    
        self.root=root
        #Size of window
        root.geometry("1000x600+0+0")
        #Window title
        root.title("CrazyFlie control system")
        
        #Top frame
        self.Tops = Frame(root, width = 1000,height = 40, bg ="powder blue", relief=SUNKEN)
        self.Tops.pack(side=TOP)
        
        #Label in top frame
        self.lblName = Label(self.Tops, font =('arial', 30,'bold'), text = "CrazyFlie control system", fg = "Steel blue", bd = 10, anchor = 'w')
        self.lblName.grid(row=0,column=0) 
        
        #Upper left frame for parameters and reference values
        self.paramFrame = Frame(root, width = 500,height = 360, relief=SUNKEN)
        self.paramFrame.pack(side=LEFT)
        
        #Lower left frame for x, y and z-plots
        self.plotFrame = Frame(root, width = 1000,height = 200, relief=SUNKEN)
        self.plotFrame.pack(side=BOTTOM)
        
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
        self.Kz = 1
        self.PDz_K.set(self.Kz)
        
        self.PDz_Td = StringVar()
        self.Tdz = 1
        self.PDz_Td.set(self.Tdz)
        
        self.pos_ref = StringVar()
        self.ref = [1.00, 2.00, 3.14]
        self.pos_ref.set(self.ref)
        
        # Input for K parameter for PD controller of x coordinate 
        self.param_PDx_K_Lbl = Label(self.paramFrame, font=('arial', 10,'bold'), text = "PDx K", bd = 10,anchor = 'w')
        self.param_PDx_K_Lbl.grid(row=2,column=0,columnspan=2)
        self.PDx_K_Entry = Entry(self.paramFrame, font=('arial', 10,'bold'), textvariable = self.PDx_K, bd=10,insertwidth=2, bg="powder blue", justify = 'right')
        self.PDx_K_Entry.grid(row=2,column=2,columnspan=3)
        
        # Input for Td parameter for PD controller of x coordinate 
        self.param_PDx_Td_Lbl = Label(self.paramFrame, font=('arial', 10,'bold'), text = "PDx Td", bd = 10,anchor = 'w')
        self.param_PDx_Td_Lbl.grid(row=3,column=0,columnspan=2)
        self.PDx_Td_Entry = Entry(self.paramFrame, font=('arial', 10,'bold'), textvariable = self.PDx_Td, bd=10,insertwidth=2, bg="powder blue", justify = 'right')
        self.PDx_Td_Entry.grid(row=3,column=2,columnspan=3)
        
        # Input for K parameter for PD controller of y coordinate 
        self.param_PDy_K_Lbl = Label(self.paramFrame, font=('arial', 10,'bold'), text = "PDy K", bd = 10,anchor = 'w')
        self.param_PDy_K_Lbl.grid(row=4,column=0,columnspan=2)
        self.PDy_K_Entry = Entry(self.paramFrame, font=('arial', 10,'bold'), textvariable = self.PDy_K, bd=10,insertwidth=2, bg="powder blue", justify = 'right')
        self.PDy_K_Entry.grid(row=4,column=2,columnspan=3)
        
        # Input for Td parameter for PD controller of y coordinate 
        self.param_PDy_Td_Lbl = Label(self.paramFrame, font=('arial', 10,'bold'), text = "PDy Td", bd = 10,anchor = 'w')
        self.param_PDy_Td_Lbl.grid(row=5,column=0,columnspan=2)
        self.PDy_Td_Entry = Entry(self.paramFrame, font=('arial', 10,'bold'), textvariable = self.PDy_Td, bd=10,insertwidth=2, bg="powder blue", justify = 'right')
        self.PDy_Td_Entry.grid(row=5,column=2,columnspan=3)
        
        # Input for K parameter for PD controller of z coordinate 
        self.param_PDz_K_Lbl = Label(self.paramFrame, font=('arial', 10,'bold'), text = "PDz K", bd = 10,anchor = 'w')
        self.param_PDz_K_Lbl.grid(row=6,column=0,columnspan=2)
        self.PDz_K_Entry = Entry(self.paramFrame, font=('arial', 10,'bold'), textvariable = self.PDz_K, bd=10,insertwidth=2, bg="powder blue", justify = 'right')
        self.PDz_K_Entry.grid(row=6,column=2,columnspan=3)
        
        # Input for Td parameter for PD controller of z coordinate 
        self.param_PDz_Td_Lbl = Label(self.paramFrame, font=('arial', 10,'bold'), text = "PDz Td", bd = 10,anchor = 'w')
        self.param_PDz_Td_Lbl.grid(row=7,column=0,columnspan=2)
        self.PDz_Td_Entry = Entry(self.paramFrame, font=('arial', 10,'bold'), textvariable = self.PDz_Td, bd=10,insertwidth=2, bg="powder blue", justify = 'right')
        self.PDz_Td_Entry.grid(row=7,column=2,columnspan=3)
        
        # Input for reference position
        self.pos_ref_Lbl = Label(self.paramFrame, font=('arial', 10,'bold'), text = "Pos Ref", bd = 10,anchor = 'w')
        self.pos_ref_Lbl.grid(row=1,column=0,columnspan=2)
        self.pos_ref_Entry = Entry(self.paramFrame, font=('arial', 10,'bold'), textvariable = self.pos_ref, bd=10,insertwidth=2, bg="powder blue", justify = 'right',  width=20)
        self.pos_ref_Entry.grid(row=1,column=2,columnspan=3)
        
       
        
        # Add plot to window 
        self.f1 = Figure(figsize=(6,2), dpi=100)
        self.a1 = self.f1.add_subplot(111)
        self.a1.plot([1,2,3,4,5,6,7,8],[5,6,1,3,8,9,3,5])
        self.canvas1 = FigureCanvasTkAgg(self.f1, self.plotFrame)
        self.canvas1.show()
        self.canvas1.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=True)
        self.toolbar1 = NavigationToolbar2TkAgg(self.canvas1, self.plotFrame)
        self.toolbar1.update()
        self.canvas1._tkcanvas.pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=True)
        
        self.Apply = Button(self.paramFrame, padx=6,pady=6,bd=6,fg="black", font=('arial', 10,'bold'),text = "Apply", bg="powder blue",command =self.btnApply).grid(row=0, column = 4)
        self.GO = Button(self.paramFrame, padx=6,pady=6,bd=6,fg="black", font=('arial', 10,'bold'),text = "GO", bg="powder blue",command =self.btnGo).grid(row=0, column = 0)
        self.Home = Button(self.paramFrame, padx=6,pady=6,bd=6,fg="black", font=('arial', 10,'bold'),text = "Home", bg="powder blue",command =self.btnHome).grid(row=0, column = 1)
        self.Land = Button(self.paramFrame, padx=6,pady=6,bd=6,fg="black", font=('arial', 10,'bold'),text = "Land", bg="powder blue",command =self.btnLand).grid(row=0, column = 2)
        self.Stop = Button(self.paramFrame, padx=6,pady=6,bd=6,fg="black", font=('arial', 10,'bold'),text = "Stop", bg="powder blue",command =self.btnStop).grid(row=0, column = 3)
        
        #Drop down menu File and Help    
        self.menu = Menu(root)
        self.root.config(menu=self.menu)
        self.filemenu = Menu(self.menu)
        self.menu.add_cascade(label="File", menu=self.filemenu)
        self.filemenu.add_command(label="Connect", command=self.Connect)
        self.filemenu.add_command(label="Disconnect", command=self.Disconnect)
        self.filemenu.add_separator()
        self.filemenu.add_command(label="Exit", command=root.destroy)

        self.helpmenu = Menu(self.menu)
        self.menu.add_cascade(label="Help", menu=self.helpmenu)
        self.helpmenu.add_command(label="About...", command=self.About)
#    
    
     #Define method for apply button (Not real method)
    def btnApply(self):
        self.Kx = PDx_K.get()
        self.PDx_K.set(Kx)
        self.print ("PDx K = ", Kx)
        self.Tdx = PDx_Td.get()
        self.PDx_Td.set(Tdx)
        print ("PDx Td = ", Tdx)
        self.Ky = PDy_K.get()
        self.PDy_K.set(Ky)
        print ("PDy K = ", Ky)
        self.Tdy = PDy_Td.get()
        self.PDy_Td.set(Tdy)
        print ("PDy Td = ", Tdy)
        self.Kz = PDz_K.get()
        self.PDz_K.set(Kz)
        print ("PDz K = ", Kz)
        self.Tdz = PDz_Td.get()
        self.PDz_Td.set(Tdz) 
        print ("PDz Td = ", Tdz)     
        self.ref = pos_ref.get()
        print ("Position reference is set to ", ref,)
        self.pos_ref.set(ref)
    
    
    # Apply changes from input above
        
    #Define method for GO! button
    def btnGo(self):
        # TODO implement method
        print ("GO")
    #GO! button
    
    
    #Defines method for Home button
    def btnHome(self):
        #TODO implement method
        print ("Home")
    #Home button
    
    #Defines method for Land button
    def btnLand(self):
        #TODO implement method
        print ("Land")
    #Land Button
    
    #Defines method for Stop button
    def btnStop(self):
        #TODO implement method
        print ("Stop")
    #Stop button
    
    #Drop down menu
    def Connect(self):
        print ("Connect")
        
    def Disconnect(self):
        print ("Disconnect")
        
    def About(self):
        self.tkinter.messagebox.showinfo("About", "CrazyFlie dude!")
    
   


root = Tk()
my_gui=GUI(root)
root.mainloop()