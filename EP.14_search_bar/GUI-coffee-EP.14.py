import webbrowser
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import csv
from datetime import datetime
from memberdb import *
from productdb import *
from menuFunction import *
import requests

from bill import printBill




# write data to csv
def writetocsv(data, filename='data.csv'):
    with open(filename, 'a',newline='',encoding='utf-8') as file:
        fw = csv.writer(file)
        fw.writerow(data)

# create qrcode for payment
def QRImage(price=100, account='0887263735'):
    url='https://promptpay.io/{}/{:.2f}'.format(account, price)
    response = requests.get(url)
    if response.status_code == 200:
        with open("EP.14_search_bar/qr-payment.png", "wb") as image:
            image.write(response.content)



GUI = Tk()
GUI.title('โปรแกรมบันทึกการขายสินค้า')
GUI.iconbitmap('EP.8\Kzzu-I-Love-You-Coffee-brown.ico')
#full screen after run
# GUI.state('zoomed')

#----------------------------------------------------------------
style  = ttk.Style()
style.configure('Treeview.Heading', font=(None, 12))
style.configure('Treeview', font=(None, 12))
#----------------------------------------------------------------

W = 1200
H = 630
MW = GUI.winfo_screenwidth()
MH = GUI.winfo_screenheight()

SX = (MW/2) - (W/2)
SY = (MH/2) - (H/2)
SY = SY -50

GUI.geometry('{}x{}+{:.0f}+{:.0f}'.format(W, H, SX, SY))

# df = nametofont("TkDefaultFont")
# df.configure(family="Angsana New", size=12)
GUI.option_add("*Font", "aerial")

#----------------------------------Menu Bar------------------------------
menubar = Menu(GUI)
GUI.config(menu=menubar)
#------------------------------------------------------------------------
# File Menu
filemenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label='File', menu=filemenu)
def ExportDatabase():
    print('export database to csv')
    
filemenu.add_command(label='Export', command=ExportDatabase)
filemenu.add_command(label='Exit', command=lambda: GUI.destroy())
#------------------------------------------------------------------------
# Member Menu
member_menu = Menu(menubar, tearoff=0)
menubar.add_cascade(label='Member', menu=member_menu)
#------------------------------------------------------------------------
# Product Menu
addproduct = AddProduct()

Productmenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label='Product', menu=Productmenu)
Productmenu.add_command(label='Add Product', command=addproduct.command)
#------------------------------------------------------------------------
# Setting
product_icon = ProductIcon()

settingmenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label='Setting', menu=settingmenu)
settingmenu.add_command(label='Product Icon', command=product_icon.command)

#------------------------------------------------------------------------
# Help Menu
help_menu = Menu(menubar, tearoff=0)
menubar.add_cascade(label='Help', menu=help_menu)
help_menu.add_command(label='Contact US', command=lambda: webbrowser.open('https://www.facebook.com/saichon.namoom/'))




def About():
    ABGUI = Toplevel()
    ABGUI.title('about Me')
    ABGUI.iconbitmap('EP.8\Kzzu-I-Love-You-Coffee-brown.ico')
    W = 300
    H = 200
    MW = GUI.winfo_screenwidth()
    MH = GUI.winfo_screenheight()

    SX = (MW/2) - (W/2)
    SY = (MH/2) - (H/2)
    SY = SY -50

    ABGUI.geometry('{}x{}+{:.0f}+{:.0f}'.format(W, H, SX, SY))
    L = Label(ABGUI, text='โปรแกรมร้านกาแฟ', fg='green', font=('Angsana New', 30)).pack()
    L = Label(ABGUI, text='พัฒนาโดย Pimon Tungratog', font=('Angsana New', 20)).pack()

    ABGUI.mainloop()

help_menu.add_command(label='ABOUT', command=About)
#------------------------------------------------------------------------
tab = ttk.Notebook(GUI)
tab.pack(fill=BOTH, expand=True)



