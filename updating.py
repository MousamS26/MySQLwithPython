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
mycursor.execute("UPDATE Student SET department = 'ENTC' where roll_no = 24")
mydb.commit()
mycursor.execute("SELECT * FROM Student WHERE roll_no = 24")
for x in mycursor:
    print(x)