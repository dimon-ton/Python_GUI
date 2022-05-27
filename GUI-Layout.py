from tkinter import *
from tkinter import ttk

GUI = Tk()
GUI.geometry('500x300')
GUI.title('โปรแกรมจัดการเลย์เอาท์')

# Label(GUI,text='hello').pack()
#--------------------------------------Pack--------------------------------------
L1 = Label(GUI,text='hello - pack')
L1.pack() # คือเรียงจากบนลงล่าง
#--------------------------------------Place--------------------------------------
L2 = Label(GUI,text='hello2 - place')
L2.place(x=50,y=200)
#--------------------------------------GRID--------------------------------------

F1 = Frame(GUI)
F1.pack()

L3 = Label(F1,text='hello - GRID',bg='red')
L3.grid(row=0,column=0)

L4 = Label(F1,text='hello - GRID',bg='green')
L4.grid(row=0,column=1)

L5 = Label(F1,text='hello - GRID',bg='orange')
L5.grid(row=0,column=2)

L6 = Label(F1,text='hello - GRID',bg='blue',fg='white')
L6.grid(row=2,column=2)

GUI.mainloop()
