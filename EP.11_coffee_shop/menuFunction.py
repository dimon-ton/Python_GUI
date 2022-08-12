from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from productdb import *

class ProductIcon:
    def __init__(self):
        self.quantity = None
        self.table_product = None
        self.v_radio = None
    
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
        SGUI.geometry('400x400')
        self.v_radio = StringVar()
        RB1 = ttk.Radiobutton(SGUI, text='Show Icon', variable=self.v_radio, value='show', command=lambda x=None: insert_product_status(int(pid), 'show'))
        RB2 = ttk.Radiobutton(SGUI, text='Not Show Icon', variable=self.v_radio, value='', command=lambda x=None: insert_product_status(int(pid), ''))
        RB1.invoke() # เขตค่า Default ของ  radio button

        RB1.pack()
        RB2.pack()

        # Dropdown
        dropdown = ttk.Combobox(SGUI, values=['แสดงไอคอน', 'ไม่แสดงไอคอน'])
        dropdown.pack()

        SGUI.mainloop()

    def insert_table(self):
        data = View_product_table_icon()
        for d in data:
            row = list(d)
            row.append('✅')
            self.table_product.insert('', 'end', values=row)

class AddProduct:
    def __init__(self):
        self.v_productid = None
        self.v_title = None
        self.v_price = None
        self.v_imgpath = None

    def popup(self):
        MGUI = Toplevel()
        MGUI.geometry('500x600')
        MGUI.title('Add Product')

        self.v_productid = StringVar()
        self.v_title = StringVar()
        self.v_price = StringVar()
        self.v_imgpath = StringVar()

        L = Label(MGUI, text='เพิ่มรายการสินค้า', font=(None, 30))
        L.pack()

        
        L = Label(MGUI, text='รหัสสินค้า', font=(None, 30))
        L.pack(pady=10)

        
        E2 = ttk.Entry(MGUI, textvariable=self.v_productid, font=(None, 20))
        E2.pack(pady=10)

        L = Label(MGUI, text='ชื่อสินค้า', font=(None, 30))
        L.pack(pady=10)

        
        E3 = ttk.Entry(MGUI, textvariable=self.v_title, font=(None, 20))
        E3.pack(pady=10)

        L = Label(MGUI, text='ราคา', font=(None, 30))
        L.pack(pady=10)

        
        E4 = ttk.Entry(MGUI, textvariable=self.v_price, font=(None, 20))
        E4.pack(pady=10)

        L = Label(MGUI, textvariable=self.v_imgpath).pack()

        Bselect = ttk.Button(MGUI, text='เลือกรูปสินค้า (50 x 50 px)', command=self.selectFile)
        Bselect.pack(pady=10)

        Bsave = ttk.Button(MGUI, text='บันทึก', command=self.saveproduct)
        Bsave.pack(pady=10, ipadx=20, ipady=10)

        MGUI.mainloop()

    def selectFile(self):
        filetypes = (
            ('PNG','*.png'),
            ('All files', '*.*')
        )
        select = filedialog.askopenfilename(title='เลือกไฟล์ภาพ', initialdir='/', filetypes=filetypes)
        self.v_imgpath.set(select)

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