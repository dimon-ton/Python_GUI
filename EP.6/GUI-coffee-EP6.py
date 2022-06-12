import webbrowser
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import csv
import wikipedia
from datetime import datetime

def writetocsv(data, filename='data.csv'):
    with open(filename, 'a',newline='',encoding='utf-8') as file:
        fw = csv.writer(file)
        fw.writerow(data)

GUI = Tk()
GUI.title('โปรแกรมคำนวณ')
GUI.geometry('1100x600')

tab = ttk.Notebook(GUI)
tab.pack(fill=BOTH, expand=True)

T1 = Frame(tab)
T2 = Frame(tab)
T3 = Frame(tab)

icon_tab1 = PhotoImage(file='EP.4/tab1.png')
icon_tab2 = PhotoImage(file='EP.4/tab2.png')
icon_tab3 = PhotoImage(file='EP.5/tab3.png')

tab.add(T1, text='กุ้ง',image=icon_tab1, compound='left')
tab.add(T2, text='ค้นหาข้อมูล wikipedia',image=icon_tab2, compound='left')
tab.add(T3, text='CAFE',image=icon_tab3, compound='left')
#---------------------------------------TAB 1------------------------------------------
#---------------------------------------Shrimp Selling Calculator----------------------

L1 = Label(T1, text='กรอกจำนวนกุ้ง (กิโลกรัม)', font=('Angsana New', 25))
L1.pack(pady=10)

v_kilo = StringVar()

E1 = ttk.Entry(T1, textvariable = v_kilo, width=10, justify='right', font=('impact',30))
E1.pack(pady=20)
E1.focus()

def Calc(event=None):
    print('กำลังคำนวณ...กรุณารอสักครู่')
    kilo = float(v_kilo.get())
    print(kilo * 299)
    calc_result = kilo * 299
    datetime_data = datetime.now().strftime('%d-%m-%Y %H:%M:%S')
    data = [datetime_data, 'กุ้ง', '{:,.0f}'.format(kilo), '{:,.2f}'.format(calc_result)]
    writetocsv(data)
    messagebox.showinfo('รวมราคาทั้งหมด','ลูกค้าต้องจ่ายตังค์ทั้งหมด: {:,.2f} (กิโลกรัมละ 299 บาท)'.format(calc_result))

B1 = ttk.Button(T1, text='คำนวณราคา', command=Calc)
B1.pack(ipadx=40, ipady=30, pady=20)

E1.bind('<Return>',Calc) #ต้องใส่ event=None ไว้ในฟังชันก์ด้วย

#---------------------------------------TAB 2--------------------------------------
#---------------------------------------Wikipedia Search---------------------------
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
        result_url = page.url
        print(result_url)

        def URL():
            webbrowser.open(result_url, new=2)

        b_more = ttk.Button(T2, text='more info', command=URL)
        b_more.pack(ipadx=10, ipady=10)  
        
    except:
        v_result.set('ไม่มีข้อมูล')



B2 = ttk.Button(T2, text='ค้นหา', image=icon_tab2, compound='left', command=Search)
B2.pack(pady=10,ipadx=10, ipady=10)

v_result = StringVar()
v_result.set('--------------Result----------------')
result = Label(T2, textvariable=v_result, wraplength=550, justify='left', font=(None,10))
result.pack()

E2.bind('<Return>', Search)

#---------------------------------------TAB 3--------------------------------------
#---------------------------------------Coffee Cafe--------------------------------

Bfont = ttk.Style()
Bfont.configure('TButton',font=('Angsana New', 16))

# ROW0
CF1 = Frame(T3)
CF1.place(x=50, y=100)

allmenu = {}

product = {'latte':{'name':'ลาเต้','price':30},
            'cappuccino':{'name':'คาปูชิโน่','price':35},
            'expresso':{'name':'เอสเปรสโซ่','price':40},
            'icegreentea':{'name':'ชาเขียวเย็น','price':40},
            'icetea':{'name':'ชาเย็น','price':40},
            'hottea':{'name':'ชาร้อน','price':35}}


def UpdateTable():
    table.delete(*table.get_children()) #เคลียร์ข้อมูลเก่าในตาราง
    for i, m in enumerate(allmenu.values()):
        table.insert('', 'end', values=[i, m[0], m[1],m[2], m[3]])

    

def AddMenu(name='latte'):
    # name = 'latte'
    if name not in allmenu:
        allmenu[name] = [product[name]['name'], product[name]['price'], 1, product[name]['price']]
        
        # table.insert('', 'end', value=[1, 'ลาเต้', 1, 30, 30])
    else:
        quan = allmenu[name][2] + 1
        total = quan * product[name]['price']
        allmenu[name] = [product[name]['name'], product[name]['price'], quan, total]

    # resultTotal = 0
    # for a in allmenu:
    #     resultTotal += allmenu[a][3]
    # v_resultTotal.set(f'รวมราคา: {resultTotal} บาท')
    count = sum([ m[3] for m in allmenu.values()])
    v_total.set('{:,.2f}'.format(count))
    
    print(allmenu)
    UpdateTable()
    # print(resultTotal)




