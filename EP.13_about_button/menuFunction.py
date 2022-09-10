from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from productdb import *
import os


class ProductIcon:
    def __init__(self):
        self.quantity = None
        self.table_product = None
        self.v_radio = None
        self.button_list = None
        self.button_frame = None
    
    def popup(self):
        # Product GUI
        PGUI = Toplevel()
        PGUI.geometry('500x500')
        PGUI.title('ตั้งค่า --> แสดงรายการสินค้า')
    
        header = ['ID', 'รหัสสินค้า', 'ชื่อสินค้า', 'แสดงไอคอน']
        hwidth = [40, 60, 200, 80]

        self.table_product = ttk.Treeview(PGUI, columns=header, show='headings', height=15)
        self.table_product.pack()

        # for hd in header:
        #     table_member.heading(hd, text=hd)

        for hd, hw in zip(header, hwidth):
            self.table_product.heading(hd, text=hd) #ใส่หัวตาราง
            self.table_product.column(hd ,width=hw) #ปรับความกว้างของคอลัมน์

        
        self.table_product.bind('<Double-1>', self.change_status)
        self.insert_table()

        PGUI.mainloop()

    def command(self):
        self.popup()

    def change_status(self, event=None):
        select = self.table_product.selection()
        pid = self.table_product.item(select)['values'][0]
        print('PID: ',pid)

        SGUI = Toplevel()
        SGUI.geometry('400x200')
        self.v_radio = StringVar()
        RB1 = ttk.Radiobutton(SGUI, text='Show Icon', variable=self.v_radio, value='show', command=lambda x=None: insert_product_status(int(pid), 'show'))
        RB2 = ttk.Radiobutton(SGUI, text='Not Show Icon', variable=self.v_radio, value='', command=lambda x=None: insert_product_status(int(pid), ''))
        #RB1.invoke() # เขตค่า Default ของ  radio button

        RB1.pack(pady=20)
        RB2.pack()

        check = View_product_status(pid)

        if check[-1] == 'show':
            RB1.invoke()
        else:
            RB2.invoke()

        # Dropdown
        '''
        dropdown = ttk.Combobox(SGUI, values=['แสดงไอคอน', 'ไม่แสดงไอคอน'])
        dropdown.pack()
        '''

        def check_close():
            print('closed')
            SGUI.destroy()
            self.insert_table()
            self.clearButton()
            self.create_button()

        SGUI.protocol('WM_DELETE_WINDOW', check_close)


        SGUI.mainloop()

    def insert_table(self):
        self.table_product.delete(*self.table_product.get_children())
        data = View_product_table_icon()
        for d in data:
            row = list(d)

            check = View_product_status(row[0])

            # โชว์สถานะของการนำสินค้าไปใช้

            if check[-1] == 'show':
                row.append('✅')
            else:
                row.append('')

            self.table_product.insert('', 'end', values=row)

     # Refresh หน้าแสดงปุ่ม
    def clearButton(self):
        for b in self.button_list.values():
            b['button'].destroy()

    def create_button(self):

        product = product_icon_list()

        global button_dict
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

            B = ttk.Button(self.button_frame, text=v['name'], compound='top')
            button_dict[v['id']] = {'button':B, 'row':row, 'column':column}

            B.configure(image=new_icon)
            B.image = new_icon

            B.configure(command=lambda m=k: AddMenu(m))
            B.grid(row=row, column=column)
            column += 1

        self.button_list = button_dict

class AddProduct:
    def __init__(self):
        self.v_productid = None
        self.v_title = None
        self.v_price = None
        self.v_imgpath = None
        self.MGUI = None
        self.ProductImage = None
        self.button_list = None
        self.button_frame = None

    def popup(self):
        self.MGUI = Toplevel()
        self.MGUI.geometry('500x700')
        self.MGUI.title('Add Product')

        self.v_productid = StringVar()
        self.v_title = StringVar()
        self.v_price = StringVar()
        self.v_imgpath = StringVar()

        L = Label(self.MGUI, text='เพิ่มรายการสินค้า', font=(None, 30))
        L.pack()

        
        L = Label(self.MGUI, text='รหัสสินค้า', font=(None, 30))
        L.pack(pady=10)

        
        E2 = ttk.Entry(self.MGUI, textvariable=self.v_productid, font=(None, 20))
        E2.pack(pady=10)

        L = Label(self.MGUI, text='ชื่อสินค้า', font=(None, 30))
        L.pack(pady=10)

        
        E3 = ttk.Entry(self.MGUI, textvariable=self.v_title, font=(None, 20))
        E3.pack(pady=10)

        L = Label(self.MGUI, text='ราคา', font=(None, 30))
        L.pack(pady=10)

        
        E4 = ttk.Entry(self.MGUI, textvariable=self.v_price, font=(None, 20))
        E4.pack(pady=10)

        img = PhotoImage(file='EP.13_about_button\default_icon.png')

        self.ProductImage = Label(self.MGUI, textvariable=self.v_imgpath, image=img, compound='top')
        self.ProductImage.pack()

        Bselect = ttk.Button(self.MGUI, text='เลือกรูปสินค้า (120 x 120 px)', command=self.selectFile)
        Bselect.pack(pady=10)

        Bsave = ttk.Button(self.MGUI, text='บันทึก', command=self.saveproduct)
        Bsave.pack(pady=10, ipadx=20, ipady=10)

        self.MGUI.mainloop()

    def selectFile(self):
        filetypes = (
            ('PNG','*.png'),
            ('All files', '*.*')
        )
        DIR = os.getcwd() # ตำแหน่งโฟลเดอร์โปรแกรม DIR
        select = filedialog.askopenfilename(title='เลือกไฟล์ภาพ', initialdir=DIR, filetypes=filetypes)
        img = PhotoImage(file=select)
        self.ProductImage.configure(image=img)
        self.ProductImage.image = img

        self.v_imgpath.set(select)
        self.MGUI.focus_force() # โฟกัสหน้าต่างที่ select
        self.MGUI.grab_set()

    def command(self):
        self.popup()

    def saveproduct(self):
        v1 = self.v_productid.get()
        v2 = self.v_title.get()
        v3 = float(self.v_price.get())
        v4 = self.v_imgpath.get()

        Insert_product(v1, v2, v3, v4)

        self.v_productid.set('')
        self.v_title.set('')
        self.v_price.set('')
        self.v_imgpath.set('')
        View_product()

        self.clearButton()
        self.create_button()
    # Refresh หน้าแสดงปุ่ม
    def clearButton(self):
        for b in self.button_list.values():
            b['button'].destroy()

    def create_button(self):

        product = product_icon_list()

        global button_dict
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

            B = ttk.Button(self.button_frame, text=v['name'], compound='top')
            button_dict[v['id']] = {'button':B, 'row':row, 'column':column}

            B.configure(image=new_icon)
            B.image = new_icon

            B.configure(command=lambda m=k: AddMenu(m))
            B.grid(row=row, column=column)
            column += 1

            # self.button_list = button_dict