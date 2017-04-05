# -*- coding: utf-8 -*-
"""
Created on Mon Apr  3 11:13:54 2017

@author: Johan
"""

<<<<<<< HEAD
from tkinter import*
import tkinter.messagebox
=======
from tkinter import *
>>>>>>> origin/master

root = Tk()
#Size of window
root.geometry("1000x600+0+0")
#Window title
root.title("CrazyFlie control system")

#Top frame
Tops = Frame(root, width = 1000,height = 40, bg ="powder blue", relief=SUNKEN)
Tops.pack(side=TOP)

#Label in top frame
lblName = Label(Tops, font =('arial', 30,'bold'), text = "CrazyFlie control system", fg = "Steel blue", bd = 10, anchor = 'w')
lblName.grid(row=0,column=0) 

#Upper left frame for parameters and reference values
paramFrame = Frame(root, width = 500,height = 360, relief=SUNKEN)
paramFrame.pack(side=LEFT)

#Lower left frame for x, y and z-plots
plotFrame = Frame(root, width = 1000,height = 200, relief=SUNKEN)
plotFrame.pack(side=BOTTOM)

#String variables for input
PDx_K = StringVar()
Kx = 1
PDx_K.set(Kx)

PDx_Td = StringVar()
Tdx = 1
PDx_Td.set(Tdx)

PDy_K = StringVar()
Ky = 1
PDy_K.set(Ky)

PDy_Td = StringVar()
Tdy = 1
PDy_Td.set(Tdy)

PDz_K = StringVar()
Kz = 1
PDz_K.set(Kz)

PDz_Td = StringVar()
Tdz = 1
PDz_Td.set(Tdz)

pos_ref = StringVar()
ref = [1.00, 2.00, 3.14]
pos_ref.set(ref)

# Input for K parameter for PD controller of x coordinate 
param_PDx_K_Lbl = Label(paramFrame, font=('arial', 10,'bold'), text = "PDx K", bd = 10,anchor = 'w')
param_PDx_K_Lbl.grid(row=2,column=0,columnspan=2)
PDx_K_Entry = Entry(paramFrame, font=('arial', 10,'bold'), textvariable = PDx_K, bd=10,insertwidth=2, bg="powder blue", justify = 'right')
PDx_K_Entry.grid(row=2,column=2,columnspan=3)

# Input for Td parameter for PD controller of x coordinate 
param_PDx_Td_Lbl = Label(paramFrame, font=('arial', 10,'bold'), text = "PDx Td", bd = 10,anchor = 'w')
param_PDx_Td_Lbl.grid(row=3,column=0,columnspan=2)
PDx_Td_Entry = Entry(paramFrame, font=('arial', 10,'bold'), textvariable = PDx_Td, bd=10,insertwidth=2, bg="powder blue", justify = 'right')
PDx_Td_Entry.grid(row=3,column=2,columnspan=3)

# Input for K parameter for PD controller of y coordinate 
param_PDy_K_Lbl = Label(paramFrame, font=('arial', 10,'bold'), text = "PDy K", bd = 10,anchor = 'w')
param_PDy_K_Lbl.grid(row=4,column=0,columnspan=2)
PDy_K_Entry = Entry(paramFrame, font=('arial', 10,'bold'), textvariable = PDy_K, bd=10,insertwidth=2, bg="powder blue", justify = 'right')
PDy_K_Entry.grid(row=4,column=2,columnspan=3)

# Input for Td parameter for PD controller of y coordinate 
param_PDy_Td_Lbl = Label(paramFrame, font=('arial', 10,'bold'), text = "PDy Td", bd = 10,anchor = 'w')
param_PDy_Td_Lbl.grid(row=5,column=0,columnspan=2)
PDy_Td_Entry = Entry(paramFrame, font=('arial', 10,'bold'), textvariable = PDy_Td, bd=10,insertwidth=2, bg="powder blue", justify = 'right')
PDy_Td_Entry.grid(row=5,column=2,columnspan=3)

# Input for K parameter for PD controller of z coordinate 
param_PDz_K_Lbl = Label(paramFrame, font=('arial', 10,'bold'), text = "PDz K", bd = 10,anchor = 'w')
param_PDz_K_Lbl.grid(row=6,column=0,columnspan=2)
PDz_K_Entry = Entry(paramFrame, font=('arial', 10,'bold'), textvariable = PDz_K, bd=10,insertwidth=2, bg="powder blue", justify = 'right')
PDz_K_Entry.grid(row=6,column=2,columnspan=3)

