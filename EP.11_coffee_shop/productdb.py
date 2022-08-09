import sqlite3

conn = sqlite3.connect('EP.11_coffee_shop/productdb.sqlite3') # สร้างไฟล์ฐานข้อมูล
c = conn.cursor()

# สร้างตารางจัดเก็บ
c.execute("""CREATE TABLE IF NOT EXISTS product(
                ID INTEGER PRIMARY KEY AUTOINCREMENT,
                productid TEXT,
                title TEXT,
                price REAL,
                image TEXT)""")


def Insert_product(productid, title, price, image):
    with conn:
        command = 'INSERT INTO product VALUES (?,?,?,?,?)' # SQL
        c.execute(command, (None,productid, title, price, image))
    conn.commit() # save database
    print('saved')


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

if __name__ == '__main__':
    # ฟังก์ชั้นเอาไว้เช็คว่าตอนนี้ไฟล์ที่กำลังรันนี้อยู่ในไฟล์จริงหรือไม่ (รันเฉพาะฟังก์ชั่นนี้)
    View_product_table_icon()



