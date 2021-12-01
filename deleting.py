import mysql.connector
#CREATING AND INSERTING DATA
mydb = mysql.connector.connect(
    host='localhost',
    username= 'root',
    password = '12345',
    port = '3306',
    database = 'dbmsl'
)
mycursor = mydb.cursor()
mycursor.execute("DELETE FROM Student WHERE roll_no = 27")
mydb.commit()
mycursor.execute("SELECT * FROM Student")
for x in mycursor:
    print(x)