import sqlite3

conn = sqlite3.connect('EP.9_basic_sql/basicdb.sqlite3') # สร้างไฟล์ฐานข้อมูล
c = conn.cursor()

# สร้างตารางจัดเก็บ
c.execute("""CREATE TABLE IF NOT EXISTS member(
                ID INTEGER PRIMARY KEY AUTOINCREMENT,
                membercode TEXT,
                fullname TEXT,
                tel TEXT,
                usertype TEXT,
                points INTEGER)""")


def Insert_member(membercode, fullname, tel, usertype, points):
    with conn:
        command = 'INSERT INTO member VALUES (?,?,?,?,?,?)' # SQL
        c.execute(command, (None, membercode, fullname, tel, usertype, points))
    conn.commit() # save database
    print('saved')

#Insert_member('MB-102', 'สมหญิง ดีมาก', '0887234359', 'general', 150)

def View_member():
    with conn:
        command = 'SELECT * FROM member'
        c.execute(command)
        result = c.fetchall()
    print(result)
    return result

def Update_member(ID, field, newvalue):
    with conn:
        command = 'UPDATE member SET {} = (?) WHERE ID = (?)'.format(field)
        c.execute(command, ([newvalue, ID]))
    conn.commit()
    print('updated')

def Delete_member(ID):
    with conn:
        command = 'DELETE FROM member WHERE ID = (?)'
        c.execute(command, ([ID]))
    conn.commit()
    print('deleted')

Insert_member('MB-1003', 'นายพิมล ตุ่นกระโทก', '0887263735', 'vip', 300)
View_member()