T3 = Frame(tab)
T4 = Frame(tab)

icon_tab1 = PhotoImage(file='EP.4/tab1.png')
icon_tab2 = PhotoImage(file='EP.4/tab2.png')
icon_tab3 = PhotoImage(file='EP.5/tab3.png')
icon_tab4 = PhotoImage(file='EP.7/tab4.png')



tab.add(T3, text='CAFE',image=icon_tab3, compound='left')
tab.add(T4, text='Member',image=icon_tab4, compound='left')


#---------------------------------------TAB 3--------------------------------------
#---------------------------------------Coffee Cafe--------------------------------

Bfont = ttk.Style()
Bfont.configure('TButton',font=('Angsana New', 16))

# Accessory
CF1 = Frame(T3)
CF1.place(x=50, y=100)

# check member if they exist
def set_member():
    GUIM = Toplevel()
    W = 300
    H = 200
    MW = GUIM.winfo_screenwidth()
    MH = GUIM.winfo_screenheight()

    SX = (MW/2) - (W/2)
    SY = (MH/2) - (H/2)
    SY = SY -50

    GUIM.geometry('{}x{}+{:.0f}+{:.0f}'.format(W, H, SX, SY))
    GUIM.focus_force()


    L = ttk.Label(GUIM, text='non-member')
    L.pack(pady=20)

    v_member.set('')
    EMember = ttk.Entry(GUIM, textvariable=v_member, font=(None, 20))
    EMember.pack(padx=20)
    EMember.focus()

    def Check(event=None):
        c = Check_member(v_member.get())
        if c == True:
            v_member.set(v_member.get())
            LM.configure(foreground='green')
            GUIM.destroy()
        else:
            v_member.set('non-member')
            LM.configure(foreground='red')

    B = ttk.Button(GUIM, text='Check', command=Check)
    B.pack(pady=20)

    
    
    def close_window(evemt=None):
        v_member.set('non-member')
        GUIM.destroy()
        LM.configure(foreground='red')
    
    GUIM.protocol('WM_DELETE_WINDOW', close_window)

    GUIM.bind('<Return>', Check)
    GUIM.mainloop()


img_member = PhotoImage(file='EP.14_search_bar/man-icon.png')
Bmember = ttk.Button(T3, image=img_member, command=set_member)
Bmember.place(x=50, y=30)

v_member = StringVar()
v_member.set('non-member')

LM = ttk.Label(T3, textvariable=v_member, font=(None, 15))
LM.place(x=120, y=50)

LM.configure(foreground='red')




allmenu = {}
'''
product = {'latte':{'name':'ลาเต้','price':30},
            'cappuccino':{'name':'คาปูชิโน่','price':35},
            'expresso':{'name':'เอสเปรสโซ่','price':40},
            'icegreentea':{'name':'ชาเขียวเย็น','price':40},
            'cocoa':{'name':'โกโก้','price':50},
            'icetea':{'name':'ชาเย็น','price':40},
            'hottea':{'name':'ชาร้อน','price':35}}
'''


product = product_icon_list()


def UpdateTable():
    table.delete(*table.get_children()) #เคลียร์ข้อมูลเก่าในตาราง
    for i, m in enumerate(allmenu.values(), start=1):
        table.insert('', 'end', values=[i, m[0], m[1],m[2], m[3], m[4]])

    

def AddMenu(name='latte'):
    # name = 'latte'
    if name not in allmenu:
        allmenu[name] = [product[name]['id'], product[name]['name'], product[name]['price'], 1, product[name]['price']]
        
        # table.insert('', 'end', value=[1, 'ลาเต้', 1, 30, 30])
    else:
        quan = allmenu[name][3] + 1
        total = quan * product[name]['price']
        allmenu[name] = [product[name]['id'], product[name]['name'], product[name]['price'], quan, total]

    # resultTotal = 0
    # for a in allmenu:
    #     resultTotal += allmenu[a][3]
    # v_resultTotal.set(f'รวมราคา: {resultTotal} บาท')
    count = sum([ m[4] for m in allmenu.values()])
    v_total.set('{:,.2f}'.format(count))
    
    print('----> ALLMENU', allmenu)
    UpdateTable()
    # print(resultTotal)




