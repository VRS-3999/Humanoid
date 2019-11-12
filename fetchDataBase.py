import mysql.connector
mydb = mysql.connector.connect(
    host = "localhost",
    user = "invicta",
    passwd = "DRAGONBALL",
    database = "names",
    port = "3300"
    )
mycursor = mydb.cursor()
sql = "select name from NAMES where ids=4" 
mycursor.execute(sql)
a = mycursor.fetchone()
mydb.commit()
print(a[0])
