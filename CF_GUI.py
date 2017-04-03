# -*- coding: utf-8 -*-
"""
Created on Mon Apr  3 11:13:54 2017

@author: Johan
"""

from tkinter import*

root = Tk()
root.geometry("1000x600+0+0")
root.title("CrazyFlie controll system")

Tops = Frame(root, width = 1000,height = 100, bg ="powder blue", relief=SUNKEN)
Tops.pack(side=TOP)
lblName = Label(Tops, font =('arial', 30,'bold'), text = "CrazyFlie controll system", fg = "Steel blue", bd = 10, anchor = 'w')
lblName.grid(row=0,column=0) 

paramFrame = Frame(root, width = 500,height = 250, relief=SUNKEN)
paramFrame.pack(side=LEFT)

plotFrame = Frame(root, width = 500,height = 250, relief=SUNKEN)
plotFrame.pack(side=LEFT)





root.mainloop()