# def Clear():
#     v_resultTotal.set('')
#     allmenu.clear()
#     for i in table.get_children():
#         table.delete(i)


# Order Button

button_dict = {}

row = 0
column = 0
column_quan = 3 # ปรับค่านี้เพื่อสร้างจำนวนคอลัมน์

for i, (k, v) in enumerate(product.items()):
    if column == column_quan:
        column = 0
        row += 1

    print('IMG: ', v['icon'])
    new_icon = PhotoImage(file=v['icon'])

    B = ttk.Button(CF1, text=v['name'], compound='top')
    button_dict[v['id']] = {'button':B, 'row':row, 'column':column}

    B.configure(image=new_icon)
    B.image = new_icon

    B.configure(command=lambda m=k: AddMenu(m))
    B.grid(row=row, column=column)
    column += 1

addproduct.button_list = button_dict
addproduct.button_frame = CF1

product_icon.button_list = button_dict
product_icon.button_frame = CF1

print(button_dict)
def testclearButton(event):
    for b in button_dict.values():
        b['button'].grid_forget()

GUI.bind('<F5>', testclearButton)

'''
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
'''

# table
CF2 = Frame(T3)
CF2.place(x=500, y=100)

header = ['No.','ID' , 'title', 'price', 'qualtity', 'total']
hwidth = [50, 100, 180, 100, 100, 100]

table = ttk.Treeview(CF2, columns=header, show='headings', height=15)
table.pack()

# for hd in header:
#     table.heading(hd, text=hd)

for hd, hw in zip(header, hwidth):
    table.heading(hd, text=hd) #ใส่หัวตาราง
    table.column(hd ,width=hw) #ปรับความกว้างของคอลัมน์

# Delete product from table
def DeleteProduct(event=None):
    choice = messagebox.askyesno('ลบรายการ', 'คุณต้องการลบข้อมูลใช่หรือไม่')
    print(choice)
    if choice == True:
        select = table.selection() #เลือก item
        if len(select) != 0:
            data = table.item(select)['values']
            print(data)
            del allmenu[data[1]]
            # update total
            count = sum([ m[4] for m in allmenu.values()])
            v_total.set('{:,.2f}'.format(count))
            # upate table
            UpdateTable()
 
        else:
            messagebox.showwarning('เกิดข้อผิดพลาด', 'กรุณาเลือกรายการก่อนลบข้อมูล')
    else:
        pass

table.bind('<Delete>', DeleteProduct)

# Update quantity table
def UpdateQuantity(event=None):
    GUIQ = Toplevel()

    W = 300
    H = 200
    MW = GUI.winfo_screenwidth()
    MH = GUI.winfo_screenheight()

    SX = (MW/2) - (W/2)
    SY = (MH/2) - (H/2)
    SY = SY -50

    L = Label(GUIQ, text="กรุณากรอกจำนวนสินค้า", font=(None,20)).pack(pady=20)

    v_newquan = IntVar()
    v_newquan.set(1)
    E1 = ttk.Entry(GUIQ, textvariable=v_newquan, font=(None, 20))
    E1.pack(padx=20)
    E1.focus()

    select = table.selection() #เลือก item
    print(select)
    if len(select) != 0:
        data = table.item(select)['values']
        print(data)
        
        sid = data[1]
        current_quan = data[4]
        v_newquan.set(current_quan)

    else:
        messagebox.showwarning('เกิดข้อผิดพลาด', 'กรุณาเลือกรายการก่อนแก้ไขข้อมูล')

    def save_update(event=None):

        allmenu[sid][3] = v_newquan.get()
        allmenu[sid][4] = v_newquan.get() * float(allmenu[sid][2]) # multiply by price

        # update total
        count = sum([ m[4] for m in allmenu.values()])
        v_total.set('{:,.2f}'.format(count))
        # upate table
        UpdateTable()
        GUIQ.destroy()


    B1 = ttk.Button(GUIQ, text='บันทึก', command=save_update)
    B1.pack(ipadx=20, ipady=10, pady=20)

    GUIQ.bind('<Return>', save_update)

    GUIQ.geometry('{}x{}+{:.0f}+{:.0f}'.format(W, H, SX, SY))
    GUIQ.focus_force()
    GUIQ.bind('<Escape>', lambda x: GUIQ.destroy())

    E1.bind('<Up>', lambda x: v_newquan.set(v_newquan.get() + 1))
    E1.bind('<Down>', lambda x: v_newquan.set(v_newquan.get() - 1))

    GUIQ.mainloop()

