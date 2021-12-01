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

mycursor.execute("CREATE TABLE Student (name varchar(50), department varchar(50), roll_no int PRIMARY KEY, sgpa int )")
mycursor.execute("INSERT INTO Student values ('Anuj', 'CS', 24, 4)")
mycursor.execute("INSERT INTO Student values ('Shrujan', 'CS', 25, 7)")
mycursor.execute("INSERT INTO Student values ('Sagar', 'ME', 26, 7)")
mycursor.execute("INSERT INTO Student values ('Harsh', 'IT', 27, 6)")
mydb.commit()

