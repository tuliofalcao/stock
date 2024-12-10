from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import tkinter
import random
import pymysql # type: ignore
import csv
from datetime import datetime
import numpy as np # type: ignore

window = tkinter.Tk()
window.title("Sistema de Gerenciamento de Estoque")
window.geometry("720x640")
my_tree = ttk.Treeview(window, show='headings', height=20)
style=ttk.Style()

placeholderArray = ['','','','','']

def connection():
    conn=pymysql.connect(
        host='localhost',
        user='root',
        password='',
        db='stock'
    )
    return conn

conn=connection()
cursor=conn.cursor()

for i in range(0,5):
    placeholderArray[i]=tkinter.StringVar()
    
dummydata = [
    ['123123','123sd','123sd','123sd','123sd','123sd'],
    ['123133','123sd','123sd','123sd','123sd','123sd'],
    ['1231253','123sd','123sd','123sd','123sd','123sd'],
    ['1231273','123sd','123sd','123sd','123sd','123sd'],
    ['12315623','123sd','123sd','123sd','123sd','123sd'],
    ['12312753','123sd','123sd','123sd','123sd','123sd'],
]

def refreshTable():
    for data in my_tree.get_children():
        my_tree.delete(data)
    for array in dummydata:
        my_tree.insert(parent='', index='end', iid=array, text="", values=(array), tag="orow")
    my_tree.tag_configure('orow', background="#EEEEEE")
    my_tree.pack()
    
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
exportBtn = Button(manageFrame, text="EXPORTAR EXCEL", width=13, borderwidth=3, bg=btnColor, fg='white')

saveBtn.grid(row=0,column=0,padx=5,pady=5)
updateBtn.grid(row=0,column=1,padx=5,pady=5)
deleteBtn.grid(row=0,column=2,padx=5,pady=5)
selectBtn.grid(row=0,column=3,padx=5,pady=5)
findBtn.grid(row=0,column=4,padx=5,pady=5)
clearBtn.grid(row=0,column=5,padx=5,pady=5)
exportBtn.grid(row=0,column=6,padx=5,pady=5)

entriesFrame = tkinter.LabelFrame(frame,text="Form",borderwidth=5)
entriesFrame.grid(row=1,column=0,sticky="w",padx=[10,200],pady=[0,20],ipadx=[6])

itemIdLabel = Label(entriesFrame, text="ID ITEM", anchor="e", width=10)
nameLabel = Label(entriesFrame, text="NOME", anchor="e", width=10)
priceLabel = Label(entriesFrame, text="PREÇO", anchor="e", width=10)
qntLabel = Label(entriesFrame, text="QUANTIDADE", anchor="e", width=10)
categoryLabel = Label(entriesFrame, text="CATEGORIA", anchor="e", width=10)

itemIdLabel.grid(row=0,column=0,padx=10)
nameLabel.grid(row=1,column=0,padx=10)
priceLabel.grid(row=2,column=0,padx=10)
qntLabel.grid(row=3,column=0,padx=10)
categoryLabel.grid(row=4,column=0,padx=10)

categoryArray = ['Ferramentas de Rede', 'Peças de Computador', 'Ferramentas de Reparo', 'Gadgets']

itemIdEntry = Entry(entriesFrame,width=50, textvariable=placeholderArray[0])
nameEntry = Entry(entriesFrame,width=50, textvariable=placeholderArray[1])
priceEntry = Entry(entriesFrame,width=50, textvariable=placeholderArray[2])
qntEntry = Entry(entriesFrame,width=50, textvariable=placeholderArray[3])
categoryCombo = ttk.Combobox(entriesFrame,width=50, textvariable=placeholderArray[4],values=categoryArray)

itemIdEntry.grid(row=0,column=2,padx=5,pady=5)
nameEntry.grid(row=1,column=2,padx=5,pady=5)
priceEntry.grid(row=2,column=2,padx=5,pady=5)
qntEntry.grid(row=3,column=2,padx=5,pady=5)
categoryCombo.grid(row=4,column=2,padx=5,pady=5)

generateIdBtn = Button(entriesFrame, text="GERA ID", borderwidth=3, bg=btnColor, fg='white')
generateIdBtn.grid(row=0,column=3,padx=5,pady=5)

style.configure(window)

my_tree['columns']=("ID Item", "Nome", "Preço", "Quantidade", "Categoria", "Data")

my_tree.column("#0", width=0, stretch=NO)
my_tree.column("ID Item", anchor=W, width=70)
my_tree.column("Nome", anchor=W, width=125)
my_tree.column("Preço", anchor=W, width=125)
my_tree.column("Quantidade", anchor=W, width=100)
my_tree.column("Categoria", anchor=W, width=150)
my_tree.column("Data", anchor=W, width=150)

my_tree.heading("ID Item", text="ID Item", anchor=W)
my_tree.heading("Nome", text="Nome", anchor=W)
my_tree.heading("Preço", text="Preço", anchor=W)
my_tree.heading("Quantidade", text="Quantidade", anchor=W)
my_tree.heading("Categoria", text="Categoria", anchor=W)
my_tree.heading("Data", text="Data", anchor=W)

my_tree.tag_configure('orow',background='#EEEEEE')
my_tree.pack()

refreshTable()


window.resizable(False, False)
window.mainloop()