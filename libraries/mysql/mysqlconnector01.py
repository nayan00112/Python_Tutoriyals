import mysql.connector

# create connection

myconn = mysql.connector.connect(host="localhost", passwd="nayan@2003", user="root") 

print(myconn.is_connected())
# True


