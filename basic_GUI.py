'''
    นี่คือโปรแกรมแรกของเรา
'''
print('เริ่มโปรแกรม')

from tkinter import *
from tkinter import ttk, messagebox

GUI = Tk()

#-----------------------------------------------------------------
GUI.title('โปรแกรมคำนวณเลข') #ชื่อโปรแกรม
GUI.geometry('500x300') #ปรับขนาดโปรแกรม

def Show():
    messagebox.showinfo('Show Box','สวัสดีจ้า ได้แล้ว!!')

B1 = ttk.Button(GUI,text="คลิกปุ่มนี้",command=Show)
B1.pack(ipadx=30,ipady=30,pady=50)
#-----------------------------------------------------------------

GUI.mainloop()