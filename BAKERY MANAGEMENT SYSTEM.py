
                          #BAKERY MANAGEMENT SYSTEM

import mysql.connector

val = mysql.connector.connect(host = 'localhost',user = 'root', password = 'root')
cur = val.cursor()
cur.execute("create database if not exists menu")
cur.execute("use menu")
cur.execute("create table if not exists menu(Sno int, Products varchar(30),cost int)")
sql = "select*from menu"
cur.execute(sql)
res = cur.fetchall()
if res == []:
    cur.execute("insert into menu values(1,'CAKE',           100)")
    cur.execute("insert into menu values(2,'CHOCLATE PASTRY',25)")
    cur.execute("insert into menu values(3,'BRWONY',         35)")
    cur.execute("insert into menu values(4,'COLESLOE CHEESE SANDWICH',35)")
    cur.execute("insert into menu values(5,'CHOCLATE MUPHIN',15)")
    cur.execute("insert into menu values(6,'MINI PIZZA',     40)")
    cur.execute("insert into menu values(7,'CREAM ROLL',     40)")
    cur.execute("insert into menu values(8,'MASALA CROSSIANT',45)")
    val.commit()
cur.execute('create table if not exists flavors(Sno int, Flavours varchar(30))')
sql1 = "select*from flavors"
cur.execute(sql1)
res1 = cur.fetchall()
if res1 == []:
    cur.execute("insert into flavors values(1,'VANILLA')")
    cur.execute("insert into flavors values(2,'CHOCLATE')")
    cur.execute("insert into flavors values(3,'BUTTER SCHOTCH')")
    cur.execute("insert into flavors values(4,'STRAWBERRY')")
    cur.execute("insert into flavors values(5,'RUM RAISIN')")
    val.commit()
cur.execute("create table if not exists workers(Sno int, Name varchar(10), Salary int)")
sql2 = "select*from workers"
cur.execute(sql2)
res2 = cur.fetchall()
if res2 == []:
    cur.execute("insert into workers values(1,'RAJU',9000)")
    cur.execute("insert into workers values(2,'SOMESH',9000)")
    cur.execute("insert into workers values(3,'BABBAN',8500)")
    val.commit()

from datetime import datetime
print("______________________________CS PRJECT(083)____________________________")
print("________________________________________________________________________")
print("____________________@@@@@@@@@@@@WELCOME TO @@@@@@@@@@@@_____________________")
print("____________________@@@@@@@@@@@BAKERY@@@@@@@@@@@@_______________________")
print("____________________@@@@@@@MANAGEMENT SYSTEM@@@@@@@_____________________")
print("________________@@@@@@@@MADE BY:- HIMANSHU BISWAS@@@@@@@@@________________")

