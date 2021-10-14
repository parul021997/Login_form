from tkinter import *
from tkinter import messagebox as ms
import sqlite3

win = Tk()
win.geometry('800x800')
win.title("Login  Form")

#field for gui
UserName=StringVar()
Password=StringVar()

def database():
    
    un=UserName.get()
    print(un)
    ps=Password.get()
    print(ps)
  
#connection with db 
    
    conn = sqlite3.connect('Register.db')
    with conn:
      cursor=conn.cursor()
      cursor.execute("select * from Student where Name=='"+un+"'and Pass=='"+ps+"'")
      result=cursor.fetchone()
   
    if result==None:
       ms.showwarning("invalid  Entry")
       
       
    else:
        ms.showwarning("Login Detail "," User_Name " + UserName.get()+" Password: "+Password.get())
        #label1=tk.Label(ms,text="Your name: "+un.get())
        #label2=tk.Label(ms,text="Your password: "+ps.get())
        #label1.place(x=10,y=125)
        #label2.place(x=10,y=150)
  
       
Uname= Label(win, text="UserName",width=20)
Uname.place(x=80,y=130)
Uname1 = Entry(win,textvar=UserName)
Uname1.place(x=240,y=130)

Pwd= Label(win, text="Password",width=20)
Pwd.place(x=68,y=180)
Pwd1 = Entry(win,textvar=Password)
Pwd1.place(x=240,y=180)  

Button(win, text='Login',width=20,bg='brown',fg='white',command=database).place(x=180,y=420)     
       
win.mainloop()       
       
       
       
    




