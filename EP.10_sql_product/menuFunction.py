from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from productdb import *
class AddMember:
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