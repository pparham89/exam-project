from tkinter import *
from tkinter import messagebox
import sqlite3
import contacs
win = Tk()
#========================================


#========================================
win.geometry("500x350")
win.title("فرم ثبت نام")
win.resizable(0,0)
win.config(bg='light pink')
#========================================
def singin():
    if ent_password.get() and ent_email.get() != "":

        contacs.sign_in(ent_password.get(),ent_email.get())
        
    else:
        messagebox.showerror('error','enter password and email completely')
def signup():
    if ent_name.get() and ent_family .get() and ent_email.get() and ent_password.get() !='':
        contacs.sing_up(ent_name.get(),ent_family.get(),ent_email.get(),ent_password.get())
        messagebox.showinfo('done','data inserted')
    else:
        messagebox.showerror('error','enter the data completely')
#========================================
lbl_name = Label(win,text="fname :",font="_MRT_khodkar 8 bold",bg='light pink')
lbl_name.place(x=30,y=15)

lbl_family = Label(win,text="lname :",font="_MRT_khodkar 8 bold",bg='light pink')
lbl_family.place(x=247,y=15)

lbl_email= Label(win,text="email :",font="_MRT_khodkar 8 bold",bg='light pink')
lbl_email.place(x=30,y=75)

lbl_pass = Label(win,text="password :",font="_MRT_khodkar 8 bold",bg='light pink')
lbl_pass.place(x=250,y=75)


ent_name = Entry(win)
ent_name.place(x=80,y=20)

ent_family = Entry(win)
ent_family.place(x=330,y=20)

ent_email = Entry(win)
ent_email.place(x=80,y=80)

ent_password= Entry(win)
ent_password.place(x=330,y=80)



btn_signup =Button(win,text="sign up :",width=10,command=signup,bg='light pink')
btn_signup.place(x=100,y=220)


btn_signin =Button(win,text="sign in :",width=10,command=singin,bg='light pink')
btn_signin.place(x=300,y=220)




#================================================

win.mainloop()

