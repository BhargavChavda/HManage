import mysql.connector #importing mysql.connector to connect python to MySQL
from datetime import date #importing date from datetime to use later in code

#Clearing the App Screen 
def clear():
    for _ in range(65): #for loop to add new lines to make output look clean
        print()

#Existing Room Check function (for addr)
def roomc():
    con = mysql.connector.connect(host='localhost', database= 'hm', user = 'root',password = 'j123') #connecting mysql
    cur = con.cursor() #cursor to execute mySQL scripts

    script = "SELECT * FROM rooms WHERE roomno =" +room_no+ ";" #script to select inputted room no.
    cur.execute(script)
    ans = cur.fetchone() #fetching the record and storing it in ans
    return ans

#Add Room Function
def addr():
    con = mysql.connector.connect(host='localhost', database= 'hm', user = 'root',password = 'j123')
    cur = con.cursor()

    global room_no #making room_no a global variable to use in the above function

    clear() #clear output screen
    print("Add new room: \n")
    room_no = input("\n Enter Room Number: ")
    room_type = input("\n Enter Room Type (AC,Non-AC,Suite): ")
    room_rent = input("\n Enter Room Rent (INR): ")
    room_stat = input("\n Enter the room's status (Available, Occupied): ")

    script = 'INSERT INTO ROOMS(roomno,roomt,roomr,status)VALUES ('+room_no+',"'+room_type+'",'+room_rent+',"'+room_stat+'");' #inserting the values in rooms
    check = roomc() #using the roomc function to check if the inputted room exists
    if check == None:
        cur.execute(script)
    else:
        print("The Room Number entered already exists.")
    con.commit() #committing changes
    con.close() #closing the connection
    wait = input('\n Press any key to continue.')

#Add Customer Function
def addc():
    con = mysql.connector.connect(host='localhost', database= 'hm', user = 'root',password = 'j123')
    cur = con.cursor()

    clear()
    print("Add Customer Details: \n")
    cust_name = input("\n Enter Name: ")
    cust_add = input("\n Enter address: ")
    cust_phone = input("\n Enter Phone number: ")
    cust_email = input("\n Enter Email: ")
    cust_id = input("\n Enter ID Option(Passport, Aadhar Card, Pan Card): ")
    cust_idproof = input("\n Enter ID No.: ")
    cust_m = input("\n Enter number of males: ")
    cust_f = input("\n Enter number of females: ")
    cust_c = input("\n Enter number of children: ")

    script = 'INSERT INTO customer(name, address, phone, email, idproof, idproofno, children, female, male)VALUES ("'+cust_name+'","'+cust_add+'","'+cust_phone+'","'+cust_email+'","'+cust_id+'","'+cust_idproof+'",'+cust_c+','+cust_f+','+cust_m+');'
    cur.execute(script)
    con.commit()
    con.close()

    wait = input('\n Press any key to continue.') #to reset and go back to the menu


#Room Booking function
def room_book():
    con = mysql.connector.connect(host='localhost', database= 'hm', user = 'root',password = 'j123')
    cur = con.cursor()

    clear()

    print("Insert Details: \n")
    room_numb = input('\n Enter Room Number: ')
    cust_id = str(input('\n Enter Customer ID: ')) #cust_id, book_in and book_out are strings as int and dates are not concatenatable
    book_in = str(date.today())
    book_out = str(input('\n Enter Checkout Date (YYYY-MM-DD): '))

    script0 = 'select * from rooms where roomno =' +room_numb+ ';' #selecting record
    cur.execute(script0)
    rez = cur.fetchone()

    rid = str(rez[0]) #fetching room id from the record

    script = 'update rooms set status = "Occupied" where roomno ='+room_numb+';' #set room's status from Available to Occupied when booked
    script1 = 'INSERT INTO bookings(room_id,cust_id,room_no,checkin,checkout) VALUES('+rid+','+cust_id+',"'+room_numb+'","'+book_in+'","'+book_out+'");' #inserting values in bookings

    cur.execute(script)
    cur.execute(script1)

    con.commit()
    con.close
    
    wait = input('\n Press any key to continue.')


#Bill generation
def billgen():
    con = mysql.connector.connect(host='localhost', database= 'hm', user = 'root',password = 'j123')
    cur = con.cursor()

    cout = date.today() #for bill generation setting check out date as today's date
    rid = int(input("Enter the room number: \n"))
    sql = 'select * from bookings where room_no='+str(rid)+';'
    cur.execute(sql)
    res = cur.fetchone()

    cin = res[4] #fetching checkin date from record
    days = (cout-cin).days #calculation for the number of days stayed

    sql2 = 'select * from rooms where roomno ='+str(rid)+';'
    cur.execute(sql2)
    res2 = cur.fetchone()

    rent = res2[3] #fetching rent for the room
    netamount = days*rent #calculation for the amount to be paid

    rno = res2[1] #fetching room no. for later use

    clear()
    
    print('-'*100)
    print('Check-in: ', cin)
    print('Check-out: ', cout)
    print('Room No: ', rno)
    print('Rent per night: ', rent)    
    print('Amount to pay: ', netamount)
    
    sqlupdate = 'UPDATE rooms SET status = "Available" WHERE roomno = '+str(rno)+';' #updating room status from Occupied to Available
    sqlupdate2 = 'UPDATE bookings SET checkout = "'+str(cout)+'" WHERE room_id = '+str(rid)+';' #update checkout date in bookings

    cur.execute(sqlupdate)
    cur.execute(sqlupdate2)

    con.commit()
    con.close
    
    wait = input('\nPress any key to continue.')


#Show all tables
def tab():
    con = mysql.connector.connect(host="localhost",database='hm',user="root",password="j123")
    cur = con.cursor()

    clear()

    cur.execute("SHOW TABLES;")

    for table_name in cur:
        print(table_name)

    con.commit()
    con.close
    
    wait = input('\nPress any key to continue.')

#Show contents of a specific table
def tabcon():
    con = mysql.connector.connect(host="localhost",database='hm',user="root",password="j123")
    cur = con.cursor()

    tabname = input("Enter the name of the table: \n")

    clear()

    cur.execute("SELECT * FROM "+tabname+";")

    for char in cur:
        print(char)

    wait = input('\nPress any key to continue.')


#Main menu function
def menu():
    while True: #as long as the program is running
        clear()
        print('Welcome to Hotel Management System!')
        print('by Bhargav,Harshal and Chirayu')

        print("\n 1) Add Customer")
        print("\n 2) Room Booking")
        print("\n 3) Add Room")
        print("\n 4) Bill Generation")
        print("\n 5) Show All Tables")
        print("\n 6) Show Table") 
        print("\n 7) Close Application")
        print("\n\n\n")

        choice = int(input("Enter your desired functions: \n"))
        if choice == 1:
            addc()
        if choice == 2:
            room_book()
        if choice == 3:
            addr()
        if choice == 4:
            billgen()
        if choice == 5:
            tab()
        if choice == 6:
            tabcon()
        if choice == 7:
            break


menu() #running the menu function