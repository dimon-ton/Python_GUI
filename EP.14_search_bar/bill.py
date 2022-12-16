from reportlab.pdfgen import canvas
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfmetrics
from reportlab.lib.units import mm
from reportlab.pdfbase.pdfmetrics import stringWidth
from datetime import datetime

import win32print
import win32api


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


# table header
c.setFont('F2', 8)
table_header = ['รายการ', 'จำนวน', 'ราคา', 'รวม']

x1, y1, x2, y2 = [5 * mm, 115 * mm, 75 * mm, 115 * mm]

c.line(x1, y1, x2, y2)


c.drawString(10 * mm, 116 * mm, table_header[0])
c.drawString(32 * mm, 116 * mm, table_header[1])
c.drawString(52 * mm, 116 * mm, table_header[2])
c.drawString(68 * mm, 116 * mm, table_header[3])
    

c.setFont('F1', 8)
product = [['ชาร้อน', 1, 50, 50], ['ชามะลิ', 3, 50, 150], ['ชาดำ', 6, 50, 300], ['ชาเขียว', 2, 50, 100],]

for i, pd in enumerate(product):
    c.drawString(10 * mm, (112 - (i*3))*mm, pd[0])
    c.drawRightString(35 * mm, (112 - (i*3))*mm, str(pd[1]))
    c.drawRightString(55 * mm, (112 - (i*3))*mm, str(pd[2]))
    c.drawRightString(70 * mm, (112 - (i*3))*mm, str(pd[3]))



c.showPage()
c.save()

# print
# current_printer = win32print.GetDefaultPrinter()
# win32api.ShellExecute(0, 'print', 'bill.pdf', None, '.', 0)
# win32print.SetDefaultPrinter(current_printer)


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


