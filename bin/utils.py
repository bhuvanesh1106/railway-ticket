import mysql.connector


def connect_db():
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="railwayticket"
    )

    return mydb


def insert_data( uid, name, mail_id, number, address):
    mydb = connect_db()
    mycursor=mydb.cursor()

    sql = "INSERT INTO details (uid, name, emailid, number, address) VALUES (%s,%s, %s,%s,%s)"
    val = (uid, name, mail_id, number, address)
    mycursor.execute(sql, val)

    mydb.commit()

    print(mycursor.rowcount, "record inserted.")


def fetch_data():
    mydb = connect_db()
    cursor=mydb.cursor()
    cursor.execute("SELECT * FROM details;")
    return cursor.fetchall()