ch = ''
while ch!='n' or ch != 'N':
    print("\nPLEASE CHOOSE\n1.) FOR ADMIN\n2.) FOR CUSTMOR\n3.)EXIT")
    choice = int(input("ENTER YOUR CHOICE: "))
    if choice == 1:
        admin = input("USERNAME: ")
        passwrd = int(input("ENTER PASSWORD: "))
        if passwrd == 9957 and admin == 'HIMANSHU' or admin == 'ANANAD':
            print("************HELLO SIR, YOU'VE LOGGED SUCCESSFULLY AS ADMIN************")
            print("______________________________________________________________________")
            print("PRESS 1 TO ADD ITEM IN THE SHOP.....")
            print("PRESS 2 TO SEE ITEMS IN THE SHOP....")
            print("PRESS 3 TO UPDATE COST OF ANY ITEM....")
            print("PRESS 4 TO ADD VARITIES OF CAKE IN THE SHOP....")
            print("PRESS 5 TO ADD WORKERS IN THE SHOP....")
            print("PRESS 6 TO SEE WORKERS....")
            print("PRESS 7 TO REMOVE ANY FLAVOURS OF CAKE.....")
            C = int(input("ENTER YOUR CHOICE: "))
            if C == 1:
                def add():
                    sno = int(input("ENTER Sno.: "))
                    product1 = input("ENTER PRODUCT NAME: ")
                    cost = int(input("ENTER THE COST: "))
                    d1 = (sno,product1,cost)
                    s1 = "insert into menu values(%s,%s,%s)"
                    cur.execute(s1,d1)
                    val.commit()
                    print("__________@@@@ITEM ADDED SUCCESFULLY@@@@________")
                add()
            elif C == 2:
                def items():
                    print("ITEMS IN THE SHOP ARE:- ")
                    sql3 = 'select*from menu'
                    cur.execute(sql3)
                    res3 = cur.fetchall()
                    t = (['serial_no','products','cost'])
                    for serial_no,products,cost in res3:
                        print(serial_no,"\t\t",products,"\t\t",cost)
                items()
            elif C == 3:
                def money():
                    sno1 = int(input("ENTER THE Sno OF PRODUCTS: "))
                    n_cost = int(input("ENTER THE RUPEES TO BE ADDED: "))
                    cur.execute("update items set cost = cost+"+n_cost+"where Sno ="+Sno+":")
                    val.commit()
                    print("TABLE AFTER UPADTATION: ")
                    sql4 = "select*from menu"
                    cur.execute(sql4)
                    res4 = cur.fetchall()
                    t = (['Sno','Products','cost'])
                    for sno,Products,cost in res4:
                        print(sno,"\t\t",Products,"\t\t",cost)
                money()
            elif C == 4:
                def variety():
                    sno = int(input("ENTER SNO.: "))
                    varities = input("ENTER VARIETY: ")
                    d2 = (sno,varities)
                    s2 = 'insert into flavors values(%s,%s)'
                    cur.execute(s2,d2)
                    val.commit()
                variety()
            elif C == 5:
                def workeradd():
                    sno = int(input("ENTER SNO.: "))
                    emp = input("ENTER NAME: ")
                    salary = int(input("ENTER SALARY OF WORKER: "))
                    dx = (sno,emp,salary)
                    dy = 'insert into workers values(%s,%s)'
                    cur.execute(dy,dx)
                    val.commit()
                    print("__________////////WOKERS ADDED///////_____________")
                workeradd()
            elif C == 6:
                def workers():
                    print("WOKERS IN THE SHOP:- ")
                    sql5 = 'select*from workers'
                    cur.execute(sql5)
                    res5 = cur.fetchall()
                    t = (['serial_no','name','salary'])
                    for serial_no,name,salary in res5:
                        print(serial_no,"\t\t",name,"\t\t",name)
                workers()
            elif C == 7:
                def remove():
                    sno1 = int(input("ENTER SNO.: "))
                    variety = input("ENTER YOU WANT TO DELETE VARIETY: ")
                    d3 = (sno1,variety)
                    s3 = "delte from flavors where Sno='%s'"
                    cur.execute(s3,d3)
                    val.commit()
                remove()    
            else:
                print("SORRY...........WRONG INPUT........")
        else:
            print("\t\t\t\t\t\t\t***********WRONG PASSWORD************\t\t\t\t\t\t\t")
    elif choice == 2:
        name = input("ENTER YOUR NAME: ")
        phone = int(input("ENTER THE PHONE NUMBER: "))
        print("PRESS 1 TO SEE MENU.....")
        print("PRESS 2 TO ORDER ITEM")
        c = int(input("ENTER YOUR CHOICE: "))
        if c == 1:
            def items():
                
                print("ITEMS IN THE SHOP:- ")
                sql7 = "select*from menu"
                cur.execute(sql7)
                res7 = cur.fetchall()
                t = (['serial_no','products','cost'])
                for serial_no,products,cost in res7:
                    print(serial_no,"\t\t",products,"\t\t",cost)
            items()
        elif c == 2:
            
            print("WHAT DO YOU WANT TO ORDER?")
            sql8 = "select*from menu"
            cur.execute(sql8)
            res8 = cur.fetchall()
            t = (['serial_no','products','cost'])
            for serial_no,products,cost in res8:
                print(serial_no,'\t\t',products,'\t\t',cost)
            sql9 = "select*from menu"
            cur.execute(sql9)
            res9 = cur.fetchall()
            d = int(input("ENTER YOUR SERIAL NUMBER TO BUY: "))
            if d == 1:
                print("WHICH FLAVOUR DO YOU WANT?")
                kl = "select*from flavors"
                cur.execute(kl)
                res10 = cur.fetchall()
                f = (['sno','varities'])
                for sno,varities in res10:
                    print(sno,'\t\t',varities)
                print("CHOOSE WHICH FLAVOUR DO YOU WANT?")
                c1 = int(input("ENTER CHOICE: "))
                if c1 == 1:
                    print("HOW MUCH QUANTITY OF VANILLA CAKE YOU WANT?")
                    qty = int(input("ENTER QUANTITY: "))
                    print("YOU HAVE SUCCESSFULLY ORDERD YOUR CAKE!!!!!!")
                    cur.execute("select*from menu where Products = 'CAKE'" )
                    for i in cur:
                        c2 = i[2]
                        val.commit()
                    print("TOTAL AMOUNT: ",qty*c2)
                    print(".........................................................")
                    print("YOUR BILL")
                    print("_________________________________________________________")
                    print("CUSTMOR'S NAME: ",name)
                    print("PHONE NUMBER: ",phone)
                    print("CAKE TYPE VANILLA")
                    print("NO. OF CAKES",qty)
                    print("_____________********THANK YOU FOR ORDERING*******_____________")
                    print("\t\t\t\t\t\tDATE: ",datetime.now())
                elif c1 == 2:
                    print("HOW MUCH QUANTITY OF CHOCLATE CAKE YOU WANT?")
                    qty = int(input("ENTER QUANTITY: "))
                    print("YOU HAVE SUCCESSFULLY ORDERD YOUR CAKE!!!!!!")
                    cur.execute("select*from menu where Products = 'CAKE'" )
                    for i in cur:
                        c3 = i[2]
                        val.commit()
                    print("TOTAL AMOUNT: ",qty*c3)
                    print(".........................................................")
                    print("YOUR BILL")
                    print("_________________________________________________________")
                    print("CUSTMOR'S NAME: ",name)
                    print("PHONE NUMBER: ",phone)
                    print("CAKE TYPE CHOCLATE")
                    print("NO. OF CAKES",qty)
                    print("_____________********THANK YOU FOR ORDERING*******_____________")
                    print("\t\t\t\t\t\tDATE: ",datetime.now())
                elif c1 == 3:
                    print("HOW MUCH QUANTITY OF BUTTER SCHOTCH CAKE YOU WANT?")
                    qty = int(input("ENTER QUANTITY: "))
                    print("YOU HAVE SUCCESSFULLY ORDERD YOUR CAKE!!!!!!")
                    cur.execute("select*from menu where Products = 'CAKE'" )
                    for i in cur:
                        c4 = i[2]
                        val.commit()
                    print("TOTAL AMOUNT: ",qty*c4)
                    print(".........................................................")
                    print("YOUR BILL")
                    print("_________________________________________________________")
                    print("CUSTMOR'S NAME: ",name)
                    print("PHONE NUMBER: ",phone)
                    print("CAKE TYPE BUTTER SCHOTCH")
                    print("NO. OF CAKES",qty)
                    print("_____________********THANK YOU FOR ORDERING*******_____________")
                    print("\t\t\t\t\t\tDATE: ",datetime.now())
                elif c1 == 4:
                    print("HOW MUCH QUANTITY OF STRAWBERRY CAKE YOU WANT?")
                    qty = int(input("ENTER QUANTITY: "))
                    print("YOU HAVE SUCCESSFULLY ORDERD YOUR CAKE!!!!!!")
                    cur.execute("select*from menu where Products = 'CAKE'" )
                    for i in cur:
                        c5 = i[2]
                        val.commit()
                    print("TOTAL AMOUNT: ",qty*c5)
                    print(".........................................................")
                    print("YOUR BILL")
                    print("_________________________________________________________")
                    print("CUSTMOR'S NAME: ",name)
                    print("PHONE NUMBER: ",phone)
                    print("CAKE TYPE STRAWBERRY")
                    print("NO. OF CAKES",qty)
                    print("_____________********THANK YOU FOR ORDERING*******_____________")
                    print("\t\t\t\t\t\tDATE: ",datetime.now())
                elif c1 == 5:
                    print("HOW MUCH QUANTITY OF RUM RAISIN CAKE YOU WANT?")
                    qty = int(input("ENTER QUANTITY: "))
                    print("YOU HAVE SUCCESSFULLY ORDERD YOUR CAKE!!!!!!")
                    cur.execute("select*from menu where Products = 'CAKE'" )
                    for i in cur:
                        c6 = i[2]
                        val.commit()
                    print("TOTAL AMOUNT: ",qty*c6)
                    print(".........................................................")
                    print("YOUR BILL")
                    print("_________________________________________________________")
                    print("CUSTMOR'S NAME: ",name)
                    print("PHONE NUMBER: ",phone)
                    print("CAKE TYPE RUM RAISIN")
                    print("NO. OF CAKES",qty)
                    print("_____________********THANK YOU FOR ORDERING*******_____________")
                    print("\t\t\t\t\t\tDATE: ",datetime.now())
            elif d == 2:
                 print("HOW MANY MUPHINS DO YOU WANT TO ORDER?")
                 qunty = int(input("ENTER HOW MNAY MUPHINS: "))
                 print("YOU HAVE SUCCESSFULLY ORDERED",qunty,"PIECES OF MUPHINS")
                 cur.execute("select*from menu where Products = 'MUPHINS'")
                 for i in cur:
                     m = i[2]
                     val.commit()
                 print("TOTAL AMOUNT: ",qunty*m)
                 print(".........................................................")
                 print("YOUR BILL")
                 print("_________________________________________________________")
                 print("CUSTMOR'S NAME: ",name)
                 print("PHONE NUMBER: ",phone)
                 print("BRWONIES")
                 print("NO. OF BRWONIES",qunty)
                 print("_____________********THANK YOU FOR ORDERING*******_____________")
                 print("\t\t\t\t\t\tDATE: ",datetime.now()) 
            elif d == 3:
                print("HOW MUCH CHOCLATE PASTRY DO YOU WANT?")
                qtiy =  int(input("ENTER QUANTITY: "))
                pest = int(input("ENTER YOUR CHOICE: "))
                print("YOU HAVE SUCCESSFULLY ORDERED CHOCLATE PASTRY!!!")
                cur.execute("select*from menu where Products = 'CHOCLATE PASTRY'")
                for i in cur:
                    p = i[2]
                    val.commit()
                print("TOTAL AMOUNT: ",qtiy*p)
                print(".........................................................")
                print("YOUR BILL")
                print("_________________________________________________________")
                print("CUSTMOR'S NAME: ",name)
                print("PHONE NUMBER: ",phone)
                print("CHOCLATE PASTRY")
                print("NO. OF PASTRIES",qtiy)
                print("_____________********THANK YOU FOR ORDERING*******_____________")
                print("\t\t\t\t\t\tDATE: ",datetime.now()) 
            elif d == 4:
                print("HOW MUCH BRWONY PIECES DO YOU WANT?")
                qtiyb = int(input("ENTER YOUR QUANTITY: "))
                print("YOU HAVE SUCCESFULLY ORDERED!!!!!!\n",qtiyb,"PIECES OF BRWONIES")
                cur.execute("select*from menu where Products = 'BROWNY'")
                for i in cur:
                    b = i[2]
                    val.commit()
                print("TOTAL AMOUNT: ",qtiyb*b)
                print(".........................................................")
                print("YOUR BILL")
                print("_________________________________________________________")
                print("CUSTMOR'S NAME: ",name)
                print("PHONE NUMBER: ",phone)
                print("BRWONIES")
                print("NO. OF BRWONIES",qtiyb)
                print("_____________********THANK YOU FOR ORDERING*******_____________")
                print("\t\t\t\t\t\tDATE: ",datetime.now())
            elif  d == 5:
                print("HOW MANY COLESLOE CHEESE SANDWICH DO YOU WANT?")
                qtiyc = int(input("ENTER QUANTITY TO ORDER: "))
                print("YOU HAVE SUCCESSFULLY ORDERED",qtiyc,"OF COLESLOE CHEESE SANDWICH")
                cur.execute("select*from menu where Products = 'COLESLOE CHEESE SANDWICH'")
                for i in cur:
                    s = i[2]
                    val.commit()
                print("TOTAL AMOUNT: ",qtiyc*s)
                print(".........................................................")
                print("YOUR BILL")
                print("_________________________________________________________")
                print("CUSTMOR'S NAME: ",name)
                print("PHONE NUMBER: ",phone)
                print("BRWONIES")
                print("NO. OF BRWONIES",qtiyc)
                print("_____________********THANK YOU FOR ORDERING*******_____________")
                print("\t\t\t\t\t\tDATE: ",datetime.now())
            elif d == 6:
                print("HOW MANY MINI PIZZAS DO YOU WANT TO ORDER?")
                quntyp = int(input("ENTER THE NO. OF MINI PIZZAS: "))
                print("YOU HAVE SUCCESSFULLY ORDERED",quntyp,"OF MINI PIZZAS")
                cur.execute("select*from menu where Products = 'MINI PIZZA'")
                for i in cur:
                    p =i[2]
                print("TOTAL AMOUNT: ",quntyp*p)
                print(".........................................................")
                print("YOUR BILL")
                print("_________________________________________________________")
                print("CUSTMOR'S NAME: ",name)
                print("PHONE NUMBER: ",phone)
                print("BRWONIES")
                print("NO. OF BRWONIES",quntyp)
                print("_____________********THANK YOU FOR ORDERING*******_____________")
                print("\t\t\t\t\t\tDATE: ",datetime.now())
            elif d == 7:
                print("HOW MANY CREAM ROLLS DO YOU WANT TO ORDER?")
                quntyr = int(input("ENTER THE NO. OF CREAM ROLLS: "))
                print("YOU HAVE SUCCESSFULLY ORDERED",quntyr,"OF CREAM ROLLS")
                cur.execute("select*from menu where Products = 'CREAM ROLL'")
                for i in cur:
                    r =i[2]
                print("TOTAL AMOUNT: ",quntyr*r)
                print(".........................................................")
                print("YOUR BILL")
                print("_________________________________________________________")
                print("CUSTMOR'S NAME: ",name)
                print("PHONE NUMBER: ",phone)
                print("BRWONIES")
                print("NO. OF BRWONIES",quntyr)
                print("_____________********THANK YOU FOR ORDERING*******_____________")
                print("\t\t\t\t\t\tDATE: ",datetime.now())
            elif d == 8:
                print("HOW MANY MASALA CROSSIANTS DO YOU WANT TO ORDER?")
                quntyt = int(input("ENTER THE NO. OF MASALA CROSSIANTS: "))
                print("YOU HAVE SUCCESSFULLY ORDERED",quntyt,"OF MASALA CROSSIANTS")
                cur.execute("select*from menu where Products = 'MINI PIZZA'")
                for i in cur:
                    t =i[2]
                print("TOTAL AMOUNT: ",quntyt*t)
                print(".........................................................")
                print("YOUR BILL")
                print("_________________________________________________________")
                print("CUSTMOR'S NAME: ",name)
                print("PHONE NUMBER: ",phone)
                print("BRWONIES")
                print("NO. OF BRWONIES",quntyt)
                print("_____________********THANK YOU FOR ORDERING*******_____________")
                print("\t\t\t\t\t\tDATE: ",datetime.now())
            elif d in l:
                qtyl = int(input("ENTER QUANTITY: "))
                print("YOU HAVE SUCCESSFULLY ORDERED YOUR SELECTED ITEM!!!\t")
                cur.execute("select*from menu where Sno = ",str(d))
                for i in cur:
                    n = i[2]
                print("TOTAL AMOUNT: ",qtyl*n)
                print(".........................................................")
                print("YOUR BILL")
                print("_________________________________________________________")
                print("CUSTMOR'S NAME: ",name)
                print("PHONE NUMBER: ",phone)
                print("BRWONIES")
                print("NO. OF BRWONIES",qtyl)
                print("_____________********THANK YOU FOR ORDERING*******_____________")
                print("\t\t\t\t\t\tDATE: ",datetime.now())
            else:
                print("WRONG INPUT!!!!!!!!!!!!!\t\t\t\t\t\t")
    else:
        break
        
