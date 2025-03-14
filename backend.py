from tkinter import *


import sqlite3
from tkinter import messagebox
con = sqlite3.connect('c:/Users/89parham/Documents/exam_projet/contact3.db')
cur=con.cursor()
cur.execute('create table if not exists persons (fname txt,lname txt,email txt ,password txt)')

def sign_in(password,email):
    p=cur.execute('select * from persons where password =? and email=?',(password,email))
    d=p.fetchall()

    if d != []:
        print(d)
        win1=Tk()
    else:
        messagebox.showerror('error','passord or email is wrong')



#========================================


def sing_up (fname,lname,email,password):
    
    cur.execute('insert into persons values (?,?,?,?)',(fname,lname,email,password))
    con.commit()

    
#========================================


#================================================
