from Bank import l
import sqlite3
conn=sqlite3.connect("Bank1.db")
cursor=conn.cursor()
print("database connect successfully")
cursor.execute(""" create table Customer_details
               (
               id number primary key,
               Name varchar(32),
               account_num number(14) unique not null,
               account_type varchar(20),
               balance number default(500),
               branch varchar(20),
               phone number(10),
               email_id varchar(40),
               gender char(6),
               pin number(4)

               ) """)
print("table is created successfully")

for i in l:
    cursor.execute(f''' insert into Customer_details values({i.id},'{i.Name}',{i.account_number},'{i.account_type}',{i.balance},'{i.branch}',{i.phone},'{i.email}','{i.gender}',{i.pin_number})''')
    conn.commit()
    print("data is added succesfully")



