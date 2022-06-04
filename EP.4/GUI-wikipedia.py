import webbrowser
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import csv
import fontTools
import wikipedia
from datetime import datetime

def writetocsv(data):
    with open('data.csv','a',newline='',encoding='utf-8') as file:
        fw = csv.writer(file)
        fw.writerow(data)

GUI = Tk()
GUI.title('โปรแกรมคำนวณ')
GUI.geometry('800x600')

tab = ttk.Notebook(GUI)
tab.pack(fill=BOTH, expand=True)

T1 = Frame(tab)
T2 = Frame(tab)

icon_tab1 = PhotoImage(file='EP.4/tab1.png')
icon_tab2 = PhotoImage(file='EP.4/tab2.png')

tab.add(T1, text='กุ้ง',image=icon_tab1, compound='left')
tab.add(T2, text='ค้นหาข้อมูล wikipedia',image=icon_tab2, compound='left')
#---------------------------------------TAB 1------------------------------------------

L1 = Label(T1,text='กรอกจำนวนกุ้ง (กิโลกรัม)',font=('Angsana New',25))
L1.pack(pady=10)

v_kilo = StringVar()

E1 = ttk.Entry(T1, textvariable = v_kilo, width=10, justify='right', font=('impact',30))
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

B1 = ttk.Button(T1,text='คำนวณราคา',command=Calc)
B1.pack(ipadx=40,ipady=30,pady=20)

E1.bind('<Return>',Calc) #ต้องใส่ event=None ไว้ในฟังชันก์ด้วย

#---------------------------------------TAB 2--------------------------------------
FONT1 = ('Angsana New', 25)
L2 = Label(T2, text='ค้นหาข้อมูล wikipedia', font=FONT1,)
L2.pack(pady=10)

v_search = StringVar()
E2 = ttk.Entry(T2, textvariable=v_search, font=FONT1)
E2.pack(pady=10)

wikipedia.set_lang('th')

def Search(event=None):
    try:
        search = v_search.get()
        text = wikipedia.summary(search)
        print(text)
        v_result.set(text[:1000])

        page = wikipedia.page(search)

        def URL():
            webbrowser.open(page.url, new=2)

        B_moreInfo = ttk.Button(T2, text='more info', command=URL)
        B_moreInfo.pack(ipadx=10, ipady=10)
        
    except:
        v_result.set('ไม่มีข้อมูล')



B2 = ttk.Button(T2, text='ค้นหา', image=icon_tab2, compound='left', command=Search)
B2.pack(pady=10,ipadx=10, ipady=10)

v_result = StringVar()
v_result.set('--------------Result----------------')
result = Label(T2, textvariable=v_result, wraplength=550, justify='left', font=(None,10))
result.pack()
E2.bind('<Return>', Search)

GUI.mainloop()