from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import tkinter
import random
import pymysql
import csv
from datetime import datetime
import numpy as np

window = tkinter.Tk()
window.title("Sistema de Gerenciamento de Estoque")
my_tree = ttk.Treeview(window, show='headings', height=20)
window.geometry("720x640")

placeholderArray = ['','','','','']

for i in range(0,5):
    placeholderArray[i]=tkinter.StringVar()
    
frame = tkinter.Frame(window, bg="#02577A")
frame.pack()

btnColor = "#196E78"

manageFrame = tkinter.LabelFrame(frame, text="Gerência", borderwidth=5)
manageFrame.grid(row=0, column=0, sticky="w", padx=[10,200], pady=20, ipadx=[6])

saveBtn = Button(manageFrame, text="SALVAR", width=10, borderwidth=3, bg=btnColor, fg='white')
updateBtn = Button(manageFrame, text="ATUALIZAR", width=10, borderwidth=3, bg=btnColor, fg='white')
deleteBtn = Button(manageFrame, text="DELETAR", width=10, borderwidth=3, bg=btnColor, fg='white')
selectBtn = Button(manageFrame, text="SELECIONAR", width=10, borderwidth=3, bg=btnColor, fg='white')
findBtn = Button(manageFrame, text="ENCONTRAR", width=10, borderwidth=3, bg=btnColor, fg='white')
clearBtn = Button(manageFrame, text="LIMPAR", width=10, borderwidth=3, bg=btnColor, fg='white')
exportBtn = Button(manageFrame, text="EXPORTAR EXCEL", width=10, borderwidth=3, bg=btnColor, fg='white')

saveBtn.grid(row=0,column=0,padx=5,pady=5)
updateBtn.grid(row=0,column=1,padx=5,pady=5)
deleteBtn.grid(row=0,column=2,padx=5,pady=5)
selectBtn.grid(row=0,column=3,padx=5,pady=5)
findBtn.grid(row=0,column=4,padx=5,pady=5)
clearBtn.grid(row=0,column=5,padx=5,pady=5)
exportBtn.grid(row=0,column=6,padx=5,pady=5)

window.resizable(False, False)
window.mainloop()