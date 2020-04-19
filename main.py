
from Email import SendEmail
from database import*
import sys

def SendNewsLetters():
    conn = sqlite3.connect("suscribers.db")
    c = conn.cursor()

    c.execute("SELECT * FROM suscribers")
    data = c.fetchall()
    for email in data:
        SendEmail(email[0],email[1])


def Suscribers():
    print("************************************")
    print("             SUSCRIBERS")
    print("************************************")
    print("1. see all the suscribers' details")
    print("2. add new suscribers")
    print("3. delete suscribers")
    print("4.Menu")

    choice = input("Enter your choice : ")
    if choice == "1":
        getData()
        print("")
        y = input("enter B to go back ").upper()
        while y != "B":
            y = input("invalid character, try again!  " ).upper()
        Suscribers()


    elif choice == "2":
        addData()
        print("")
        y = input("enter B to go back or A to add another suscriber ").upper()
        flag = True
        while flag:
            if y == "B":
                Suscribers()
                flag = False
            elif y == "A":
                print("")
                addData()
                y = input("enter B to go back or A to add another suscriber ").upper()
            else:
                y = input("invalid character, try again!  ").upper()


    elif choice == "3":
        print("")
        getData()
        deleteData()
        print("")
        y = input("enter B to go back or D to delete another suscriber ").upper()
        flag = True
        while flag:
            if y == "B":
                Suscribers()
                flag = False
            elif y == "D":
                print("")
                getData()
                deleteData()
                y = input("enter B to go back or D to delete another suscriber ").upper()
            else:
                y = input("invalid character, try again!  ").upper()



    elif choice == "4":
        menu()

    else:
        print("choice not found, try again")
        Suscribers()

def clear():
    os.system('cls')

def menu():
    print("************************************")
    print("             WELCOME")
    print("************************************")
    print("Choose from the following options :")
    print("Enter '1' To send Newsletters to ALL the suscribers")
    print("Enter '2' for suscribers options")
    print("Enter '3' to exit")

    choice = input("Enter your choice : ")
    if choice == "1" :
        SendNewsLetters()
        print("")
        print("")
        input("Press enter to go back ").upper()
        menu()

    elif choice == "2" :
        Suscribers()
        print("")
        print("")
    elif choice == "3":
        sys.exit()
    else:
        print("choice not found, try again")
        menu()


menu()
