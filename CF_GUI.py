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

#String variables for input
PDx_K = StringVar()
PDx_Td = StringVar()
PDy_K = StringVar()
PDy_Td = StringVar()
PDz_K = StringVar()
PDz_Td = StringVar()
pos_ref = StringVar()

# Input for K parameter for PD controller of x coordinate 
param_PDx_K_Lbl = Label(paramFrame, font=('arial', 10,'bold'), text = "PDx K", bd = 10,anchor = 'w')
param_PDx_K_Lbl.grid(row=1,column=0)
PDx_K_Entry = Entry(paramFrame, font=('arial', 10,'bold'), textvariable = PDx_K, bd=10,insertwidth=2, bg="powder blue", justify = 'right')
PDx_K_Entry.grid(row=1,column=1)

# Input for Td parameter for PD controller of x coordinate 
param_PDx_Td_Lbl = Label(paramFrame, font=('arial', 10,'bold'), text = "PDx Td", bd = 10,anchor = 'w')
param_PDx_Td_Lbl.grid(row=2,column=0)
PDx_Td_Entry = Entry(paramFrame, font=('arial', 10,'bold'), textvariable = PDx_Td, bd=10,insertwidth=2, bg="powder blue", justify = 'right')
PDx_Td_Entry.grid(row=2,column=1)

# Input for K parameter for PD controller of y coordinate 
param_PDy_K_Lbl = Label(paramFrame, font=('arial', 10,'bold'), text = "PDy K", bd = 10,anchor = 'w')
param_PDy_K_Lbl.grid(row=3,column=0)
PDy_K_Entry = Entry(paramFrame, font=('arial', 10,'bold'), textvariable = PDy_K, bd=10,insertwidth=2, bg="powder blue", justify = 'right')
PDy_K_Entry.grid(row=3,column=1)

# Input for Td parameter for PD controller of y coordinate 
param_PDy_Td_Lbl = Label(paramFrame, font=('arial', 10,'bold'), text = "PDy Td", bd = 10,anchor = 'w')
param_PDy_Td_Lbl.grid(row=4,column=0)
PDy_Td_Entry = Entry(paramFrame, font=('arial', 10,'bold'), textvariable = PDy_Td, bd=10,insertwidth=2, bg="powder blue", justify = 'right')
PDy_Td_Entry.grid(row=4,column=1)

# Input for K parameter for PD controller of z coordinate 
param_PDz_K_Lbl = Label(paramFrame, font=('arial', 10,'bold'), text = "PDz K", bd = 10,anchor = 'w')
param_PDz_K_Lbl.grid(row=5,column=0)
PDz_K_Entry = Entry(paramFrame, font=('arial', 10,'bold'), textvariable = PDz_K, bd=10,insertwidth=2, bg="powder blue", justify = 'right')
PDz_K_Entry.grid(row=5,column=1)

# Input for Td parameter for PD controller of z coordinate 
param_PDz_Td_Lbl = Label(paramFrame, font=('arial', 10,'bold'), text = "PDz Td", bd = 10,anchor = 'w')
param_PDz_Td_Lbl.grid(row=6,column=0)
PDz_Td_Entry = Entry(paramFrame, font=('arial', 10,'bold'), textvariable = PDz_Td, bd=10,insertwidth=2, bg="powder blue", justify = 'right')
PDz_Td_Entry.grid(row=6,column=1)

# Input for reference position
pos_ref_Lbl = Label(paramFrame, font=('arial', 10,'bold'), text = "Pos Ref", bd = 10,anchor = 'w')
pos_ref_Lbl.grid(row=0,column=0)
pos_ref_Entry = Entry(paramFrame, font=('arial', 10,'bold'), textvariable = pos_ref, bd=10,insertwidth=2, bg="powder blue", justify = 'right')
pos_ref_Entry.grid(row=0,column=1)

#Define method for apply button (Not real method)
def btnApply():
    global test
    test = PDx_K.get()
    pos_ref.set(test)
# Apply changes from input above
Apply = Button(paramFrame, padx=8,pady=8,bd=6,fg="black", font=('arial', 10,'bold'),text = "Apply", bg="powder blue",command =btnApply).grid(row=7, column = 1)



 
root.mainloop()