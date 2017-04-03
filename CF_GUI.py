# -*- coding: utf-8 -*-
"""
Created on Mon Apr  3 11:13:54 2017

@author: Johan
"""

from tkinter import*

root = Tk()
#Size of window
root.geometry("1000x600+0+0")
#Window title
root.title("CrazyFlie controll system")

#Top frame
Tops = Frame(root, width = 1000,height = 100, bg ="powder blue", relief=SUNKEN)
Tops.pack(side=TOP)

#Label in top frame
lblName = Label(Tops, font =('arial', 30,'bold'), text = "CrazyFlie controll system", fg = "Steel blue", bd = 10, anchor = 'w')
lblName.grid(row=0,column=0) 

#Upper left frame for parameters and reference values
paramFrame = Frame(root, width = 500,height = 250, relief=SUNKEN)
paramFrame.pack(side=LEFT)

#Lower left frame for x, y and z-plots
plotFrame = Frame(root, width = 1000,height = 250, relief=SUNKEN)
plotFrame.pack(side=BOTTOM)

PDx_K = StringVar()
PDx_Td = StringVar()
# Input for K parameter for PD controller of x coordinate 
param_PDx_K_Lbl = Label(paramFrame, font=('arial', 10,'bold'), text = "PDx K", bd = 16,anchor = 'w')
param_PDx_K_Lbl.grid(row=1,column=0)
txtTest = Entry(paramFrame, font=('arial', 10,'bold'), textvariable = PDx_K, bd=10,insertwidth=2, bg="powder blue", justify = 'right')
txtTest.grid(row=1,column=1)

# Input for Td parameter for PD controller of x coordinate 
param_PDx_Td_Lbl = Label(paramFrame, font=('arial', 10,'bold'), text = "PDx Td", bd = 16,anchor = 'w')
param_PDx_Td_Lbl.grid(row=2,column=0)
txtTest = Entry(paramFrame, font=('arial', 10,'bold'), textvariable = PDx_Td, bd=10,insertwidth=2, bg="powder blue", justify = 'right')
txtTest.grid(row=2,column=1)




root.mainloop()