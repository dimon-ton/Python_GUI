from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import csv
from datetime import datetime

def writetocsv(data):
    with open('data.csv','a',newline='',encoding='utf-8') as file:
        fw = csv.writer(file)
        fw.writerow(data)

GUI = Tk()
GUI.title('โปรแกรมคำนวณ')
GUI.geometry('500x300')

L1 = Label(GUI,text='กรอกจำนวนกุ้ง (กิโลกรัม)',font=('Angsana New',25))
L1.pack()

v_kilo = StringVar()

E1 = ttk.Entry(GUI, textvariable = v_kilo, width=10, justify='right', font=('impact',30))
E1.pack(pady=20)

def Calc(event=None):
    print('กำลังคำนวณ...กรุณารอสักครู่')
    kilo = float(v_kilo.get())
    print(kilo * 299)
    calc_result = kilo * 299
    datetime_data = datetime.now().strftime('%d-%m-%Y %H:%M:%S')
    data = [datetime_data, 'กุ้ง', '{:,.0f}'.format(kilo), '{:,.2f}'.format(calc_result)]
    writetocsv(data)
    messagebox.showinfo('รวมราคาทั้งหมด','ลูกค้าต้องจ่ายตังค์ทั้งหมด: {:,.2f} (กิโลกรัมละ 299 บาท)'.format(calc_result))

B1 = ttk.Button(GUI,text='คำนวณราคา',command=Calc)
B1.pack(ipadx=40,ipady=30,pady=20)

E1.bind('<Return>',Calc) #ต้องใส่ event=None ไว้ในฟังชันก์ด้วย

GUI.mainloop()