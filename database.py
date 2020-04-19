import sqlite3
import os

# this code will be used to store suscribers, retrieve suscribers when sending emails
def createDB():

    if not os.path.exists('suscribers.db'):
        conn = sqlite3.connect("suscribers.db")
        c = conn.cursor()
        c.execute("""CREATE TABLE suscribers(
                    email text,
                    name text) """)
        conn.commit()
        conn.close()

createDB()
def addData():
    import re
    correct = False
    regex = '^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$'

    email = input("enter email address: ").lower()

    while not correct:
        if (re.search(regex, email)):
            correct = True
        else:
            os.system('cls')
            print("Invalid email, try again!")
            email = input("enter email address: ")

    name = input("enter name: ").lower()
    while len(name) == 0:
        os.system('cls')
        print("Name is empty, try again")

        name = input("enter name: ")


    conn = sqlite3.connect("suscribers.db")
    c = conn.cursor()

    c.execute("SELECT email FROM suscribers WHERE email = :email", {'email': email})
    val = c.fetchone()

    if val == None and correct == True:
        c.execute("INSERT INTO suscribers VALUES (:email,:name)", {'email': email, 'name': name})
        print("New suscriber has been added to the database!")
    else:

       os.system('cls')
       print("email already exists, try again")
       addData()



    conn.commit()
    conn.close()

def deleteData():

    print("**************************************")
    email = input("input the E-mail address of the suscriber you would like to delete : ").lower()

    conn = sqlite3.connect("suscribers.db")
    c = conn.cursor()

    c.execute("SELECT email FROM suscribers WHERE email = :email", {'email': email})
    val = c.fetchone()
    if val == None:
        print("email does not exist, try again")
        deleteData()
        print("")

    else:
        c.execute("DELETE FROM suscribers WHERE email = :email", {'email':email})

        conn.commit()
        conn.close()
        print(email, "has been deleted from the database")
        print("")
        print("")

def getData():
    conn = sqlite3.connect("suscribers.db")
    c = conn.cursor()

    c.execute("SELECT * FROM suscribers")
    data = c.fetchall()
    for x in data:
        print("E-mail:",x[0],"|","Name:",x[1])

    conn.commit()
    conn.close()


