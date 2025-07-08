from Bank1 import l
import sqlite3
conn=sqlite3.connect("Bank1.db")
cursor=conn.cursor()
print("database connect successfully")
# cursor.execute(""" create table Customer_details
#                (
#                id number  primary key ,
#                Name varchar(32),
#                account_num number(14) unique not null,
#                account_type varchar(20),
#                balance number default(500),
#                branch varchar(20),
#                phone number(10),
#                email_id varchar(40),
#                gender char(6),
#                pin number(4)

#                ) """)
# print("table is created successfully")

def Create_account():
    # print("please provide the below datails")
    Name=input("enter the user Name :- ")
    account_num=int(input("enter the account number :- "))
    account_type=input("enter the account type :- ")
    branch=input("enter the branch :- ")
    phone=int(input("enter the phone number :- "))
    email_id=input("enter the email id :- ")
    gender=input("enter the gender :- ")

    cursor.execute(f'''
insert into Customer_details(Name,account_num,account_type,branch,phone,email_id,gender) values('{Name}',{account_num},'{account_type}','{branch}',{phone},'{email_id}','{gender}')
''')
    conn.commit()
    print("The Account  has been Created successfully!!!")
def Pin_Generation():
    account_number=int(input("enter the account number "))
    cursor.execute(f''' select * from  Customer_details where account_num ={account_number} ;''')
    a=cursor.fetchone()
    if a is not  None:
        try:
            pin=int(input("enter the pin"))
            con_pin=int(input("again enter te pin"))
            if pin==con_pin:
                length=str(pin)
                if len(length)==4:
                    cursor.execute(f''' update Customer_details set pin={pin} where account_num={account_number}''')
                    conn.commit()
                    print("your pin generation has been successfully completd ,welcome !!! thank you !!!")


        except Exception as e:
            print(f"enter the pin with 4 digits")
    else:
        print("please enter the valid account_number !!!")
def check_balance():
        account_num=int(input("enter the account number :-"))
        pin=int(input("enter the pin:-"))
        cursor.execute(f''' select * from  Customer_details where account_num ={account_num} ;''')
        a=cursor.fetchone()
    
        if a is not None:
            # for i in a:
            if pin ==a[-1]:
                print("the avilable balance in your account is :",a[4])
            else:
                print("pin is not valid ???")
        else:
            print("please enter the valid account number ,the enterd acc details are not available in database ??") 
def withdraw():
        account_num=int(input("enter the account number :-"))
        pin=int(input("enter the pin:-"))

        cursor.execute(f''' select * from  Customer_details where account_num ={account_num} ;''')
        a=cursor.fetchone()
        amount=int(input("enter the amount :- "))
    
        if a is not None:
            # for i in a:
            balance = a[4]
            if pin ==a[-1]:
                
                if amount<=balance:
                    val = balance-amount
                    print("collect the cash",amount )
                    cursor.execute(f''' update Customer_details set balance ={val} where account_num={account_num}''')
                    conn.commit()
                    print("avilble balance in your account Rs/-",val)
                else:
                    print(" not sufficent:",amount)
            else:
                print("pin is not valid ???")
        else:
            print("please enter the valid account number ,the enterd acc details are not available in database ??") 
       
def deposite():
    account_num=int(input("enter the account number :-"))
    pin=int(input("enter the pin:-"))

    cursor.execute(f''' select * from  Customer_details where account_num ={account_num} ;''')
    a=cursor.fetchone()
    amount=int(input("enter the amount :- "))
    

    
    if a is not None:
            # for i in a:
            balance = a[4]
            if pin ==a[-1]:
                
                if amount >=0:
                    val = balance + amount
                    print(f"successfully the amount {amount} is added in your  account!!!",amount )
                    cursor.execute(f''' update Customer_details set balance ={val} where account_num={account_num}''')
                    conn.commit()
                    print("avilble balance in your account Rs/-",val)
                else:
                    print("please add some money??")
            else:
                print("pin is not valid ???")
    else:
            print("please enter the valid account number ,the enterd acc details are not available in database ??") 
def Transfer():
    sender_ac_no=int(input("Enter the Sender Account Number:"))
    cursor.execute(f''' select * from Customer_details
                   where account_num=={sender_ac_no} ''')
    a=cursor.fetchone()
    if a is not None:
        reciever_ac_no=int(input("Enter the Reciever Account Number:"))
        cursor.execute(f''' select * from Customer_details
                   where account_num=={reciever_ac_no} ''')
        b=cursor.fetchone()
        
        count=0
        while count<=3:

            pin=int(input("Enter the Pin:"))

            if pin==a[-1]:

                amount=int(input("Enter the Amount:"))

                if amount<=a[4]:
                    print(a[4])
                    val=a[4]-amount
                    print(val)
                    print(f"The Amount has been Transfered Successfully \n ..Your available Balance is :{val}")
                    cursor.execute(f''' update Customer_details
                                    set balance={val} 
                                    where account_num={sender_ac_no}''')
                    conn.commit()
                    break
                else:
                    print("inceficient Balance in your account")
                    print()
            else:
                print("Invalid Pin Number..")
                count=count+1
                print()      
        if count==4:
            print("You attempt morethen 3 times wrong pin you try again after 24 hours")   
            print()    
    else:
        print("Invalid Account Number...😒")
    
    if b is not None:
        print(b[4])
        dep_value=b[4]+amount
        print(dep_value)
        print(f'Amount is successfully added..💐💐 Current Balance is :{dep_value}')
        cursor.execute(f''' update Customer_details
                       set balance={dep_value}
                        where account_num={reciever_ac_no} ''')
        conn.commit()
    else:
        print("Invalid Account Number ??.... --->Please enter the Valid Account Number..")


    
while True:
    print("please enter 1 for account creation \n please enter 2 for pin generation \n please enter 3 check balance \n please enter 4 for withdrawal \n enter 5 for diposite \n enter 6 for account transfer \n enter exit for the programme")
    user=input("please select the command :- ")
    if user== '1' :
        Create_account()
    elif user == 'exit':
        exit()
    elif user=='2':
        Pin_Generation()
    elif user=='3':
        check_balance()
    elif user=='4':
        withdraw()
    elif user=='5':
        deposite()
    elif user=='6':
        Transfer()