table.bind('<F12>', UpdateQuantity)

# Sum result

# v_resultTotal = StringVar()
# total_label = ttk.Label(CF2, textvariable=v_resultTotal, anchor='w', font=('Angsana New', 18))
# total_label.pack(pady=10, fill='both')

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
LTR = Label(T3, textvariable=v_transaction, font=(None, 10)).place(x=1020, y=70)

# Save Button
FB = Frame(T3)
FB.place(x=940, y=500)

def AddTransaction():
    #writetocsv('transaction.csv')
    stamp = datetime.now().strftime('%y-%m-%d %H:%M:%S')
    transaction = v_transaction.get()
    print(transaction, stamp, allmenu.values())
    for m in allmenu.values():
        del m[0]
        m.insert(0, transaction)
        m.insert(1,stamp)
        writetocsv(m, 'transaction.csv')

    Reset() # Clear Data
    messagebox.showinfo('หน้าต่างแสดงสถานะ', 'บันทึกข้อมูลเรียบร้อย')


def Checkout(event=None):
    GUICO = Toplevel()

    W = 800
    H = 900
    MW = GUI.winfo_screenwidth()
    MH = GUI.winfo_screenheight()

    SX = (MW/2) - (W/2)
    SY = (MH/2) - (H/2)
    SY = SY -50
    GUICO.geometry('{}x{}+{:.0f}+{:.0f}'.format(W, H, SX, SY))
    GUICO.focus_force()

    # Calculate discount
    global total
    if v_member.get() != 'non-member':
        discount = float(v_total.get().replace(',','')) * 0.05
        total = float(v_total.get().replace(',','')) - discount
    else:
        discount = 0
        total = float(v_total.get().replace(',',''))


    text1 = 'ทั้งหมด {:,.2f}'.format(total)
    L = Label(GUICO, text=text1,fg='green', font=(None,20)).pack(pady=10)

    text2 = 'ส่วนลด {:,.2f}'.format(discount)
    L = Label(GUICO, text=text2,fg='blue', font=(None,20)).pack(pady=10)

    text3 = 'ปกติ {}'.format(v_total.get())
    L = Label(GUICO, text=text3, font=(None,20)).pack(pady=10)

    v_change = StringVar()
    L2 = Label(GUICO, textvariable=v_change, fg='orange', font=(None, 20)).pack(pady=20)
    v_change.set('--------------เงินทอน--------------')


    v_cash = DoubleVar()
    v_cash.set(0)
    E1 = ttk.Entry(GUICO, textvariable=v_cash, font=(None, 20))
    E1.pack(padx=20)
    E1.focus()

    global state
    state = 1

    def save(event=None):
        global total
        global state
        if state == 1:
            total = total
            calc = v_cash.get() - total
            v_change.set('จำนวนเงินทอน: {:,.2f} บาท'.format(calc))
            state += 1
            Bchange.config(text='บันทึก')
        elif state == 2:
            # ------------------- print bill -------------------------
            printout = []

            for m in allmenu.values():
                printout.append(m[1:])

            # run function print bill

            printBill(product=printout, printer=False, openfile=True)

            AddTransaction()
            state = 1
            Bchange.config(text='ยืนยันการบันทึก')
            
            




    Bchange = ttk.Button(GUICO, text='คำนวณเงินทอน', command=save)
    Bchange.pack(ipadx=20, ipady=10, pady=20)

    QRImage(total)

    img = PhotoImage(file='EP.14_search_bar/qr-payment.png')
    qrcode = Label(GUICO, image=img).pack()
    

    # banknote function
    global v_banknote
    v_banknote = 0
    def Banknote(banktype):
        global v_banknote
        v_banknote += banktype
        print('Current bank accumulation: ', v_banknote)
        v_cash.set(v_banknote)


    BF = Frame(GUICO)
    BF.pack(pady=20)

    img_BN1 = PhotoImage(file='EP.14_search_bar/banknote/b1000.png')
    BN1 = ttk.Button(BF, image=img_BN1, command=lambda b=1000: Banknote(b))
    BN1.grid(row=0,column=0, padx=10, pady=10)

    img_BN2 = PhotoImage(file='EP.14_search_bar/banknote/b500.png')
    BN2 = ttk.Button(BF, image=img_BN2, command=lambda b=500: Banknote(b))
    BN2.grid(row=0,column=1, padx=10, pady=10)

    img_BN3 = PhotoImage(file='EP.14_search_bar/banknote/b100.png')
    BN3 = ttk.Button(BF, image=img_BN3, command=lambda b=100: Banknote(b))
    BN3.grid(row=0,column=2, padx=10, pady=10)

    img_BN4 = PhotoImage(file='EP.14_search_bar/banknote/b50.png')
    BN4 = ttk.Button(BF, image=img_BN4, command=lambda b=50: Banknote(b))
    BN4.grid(row=1,column=0, padx=10, pady=10)

    img_BN5 = PhotoImage(file='EP.14_search_bar/banknote/b20.png')
    BN5 = ttk.Button(BF, image=img_BN5, command=lambda b=20: Banknote(b))
    BN5.grid(row=1,column=1, padx=10, pady=10)


    BN5 = ttk.Button(BF, text='10', command=lambda b=10: Banknote(b))
    BN5.grid(row=1,column=2, padx=10, pady=10)

    L = ttk.Label(GUICO, text='* กดปุ่ม F12 เพื่อรีเซ็ตจำนวนเงิน').pack()

    def clear_banknote(event=None):
        global v_banknote
        v_banknote = 0
        v_cash.set(0)


    GUICO.bind('<F12>', clear_banknote)
    GUICO.bind('<Return>', save)

    GUICO.bind('<Escape>', lambda x: GUICO.destroy())

    E1.bind('<Up>', lambda x: v_cash.set(v_cash.get() + 100))
    E1.bind('<Down>', lambda x: v_cash.set(v_cash.get() - 20))

    GUICO.mainloop()

