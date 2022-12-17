from reportlab.pdfgen import canvas
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfmetrics
from reportlab.lib.units import mm
from reportlab.pdfbase.pdfmetrics import stringWidth
from datetime import datetime

import win32print
import win32api
import subprocess


def printBill(product=[['ชาร้อน', 50, 1, 50], ['ชามะลิ', 50, 3, 150]], printer=False, openfile=False, **kwargs):


    # set font size
    pdfmetrics.registerFont(TTFont('F1', 'THSARABUNNEW.ttf'))
    pdfmetrics.registerFont(TTFont('F2', 'THSARABUNNEW BOLD.ttf'))

    c = canvas.Canvas('bill.pdf')
    c.setPageSize((80 * mm, 150 * mm))

    # header
    c.setFont('F2', 10)
    c.drawCentredString(40 * mm, 140 * mm, 'ใบเสร็จรับเงิน/ใบกำกับภาษี')

    c.setFont('F1', 15)
    c.drawCentredString(40 * mm, 135 * mm, 'ร้านลุงโภชนาการ')

    company = ['ที่อยู่: 123 พหลโยธิน สามเสนใน พญาไท กทม.',
                'โทร. 02-123-4567, 081 238 5678',
                'สาขา: 1999 TAX ID: 107778888',
                'Line: @unclefood']




    c.setFont('F1', 8)
    for i, com in enumerate(company, start=1):
        c.drawCentredString(40 * mm, (132 - (i*3))*mm, com)

    c.setFont('F2', 5)
    c.drawString(8 * mm, 116 * mm, 'TAX INVOICE: {}'.format(kwargs['transaction']))
    c.drawRightString(75 * mm, 116 * mm, 'TIME STAMP: {}'.format(kwargs['timestamp']))
    # table header
    c.setFont('F2', 8)
    table_header = ['รายการ', 'ราคา', 'จำนวน', 'รวม']




    x1, y1, x2, y2 = [5 * mm, 114 * mm, 75 * mm, 114 * mm]

    c.line(x1, y1, x2, y2)


    c.drawString(10 * mm, 111.5 * mm, table_header[0])
    c.drawString(32 * mm, 111.5 * mm, table_header[1])
    c.drawString(52 * mm, 111.5 * mm, table_header[2])
    c.drawString(67 * mm, 111.5 * mm, table_header[3])


    x11, y11, x21, y21 = [5 * mm, 110 * mm, 75 * mm, 110 * mm]

    c.line(x11, y11, x21, y21)
        

    c.setFont('F1', 8)
    # product = [['ชาร้อน', 50, 1, 50], ['ชามะลิ', 50, 3, 150], ['ชาดำ', 50, 6, 300], ['ชาเขียว', 50, 2, 100],]

    next_reference = 0

    for i, pd in enumerate(product):
        c.drawString(10 * mm, (107 - (i*3))*mm, pd[0])
        c.drawRightString(35 * mm, (107 - (i*3))*mm, str(pd[1]))
        c.drawRightString(55 * mm, (107 - (i*3))*mm, str(pd[2]))
        c.drawRightString(70 * mm, (107 - (i*3))*mm, str(pd[3]))
        next_reference = 107 - (i*3) -5


    quan = sum([p[2] for p in product])
    total = sum([p[3] for p in product])
    vat = total * (7/100)
    nettotal = total * (100/107)

    footer = {'Quan': quan, 'Total':total, 'VAT 7%':vat, 'Net Total':nettotal}

    c.setFont('F2', 8)

    for e, (k, v) in enumerate(footer.items(), start=1):
        c.drawRightString(70 * mm, (next_reference - (5*e) + 2) * mm , '------------------------------------------------')
        c.drawRightString(70 * mm, (next_reference - (5*e)) * mm , '{}: {:,.2f}'.format(k, v))
        next_reference2 = next_reference - (4*e)

    c.drawCentredString(40 * mm, (35) * mm, '---------------------------------------------------------------------------')
    c.drawCentredString(40 * mm, (25) * mm, 'Join Our Store: www.our-store.com')
    c.drawCentredString(40 * mm, (15) * mm, '---------------------------------------------------------------------------')
    c.setFont('F1', 12)
    c.drawCentredString(40 * mm, 8 * mm, 'Thank You')


    c.showPage()
    c.save()

    # print
    if printer:
        current_printer = win32print.GetDefaultPrinter()
        win32api.ShellExecute(0, 'print', 'bill.pdf', None, '.', 0)
        win32print.SetDefaultPrinter(current_printer)


    # open pdf
    if openfile:
        subprocess.Popen('bill.pdf', shell=True)



if __name__ == '__main__':
    product = [['ชาร้อน', 50, 1, 50], ['ชามะลิ', 50, 3, 150], ['ชาดำ', 50, 6, 300], ['ชาเขียว', 50, 2, 100]]
    timestamp = datetime.now().strftime('%Y-%m-%d %H-%M')
    transaction = '65326515485'

    printBill(product, False, True, transaction=transaction, timestamp=timestamp)




# example
# # text
'''
c.setFont('F1', 10)
c.drawString(10 * mm, 140 * mm, 'ที่ใบเสร็จรับเงินเริ่ม')
c.drawString(10 * mm, 30 * mm, 'Hello World')
c.drawCentredString(40 * mm, 40 * mm, 'อักษรตรงกลาง')

c.setFont('F2', 10)
c.drawRightString(60 * mm, 30 * mm, 'วัชรเกียรติ์')
c.drawRightString(60 * mm, 20 * mm, 'โรงเรียนวัดคลองชากพง')
c.drawRightString(60 * mm, 10 * mm, 'เริ่มงานวันที่ 18 มิถุนายน พ.ศ. 2565')

# drawing line
# x1, y1, x2, y2 = [10 * mm, 100 * mm, 70 * mm, 100 * mm]

# ml = [[10 * mm, 100 * mm, 70 * mm, 100 * mm], [10 * mm, 120 * mm, 70 * mm, 120 * mm]]

# # c.line(x1, y1, x2, y2)

# c.lines(ml)
'''


