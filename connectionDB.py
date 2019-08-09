import mysql.connector

#sudo mysql -u root -p
"""
mydb = mysql.connector.connect(host="localhost",user="root",password="test" , database="STREAMS" )

mycursor=mydb.cursor()

mycursor.execute("show tables")

for i in mycursor:
    print(i)

"""


class Database:
    @staticmethod
    def connect_dbs():
        econ = mysql.connector.connect(host="localhost",user="root",password="test" , database="STREAMS" )
        return econ