B = ttk.Button(FB, text='บันทึก', command=Checkout)
B.pack(ipadx=10, ipady=10)


# search menu
FS1 = Frame(T3)
FS1.place(x=500, y=30)
v_search_barcode = StringVar()
Esearch = ttk.Entry(FS1, textvariable=v_search_barcode, font=('Angsana New', 25, 'bold'))
Esearch.grid(row=0, column=0, ipadx=25)

def searchBarcode(event=None):
    barcode = v_search_barcode.get()
    try:
        res = View_product_single(barcode)
        # print(res)
        pid = res[0]
        AddMenu(pid)
    except:
        messagebox.showwarning('Not Found','สินค้าไม่มีในระบบ')
        v_search_barcode.set('')
        Esearch.focus()

Esearch.bind('<Return>', searchBarcode)
Esearch.bind('<F3>', lambda event: v_search_barcode.set(''))


Bsearch = ttk.Button(FS1, text='ค้นหา', command=searchBarcode)
Bsearch.grid(row=0, column=1, ipadx=20, ipady=8, padx=10)


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
#---------------------------------------TAB 4 Member--------------------------------------
def ET(GUI, text, strVar, font=('Angsana New', 20)):
    T = Label(GUI, text=text, font=(None, 15)).pack()
    E = ttk.Entry(GUI, textvariable=strVar, font=font)
    return E