# def Clear():
#     v_resultTotal.set('')
#     allmenu.clear()
#     for i in table.get_children():
#         table.delete(i)


# ROW1

B = ttk.Button(CF1, text='ลาเต้', image=icon_tab3, compound='top', command=lambda m='latte': AddMenu(m))
B.grid(row=0, column=0, ipadx=20, ipady=10)

B = ttk.Button(CF1, text='คาปูชิโน่', image=icon_tab3, compound='top', command=lambda m='cappuccino': AddMenu(m))
B.grid(row=0, column=1, ipadx=20, ipady=10)

B = ttk.Button(CF1, text='เอ็กเปรสโซ่', image=icon_tab3, compound='top', command=lambda m='expresso': AddMenu(m))
B.grid(row=0, column=2, ipadx=20, ipady=10)

B = ttk.Button(CF1, text='ชาเขียวเย็น', image=icon_tab3, compound='top', command=lambda m='icegreentea': AddMenu(m))
B.grid(row=1, column=0, ipadx=20, ipady=10)

B = ttk.Button(CF1, text='ชาเย็น', image=icon_tab3, compound='top', command=lambda m='icetea': AddMenu(m))
B.grid(row=1, column=1, ipadx=20, ipady=10)

B = ttk.Button(CF1, text='ชาร้อน', image=icon_tab3, compound='top', command=lambda m='hottea': AddMenu(m))
B.grid(row=1, column=2, ipadx=20, ipady=10)


# table
CF2 = Frame(T3)
CF2.place(x=500, y=100)

header = ['No.', 'title', 'price', 'qualtity', 'total']
hwidth = [50, 180, 100, 100, 100]

table = ttk.Treeview(CF2, columns=header, show='headings', height=15)
table.pack()

# for hd in header:
#     table.heading(hd, text=hd)

for hd, hw in zip(header, hwidth):
    table.heading(hd, text=hd) #ใส่หัวตาราง
    table.column(hd ,width=hw) #ปรับความกว้างของคอลัมน์

v_resultTotal = StringVar()
total_label = ttk.Label(CF2, textvariable=v_resultTotal, anchor='w', font=('Angsana New', 18))
total_label.pack(pady=10, fill='both')

L = ttk.Label(T3, text='Total: ', font=(None, 15)).place(x=500, y=450)

v_total = StringVar()
v_total.set('0.0')
LT = ttk.Label(T3, textvariable=v_total, font=(None, 15))
LT.place(x=560, y=450)


def Reset():
    global allmenu
    allmenu = {}
    table.delete(*table.get_children())
    v_total.set('0.0')
    trStamp = datetime.now().strftime('%y%m%d%H%M%S') # generate transaction ID
    v_transaction.set(trStamp)

B = ttk.Button(T3, text='Reset', command=Reset).place(x=500, y=500)
# BClear = ttk.Button(CF2, text='เคลียร์ข้อมูล', command=Clear)
# BClear.pack(pady=5)

# Transaction ID
v_transaction = StringVar()
trStamp = datetime.now().strftime('%y%m%d%H%M%S') # generate transaction ID
v_transaction.set(trStamp)
LTR = Label(T3, textvariable=v_transaction, font=(None, 10)).place(x=940, y=70)

# Save Button
FB = Frame(T3)
FB.place(x=940, y=500)

def AddTransaction():
    #writetocsv('transaction.csv')
    stamp = datetime.now().strftime('%y-%m-%d %H:%M:%S')
    transaction = v_transaction.get()
    print(transaction, stamp, allmenu.values())
    for m in allmenu.values():
        m.insert(0, transaction)
        m.insert(1,stamp)
        writetocsv(m, 'transaction.csv')

    Reset() # Clear Data
    messagebox.showinfo('หน้าต่างแสดงสถานะ', 'บันทึกข้อมูลเรียบร้อย')

B = ttk.Button(FB, text='บันทึก', command=AddTransaction)
B.pack(ipadx=10, ipady=10)

# History PopUp
def HistoryWindow(event=None):
    HIS = Toplevel()
    HIS.geometry('750x500')

    L = ttk.Label(HIS, text='ประวัติการสั่งซื้อ', font=('Angsana New', 16)).pack()
    

    header = ['TS-ID', 'DateTime', 'title', 'price', 'qualtity', 'total']
    hwidth = [100, 100, 180, 100, 100, 100]

    table_history = ttk.Treeview(HIS, columns=header, show='headings', height=15)
    table_history.pack()

    # for hd in header:
    #     table.heading(hd, text=hd)

    for hd, hw in zip(header, hwidth):
        table_history.heading(hd, text=hd) #ใส่หัวตาราง
        table_history.column(hd ,width=hw) #ปรับความกว้างของคอลัมน์
        # update from CSV
    with open('transaction.csv', newline='', encoding='utf-8') as file:
        fr = csv.reader(file)
        for row in fr:
            table_history.insert('', 0, value=row)

    HIS.mainloop()

GUI.bind('<F1>', HistoryWindow)

GUI.mainloop()