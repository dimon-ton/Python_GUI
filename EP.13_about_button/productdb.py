import sqlite3

conn = sqlite3.connect('EP.13_about_button/productdb.sqlite3') # สร้างไฟล์ฐานข้อมูล
c = conn.cursor()

# สร้างตารางจัดเก็บ
c.execute("""CREATE TABLE IF NOT EXISTS product(
                ID INTEGER PRIMARY KEY AUTOINCREMENT,
                productid TEXT,
                title TEXT,
                price REAL,
                image TEXT)""")

c.execute("""CREATE TABLE IF NOT EXISTS product_status(
                ID INTEGER PRIMARY KEY AUTOINCREMENT,
                product_id INTEGER,
                status TEXT)""")

def insert_product_status(pid, status):
    check = View_product_status(pid)
    if check == None:
        with conn:
            command = 'INSERT INTO product_status VALUES(?,?,?)'
            c.execute(command,(None,pid,status))
        conn.commit()
        print('status saved')
    else:
        print('pid exist')
        print(check)
        update_product_status(pid, status)

def View_product_status(pid):
    with conn:
        command = 'SELECT * FROM product_status WHERE product_id = (?)'
        c.execute(command, ([pid]))
        result = c.fetchone()
    print(result)
    return result

def update_product_status(pid, status):
    with conn:
        command = 'UPDATE product_status SET status = (?) WHERE product_id = (?)'
        c.execute(command, ([status, pid]))
    conn.commit()
    print('updated', (pid, status))


def Insert_product(productid, title, price, image):
    with conn:
        command = 'INSERT INTO product VALUES (?,?,?,?,?)' # SQL
        c.execute(command, (None,productid, title, price, image))
    conn.commit() # save database
    print('saved')
    # add status after insert product
    find = View_product_single(productid)
    insert_product_status(find[0], '')


def View_product():
    with conn:
        command = 'SELECT * FROM product'
        c.execute(command)
        result = c.fetchall()
    print(result)
    return result

def View_product_table_icon():
    with conn:
        command = 'SELECT ID, productid, title FROM product'
        c.execute(command)
        result = c.fetchall()
    print(result)
    return result

def View_product_single(productid):
    with conn:
        command = 'SELECT * FROM product WHERE productid = (?)'
        c.execute(command, ([productid]))
        result = c.fetchone()
    print(result)
    return result


'''
product = {'latte':{'name':'ลาเต้','price':30},
            'cappuccino':{'name':'คาปูชิโน่','price':35},
            'expresso':{'name':'เอสเปรสโซ่','price':40},
            'icegreentea':{'name':'ชาเขียวเย็น','price':40},
            'cocoa':{'name':'โกโก้','price':50},
            'icetea':{'name':'ชาเย็น','price':40},
            'hottea':{'name':'ชาร้อน','price':35}}
'''

def product_icon_list():
    with conn:
        command = 'SELECT * FROM product'
        c.execute(command)
        product = c.fetchall()

    with conn:
        command = "SELECT * FROM product_status WHERE status = 'show'"
        c.execute(command)
        status = c.fetchall()

    result = []

    for s in status:
        for p in product:
            if s[1] == p[0]:
                # print(p, s[-1])
                result.append(p)

    result_dict = {}
    # print(result)
    for r in result:
        result_dict[r[0]] = {'id':r[0], 'productid':r[1], 'name':r[2], 'price':r[3], 'icon':r[4]}
    
    return result_dict

if __name__ == '__main__':
    pass
    # ฟังก์ชั้นเอาไว้เช็คว่าตอนนี้ไฟล์ที่กำลังรันนี้อยู่ในไฟล์จริงหรือไม่ (รันเฉพาะฟังก์ชั่นนี้)
    # View_product_table_icon()
    # insert_product_status(1, 'show')
    # View_product_status(1)
    x = product_icon_list()
    print(x)



