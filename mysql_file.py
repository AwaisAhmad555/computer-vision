import mysql.connector

conn = mysql.connector.connect(
         user='root',
         password='',
         host='localhost',
         port='3307',
         database='iphone_project')


mycursor = conn.cursor()

insert_query = "INSERT INTO user (username,email,password) VALUES(%s, %s, %s)"
values = ("madman555","madman2244@abc.com","madman555")

mycursor.execute(insert_query,values)

conn.commit()

print("1 record inserted, ID:", mycursor.lastrowid)

mycursor.execute("SELECT * FROM user")

myresult = mycursor.fetchall()

for x in myresult:
  print(x)

conn.close()