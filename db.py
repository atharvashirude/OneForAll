import mysql.connector
import dashboard
from dashboard import DashboardWindow
from mysql.connector import Error
from mysql.connector import errorcode

con = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="toor",
    database="test"
)

cursor = con.cursor()

#make a function to access the db

def logindata(val):
    try:
        connect = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="toor",
            database="test"
        )

        cursor = connect.cursor()

        qwery = """create table if not exists `login` (
                `loginid` INT AUTO_INCREMENT,
                `name` CHAR(45) NOT NULL,
                `email` VARCHAR(45) NOT NULL,
                `username` VARCHAR(45) NOT NULL,
                `password` VARCHAR(45) NOT NULL,
                PRIMARY KEY (`loginid`))
                """

        qwery2 ="Insert into login(name,username,email,password) VALUES (%s, %s, %s, %s)"
        print(val)
        cursor.execute(qwery)
        cursor.execute(qwery2, val)
        print("registered")
    except mysql.connector.Error as error:

        print("Failed to Register " + str(error))

        return False

def user_login(tup):
    try:
        print(tup)
        cursor.execute("SELECT * FROM `login` WHERE `username`=%s AND `password`=%s", tup)
        lol = cursor.fetchall()
        print(lol)

        cred = (lol[0][2],lol[0][4])


        print(cred)
        return cred


    except mysql.connector.Error as error:

        print("Failed to login " + str(error))

        return False

def addata(val):
    try:
        connect = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="toor",
            database="test"
        )

        cursor = connect.cursor()
        '''
        qwery = """create table if not exists data(
          `id` int NOT NULL AUTO_INCREMENT,
          `naame` varchar(45) NOT NULL,
          `username` varchar(90)  DEFAULT NULL,
          `email` varchar(45) NOT NULL,
          `website` varchar(45) NOT NULL,
          `pasword` varchar(45) NULL,
          `url` varchar(45) DEFAULT NULL,
          `loginid` int NOT NULL,
          PRIMARY KEY (`id`),
          FOREIGN KEY (`loginid`) REFERENCES `login` (`loginid`) 
        ) """
        '''
        qwery = """create table if not exists data(
                  `id` int NOT NULL AUTO_INCREMENT,
                  `naame` varchar(45) NOT NULL,
                  `username` varchar(90)  DEFAULT NULL,
                  `email` varchar(45) NOT NULL,
                  `website` varchar(45) NOT NULL,
                  `pasword` varchar(110) NULL,
                  `url` varchar(45) DEFAULT NULL,
                  PRIMARY KEY (`id`)) """
        
        cursor.execute(qwery)

        #qwery = "INSERT INTO articles( article_name, article_content, category_id, img, url ) VALUES( ?, ?, ( SELECT category_id FROM categories WHERE categories.category_id = ? ), ?, ?)"
        print("Table created")
        print(val)

        cursor.execute("Insert into data(naame,website,username,email,pasword,url) VALUES (%s, %s, %s, %s, %s, %s)", val)
        #cursor.execute("Insert into cpass(naame,website,username,email,pasword) VALUES ('a','a','a','a','a')")

        print("exe")
        connect.commit()
        print("coolio")
        #qwerty = cursor.execute(qwery)
        #print(qwerty)
        return cursor.fetchone()

    except mysql.connector.Error as error:
        print("Failed to insert " + str(error))
        return False

def update(val):
    try:
        connect = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="toor",
            database="test"
        )

        cursor = connect.cursor()

        print(val)

        cursor.execute("Update data set naame= %s, website=%s, username=%s, email=%s, pasword=%s, url=%s where id=%s", val)


        print("exe")
        connect.commit()
        print("coolio")
        #qwerty = cursor.execute(qwery)
        #print(qwerty)
        return cursor.fetchone()

    except mysql.connector.Error as error:
        print("Failed to insert " + str(error))
        return False

def delete(val):
    try:
        connect = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="toor",
            database="test"
        )

        cursor = connect.cursor()
        #val ="'"+val+"'"
        print(val)

        '''
        cursor.execute("select id from data where naame = "+val)
        idd = cursor.fetchall()
        
        data = str(idd[0][0])
        print(data)
        '''
        cursor.execute("Delete from data where id="+val)


        print("exe")
        connect.commit()
        print("coolio")
        #qwerty = cursor.execute(qwery)
        #print(qwerty)
        return cursor.fetchone()

    except mysql.connector.Error as error:
        print("Failed to delete " + str(error))
        return False



#showdata()