def ET2(GUI, text, strVar, font=('Angsana New', 20)):
    T = Label(GUI, text=text, font=(None, 15))
    E = ttk.Entry(GUI, textvariable=strVar, font=font)
    return (T,E)

def ET3(GUI, text, font=('Angsana New', 20)):
    v_strvar = StringVar()
    T = Label(GUI, text=text, font=(None, 15)).pack()
    E = ttk.Entry(GUI, textvariable=v_strvar, font=font, width=45)
    return (T,E, v_strvar)

# v_fullname = StringVar()
# E41 = ET(T4, 'ชื่อ-สกุล',v_fullname)
# E41.place(x=300, y=50)

# v_tel = StringVar()
# L, E42 = ET2(T4, 'เบอร์โทร', v_tel)
# E42.place(x=50, y=100)
# L.place(x=50, y=50)
F41 = Frame(T4)
F41.place(x=50, y=50)

v_memberCode = StringVar()
v_databaseCode = IntVar()

L = Label(T4, text='รหัสสมาชิก: ', font=('Angsana New', 14)).place(x=50, y=20)
LCode = Label(T4, textvariable=v_memberCode, font=('Angsana New', 14)).place(x=120, y=20)
v_memberCode.set('M-1001')

L, E41, v_fullname = ET3(F41, 'ชื่อ-สกุล')
E41.pack()

L, E42, v_tel = ET3(F41, 'เบอร์โทร')
E42.pack()

L, E44, v_point = ET3(F41, 'คะแนนสะสม')
E44.pack()

L, E43, v_usertype = ET3(F41, 'ประเภทสมาชิก')
E43.pack()
v_usertype.set('general')

v_point.set('0')

# v_usertype.set('TEST')
# E43.bind('<Return>', Lambda x: print(v_usertype.get()))

def SaveMember():
    code = v_memberCode.get()
    fullname = v_fullname.get()
    tel = v_tel.get()
    point = v_point.get()
    usertype = v_usertype.get()
    print(fullname, tel, point, usertype)
    #writetocsv([code, fullname, tel, usertype, point], 'member.csv') #บันทึกสมาชิกใหม่
    Insert_member(code, fullname, tel, usertype, point)
    #table_member.insert('', 0, values=[code, fullname, tel, usertype, point])
    UpdateTable_Member()

    v_fullname.set('')
    v_tel.set('')
    v_usertype.set('general')
    v_point.set('0')


BSave = ttk.Button(F41, text='บันทึก', command=SaveMember)
BSave.pack()
# Edit button
def EditMember():
    code = v_databaseCode.get() # get latest code from database
    allmember[code][2] = v_fullname.get()
    allmember[code][3] = v_tel.get()
    allmember[code][4] = v_usertype.get()
    allmember[code][5] = v_point.get()
    #updateCSV(list(allmember.values()), 'member.csv')
    Update_member(code, 'fullname', v_fullname.get())
    Update_member(code, 'tel', v_tel.get())
    Update_member(code, 'usertype', v_usertype.get())
    Update_member(code, 'points', v_point.get())

    UpdateTable_Member()

    v_fullname.set('')
    v_tel.set('')
    v_usertype.set('general')
    v_point.set('0')

    BEdit.state(['disabled'])
    BSave.state(['!disabled'])



BEdit = ttk.Button(F41, text='แก้ไข', command=EditMember)
BEdit.pack()
#New Button
def NewMember():
    UpdateTable_Member()

    v_fullname.set('')
    v_tel.set('')
    v_usertype.set('general')
    v_point.set('0')

    BEdit.state(['disabled'])
    BSave.state(['!disabled'])

BNew = ttk.Button(F41, text='New', command=NewMember).pack()

