import mysql.connector
import sys

class DBhelper:
    def __init__(self):
        try:
            self.conn = mysql.connector.connect(host="localhost", user="root", password="", database="hit_db_demo")
            self.mycursor = self.conn.cursor()
        except mysql.connector.Error as err:
            print(f"Error: {err}")
            sys.exit()
        else:
            print("Connected to Database")

    def register(self,name,email,password):
        try:
            self.mycursor.execute("""
            INSERT INTO `users` (`id`, `name`, `email`, `password`) VALUES (NULL,'{}','{}','{}');
            """.format(name,email,password))
            self.conn.commit()
        except:
            return -1
        else:
            return 1

    def search(self,email,password):
        self.mycursor.execute("""
        select * from users where email like '{}' and password like '{}'""".format(email,password))

        data = self.mycursor.fetchall()
        return data