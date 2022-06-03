from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import math

GUI = Tk()
GUI.title('โปรแกรมคำนวณความยาวด้านตรงข้ามมุมฉาก')
GUI.geometry('500x300')

FONT = ('Angsana New',25)

L1 = ttk.Label(GUI,text='กรอกด้านประกอบมุมฉาก A',justify='left',font=FONT)
L1.pack()

v_A = StringVar()
E1 = ttk.Entry(GUI ,textvariable=v_A, width=10,font=FONT,justify='right')
E1.pack()

L2 = ttk.Label(GUI,text='กรอกด้านประกอบมุมฉาก B',justify='left',font=FONT)
L2.pack()

v_B = StringVar()
E2 = ttk.Entry(GUI ,textvariable=v_B, width=10,font=FONT,justify='right')
E2.pack()

def Calc(event=None):
    print('Calculating...')
    A = float(v_A.get())
    B = float(v_B.get())
    calc_result = math.sqrt(A*A + B*B)
    print(calc_result)
    messagebox.showinfo('ผลการคำนวณ','ความยาวด้านตรงข้ามมุมฉากคือ {}'.format(calc_result))


B2 = ttk.Button(GUI,text='คำนวณ',command=Calc)
B2.pack(ipady=10,ipadx=10,pady=20)

E2.bind('<Return>', Calc)

GUI.mainloop()