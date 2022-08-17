
from asyncio.windows_events import NULL
from datetime import datetime
import mysql.connector
import mysql_config as c
import time
import os


def login(cursor):
    print("enter your email")
    email=input()
    cursor.execute(f"SELECT email FROM accounts WHERE email='{email}'")
    test1=cursor.fetchone()
    if test1==None:
        print("email does not exist")
    else:
        print("enter your password")
        password=input()
        cursor.execute(f"SELECT password FROM accounts WHERE password='{password}'")
        test2=cursor.fetchone()
        if test2==None:
            print("invalid password")
        else:
            print("You have logged in")
            
            return email
def createaccount(cursor):
    print("enter your email")
    email=input()
    print("enter your password")
    password=input()
    values1=[password,email]
    cursor.execute("INSERT INTO accounts (password, email) VALUES(%s,%s)",values1)
    cnx.commit()
    print("Account created")
def makeAnOrder(cursor,email,productid,amount):
    
    if(productid=="1"):
        d=datetime.today()
        values1=["Yu-Gi-Oh! Cards",email,amount,d]
        cursor.execute("INSERT INTO ordersHist (product, email,amount,date) VALUES(%s,%s,%s,%s)",values1)
        cnx.commit()
        print("Order has been Placed!")

    elif(productid=="2"):
        d=datetime.today()
        values1=["Magic the Gathering Cards",email,amount,d]
        cursor.execute("INSERT INTO ordersHist (product, email,amount,date) VALUES(%s,%s,%s,%s)",values1)
        cnx.commit()
        print("Order has been Placed!")

    elif(productid=="3"):
        d=datetime.today()
        values1=["Pokemon Cards",email,amount,d]
        cursor.execute("INSERT INTO ordersHist (product, email,amount,date) VALUES(%s,%s,%s,%s)",values1)
        cnx.commit()
        print("Order has been Placed!")

    else:
        print("invalid product id or we are not taking any more orders of that product SORRY!")
def viewLatestSets(cursor):
    query = "SELECT * FROM latestSets"
    cursor.execute(query)
    for record in cursor:
        print(record)
def viewOrders(email):
    query = f"SELECT * FROM ordersHist WHERE email='{email}'"
    print("Here are your orders\nProduct -------------- Email -------------- Amount -------------- Date and time Purchased")

    cursor.execute(query)
    for record in cursor:
        print(record)
    time.sleep(3)
def updateSet(oldsetname,newsetname):
    query = f"Update latestSets SET product='{newsetname}' WHERE product='{oldsetname}'"
    cursor.execute(query)
    cnx.commit()
    print("Set has been updated!")
def deleteSet(setToDelete):
    query = f"DELETE FROM latestSets WHERE product='{setToDelete}'"
    cursor.execute(query)
    cnx.commit()
    print("Deletion complete!")
def adminlogin():
    print("enter your admin credentials")
    admin=input()
    print("enter your password")
    password=input()
    if(admin=="admin" and password=="password"):
        print("Welcome admin!")
        return True
    else:
        return False
def clear_console():
    os.system('cls')




clear_console()
print("Connectecting to the database")
time.sleep(1)
print(".")
time.sleep(1)
print(".")
time.sleep(1)
print(".")
time.sleep(1)
print("Connected")
time.sleep(2)
cnx = mysql.connector.connect(user=c.user, password=c.password, host=c.host, database="pythonlogin")
cursor = cnx.cursor()







importemail=NULL
while True:
    clear_console()
    print("welcome to my shop!")
    print("please choose an option \n1.login\n2.create an account\n3.purchase product\n4.look at your order history\n5.Admin login\n6.Leave")
    choice=int(input())

    
    if choice==1:
        importemail=login(cursor)
    elif choice==2:
        createaccount(cursor)
    elif choice==5:
        isAdmin=adminlogin()
        while isAdmin:
            print("please choose an option \n1.Update a set\n2.Delete a set\n3.Leave")
            adminChoice=int(input())
            if adminChoice==1:
                print("Please input the old set name")
                oldsetName=input()
                print("Please input the new set name")
                newsetName=input()
                updateSet(oldsetName,newsetName)
            elif adminChoice==2:
                print("Please input the set name for deletion")
                delSet=input()
                deleteSet(delSet)
            else:
                print("Admin logging off")
                break
    elif choice==6:
        print("Goodbye!")
        break
    elif importemail==NULL:
        print("Please login first...")
    elif choice==3:
        print("Choose a product by inputting the product ID")
        viewLatestSets(cursor)
        inpID=input()
        print("How many cases would you like to buy?")
        inpAmount=input()
        makeAnOrder(cursor,importemail,inpID,inpAmount)
    elif choice==4:
        viewOrders(importemail)
    time.sleep(3)

