# Input for Td parameter for PD controller of z coordinate 
param_PDz_Td_Lbl = Label(paramFrame, font=('arial', 10,'bold'), text = "PDz Td", bd = 10,anchor = 'w')
param_PDz_Td_Lbl.grid(row=7,column=0,columnspan=2)
PDz_Td_Entry = Entry(paramFrame, font=('arial', 10,'bold'), textvariable = PDz_Td, bd=10,insertwidth=2, bg="powder blue", justify = 'right')
PDz_Td_Entry.grid(row=7,column=2,columnspan=3)

# Input for reference position
pos_ref_Lbl = Label(paramFrame, font=('arial', 10,'bold'), text = "Pos Ref", bd = 10,anchor = 'w')
pos_ref_Lbl.grid(row=1,column=0,columnspan=2)
pos_ref_Entry = Entry(paramFrame, font=('arial', 10,'bold'), textvariable = pos_ref, bd=10,insertwidth=2, bg="powder blue", justify = 'right')
pos_ref_Entry.grid(row=1,column=2,columnspan=3)

#Define method for apply button (Not real method)
def btnApply():
    Kx = PDx_K.get()
    PDx_K.set(Kx)
    print ("PDx K = ", Kx)
    Tdx = PDx_Td.get()
    PDx_Td.set(Tdx)
    print ("PDx Td = ", Tdx)
    Ky = PDy_K.get()
    PDy_K.set(Ky)
    print ("PDy K = ", Ky)
    Tdy = PDy_Td.get()
    PDy_Td.set(Tdy)
    print ("PDy Td = ", Tdy)
    Kz = PDz_K.get()
    PDz_K.set(Kz)
    print ("PDz K = ", Kz)
    Tdz = PDz_Td.get()
    PDz_Td.set(Tdz) 
    print ("PDz Td = ", Tdz)     
    ref = pos_ref.get()
    print ("Position reference is set to ", ref,)
    pos_ref.set(ref)

# Apply changes from input above
Apply = Button(paramFrame, padx=6,pady=6,bd=6,fg="black", font=('arial', 10,'bold'),text = "Apply", bg="powder blue",command =btnApply).grid(row=0, column = 4)

#Define method for GO! button
def btnGo():
    # TODO implement method
    print ("GO")
#GO! button
GO = Button(paramFrame, padx=6,pady=6,bd=6,fg="black", font=('arial', 10,'bold'),text = "GO", bg="powder blue",command =btnGo).grid(row=0, column = 0)


#Defines method for Home button
def btnHome():
    #TODO implement method
    print ("Home")
#Home button
Home = Button(paramFrame, padx=6,pady=6,bd=6,fg="black", font=('arial', 10,'bold'),text = "Home", bg="powder blue",command =btnHome).grid(row=0, column = 1)

#Defines method for Land button
def btnLand():
    #TODO implement method
    print ("Land")
#Land Button
Land = Button(paramFrame, padx=6,pady=6,bd=6,fg="black", font=('arial', 10,'bold'),text = "Land", bg="powder blue",command =btnLand).grid(row=0, column = 2)

#Defines method for Stop button
def btnStop():
    #TODO implement method
    print ("Stop")
#Stop button
Stop = Button(paramFrame, padx=6,pady=6,bd=6,fg="black", font=('arial', 10,'bold'),text = "Stop", bg="powder blue",command =btnStop).grid(row=0, column = 3)

#Drop down menu
def Connect():
    print ("Connect")
    
def Disconnect():
    print ("Disconnect")
    
def About():
    tkinter.messagebox.showinfo("About", "CrazyFlie dude!")

#Drop down menu File and Help    
menu = Menu(root)
root.config(menu=menu)
filemenu = Menu(menu)
menu.add_cascade(label="File", menu=filemenu)
filemenu.add_command(label="Connect", command=Connect)
filemenu.add_command(label="Disconnect", command=Disconnect)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=root.destroy)

helpmenu = Menu(menu)
menu.add_cascade(label="Help", menu=helpmenu)
helpmenu.add_command(label="About...", command=About)

root.mainloop()