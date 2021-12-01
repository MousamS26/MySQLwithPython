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
mycursor.execute("SELECT * FROM Student WHERE department = 'CS'")
for x in mycursor:
    print(x)
