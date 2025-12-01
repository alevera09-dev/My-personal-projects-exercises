# -*- coding: utf-8 -*-
"""
Created on Sun Oct  5 16:12:07 2025

@author: alesa
"""

"""
Calculadora con GUI de Tkinter
"""

import tkinter
from tkinter import ttk
root = tkinter.Tk()
frm = ttk.Frame(root, padding=10)
frm.grid()
ttk.Label(frm, text="Hello World!").grid(column=0, row=0)
ttk.Button(frm, text="Quit", command=root.destroy).grid(column=1, row=0)
root.mainloop()