# Member Table
F42 = Frame(T4)
F42.place(x=500, y=50)

header = ['ID', 'Code', 'ชื่อ-สกุล', 'เบอร์โทร', 'ประเภทสมาชิก', 'คะแนนสะสม']
hwidth = [30, 50, 180, 100, 100, 100]

table_member = ttk.Treeview(F42, columns=header, show='headings', height=15)
table_member.pack()

# for hd in header:
#     table_member.heading(hd, text=hd)

for hd, hw in zip(header, hwidth):
    table_member.heading(hd, text=hd) #ใส่หัวตาราง
    table_member.column(hd ,width=hw) #ปรับความกว้างของคอลัมน์

#update CSV after DeleteMember
def updateCSV(data, filename='data.csv'):
    with open(filename, 'w',newline='',encoding='utf-8') as file:
        fw = csv.writer(file) #fw = file writer
        fw.writerows(data) # writes = replace with list

# delete data in table
def DeleteMember(event=None):
    choice = messagebox.askyesno('ลบรายการ', 'คุณต้องการลบข้อมูลใช่หรือไม่')
    print(choice)
    if choice == True:
        select = table_member.selection() #เลือก item
        if len(select) != 0:
            data = table_member.item(select)['values']
            print(data)
            del allmember[data[0]]
            Delete_member(data[0])
            #updateCSV(list(allmember.values()), 'member.csv')
            UpdateTable_Member()
        else:
            messagebox.showwarning('เกิดข้อผิดพลาด', 'กรุณาเลือกรายการก่อนลบข้อมูล')
    else:
        pass

table_member.bind('<Delete>', DeleteMember)


# Edit Table_member
def UpdateMemberInfo(event=None):
    select = table_member.selection()
    if len(select) != 0:
        code = table_member.item(select)['values'][0]
        v_databaseCode.set(code)
        memberinfo = allmember[code]
        v_memberCode.set(memberinfo[1])
        v_fullname.set(memberinfo[2])
        v_tel.set(memberinfo[3])
        v_point.set(memberinfo[5])
        v_usertype.set(memberinfo[4])

        BEdit.state(['!disabled'])
        BSave.state(['disabled'])
    else:
        messagebox.showwarning('เกิดข้อผิดพลาด','กรุณาเลือกรายการก่อนอัพเดทข้อมูล')

table_member.bind('<Double-1>', UpdateMemberInfo)


# Update Table_Member
last_member = '0'
allmember = {}

def UpdateTable_Member():
    global last_member
    fr = View_member()
    table_member.delete(*table_member.get_children())
    for row in fr:
        table_member.insert('', 0, value=row)
        code = row[0]
        allmember[code] = list(row) # convert tuple to list

    print(row)
    last_member = row[1] # select member code
    next_member = int(last_member.split('-')[1]) + 1
    v_memberCode.set('M-{}'.format(next_member))
    print(allmember)

# POP UP Menu
member_rcmenu = Menu(GUI, tearoff=0) # right click menu
member_rcmenu.add_command(label='Delete', command=DeleteMember)
member_rcmenu.add_command(label='Update', command=UpdateMemberInfo)


table_member.bind('<Button-3>', lambda event: member_rcmenu.post(event.x_root, event.y_root))

def SearchName():
    select = table_member.selection()
    if len(select) != 0:
        name = table_member.item(select)['values'][1]
        print('thekeyword: ', select)
        url = 'https://www.google.com/search?q={}'.format(name)
        webbrowser.open(url)
    else:
        messagebox.showwarning('เกิดข้อผิดพลาด','กรุณาเลือกข้อมูลก่อนการค้นหาข้อมูลด้วย Google')

member_rcmenu.add_command(label='Google Search Name', command=SearchName)

BEdit.state(['disabled'])
try:
    UpdateTable_Member()
except:
    print('กรุณากรอกข้อมูลอย่างน้อย 1 รายการ')
GUI.mainloop()