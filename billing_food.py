import mysql.connector
from tkinter import *
from PIL import Image, ImageTk
import time
win=Tk()

sub=0
n=""
one=""
two=""
three=""
four=""
five=""
d=""
d2=""
I1P=0
I2P=0
I3P=0
I4P=0
I5P=0
D1P=0
D2P=0
Q1=0
Q2=0
Q3=0
Q4=0
Q5=0
Q6=0
Q7=0
taxval=0
totalval=0
def submit():
    global I1P,I2P,I3P,I4P,I5P,D1P,D2P,sub,n
    global one,two,three,four,five,d,d2,taxval,totalval
    global I1P,I2P,I3P,I4P,I5P,D1P,D2P,Q1,Q2,Q3,Q4,Q5,Q6,Q7
    n=name_entry.get()
    one=one_entry.get()
    two=two_entry.get()
    three=three_entry.get()
    four=four_entry.get()
    five=five_entry.get()
    d=drink_entry1.get()
    d2=drink_entry2.get()
    Q1=q1.get()
    Q2=q2.get()
    Q3=q3.get()
    Q4=q4.get()
    Q5=q5.get()
    Q6=q6.get()
    Q7=q7.get()
    if(one=="Burger"):
      I1P=7
    if(one=="French Fries"):
      I1P=6
    if(one=="Cheese Curds"):
      I1P=4
    if(one=="Cheese Pizza"):
      I1P=6
    if(one=="Dumplings"):
      I1P=7
    if(two=="Burger"):
      I2P=7
    if(two=="French Fries"):
      I2P=6
    if(two=="Cheese Curds"):
      I2P=4
    if(two=="Cheese Pizza"):
      I2P=6
    if(two=="Dumplings"):
      I2P=7
    if(three=="Burger"):
      I3P=7
    if(three=="French Fries"):
      I3P=6
    if(three=="Cheese Curds"):
      I3P=4
    if(three=="Cheese Pizza"):
      I3P=6
    if(three=="Dumplings"):
      I3P=7
    if(four=="Burger"):
      I4P=7
    if(four=="French Fries"):
      I4P=6
    if(four=="Cheese Curds"):
      I4P=4
    if(four=="Cheese Pizza"):
      I4P=6
    if(four=="Dumplings"):
      I4P=7
    if(five=="Burger"):
      I5P=7
    if(five=="French Fries"):
      I5P=6
    if(five=="Cheese Curds"):
      I5P=4
    if(five=="Cheese Pizza"):
      I5P=6
    if(five=="Dumplings"):
      I5P=7
    if(d=="Pepsi"):
      D1P=4
    if(d=="Fanta"):
      D1P=5
    if(d2=="Pepsi"):
      D2P=4
    if(d2=="Fanta"):
      D2P=5
    sub=I1P*Q1+I2P*Q2+I3P*Q3+I4P*Q4+I5P*Q5+D1P*Q6+D2P*Q7
    taxval=sub*0.1
    totalval=sub+sub*0.1
    mydb=mysql.connector.connect(host='localhost',user='root',password='password')
    cur=mydb.cursor()
    cur.execute("USE my_company_data")
    cur.execute("""INSERT INTO food_billing(name,item1,item2,item3,item4,
                item5,drink1,drink2,item1_price,item2_price,item3_price,
                item4_price,item5_price,drink1_price,drink2_price,sub_total,
                tax,total,timestamp,day) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,
                %s,%s,%s,%s,%s,%s)""",(n,one,two,three,four,five,d,d2,I1P,I2P,I3P,I4P,I5P,D1P,D2P,sub,taxval,totalval,time.strftime("%H:%M:%S"),time.strftime("%d:%m:%Y")))
                
        
    mydb.commit()
    mydb.close()
def delete_all():
    mydb=mysql.connector.connect(host='localhost',user='root',password='password')
    cur=mydb.cursor()
    cur.execute("USE my_company_data")
    cur.execute("""TRUNCATE TABLE food_billing""")
    mydb.commit()
    mydb.close()
name=Label(win,text="Name")
name.place(x=30,y=40)
name_entry=Entry(win)
name_entry.place(x=80,y=40)
item_1=Label(win,text="item 1")
item_1.place(x=30,y=70)
one_entry=Entry(win)
one_entry.place(x=80,y=70)
item_2=Label(win,text="item 2")
item_2.place(x=30,y=100)
two_entry=Entry(win)
two_entry.place(x=80,y=100)
item_3=Label(win,text="item 3")
item_3.place(x=30,y=130)
three_entry=Entry(win)
three_entry.place(x=80,y=130)
item_4=Label(win,text="item 4")
item_4.place(x=30,y=160)
four_entry=Entry(win)
four_entry.place(x=80,y=160)
item_5=Label(win,text="item 5")
item_5.place(x=30,y=190)
five_entry=Entry(win)
five_entry.place(x=80,y=190)
drink_1=Label(win,text="drink 1")
drink_1.place(x=30,y=220)
drink_entry1=Entry(win)
drink_entry1.place(x=80,y=220)
drink_2=Label(win,text="drink 2")
drink_2.place(x=30,y=250)
drink_entry2=Entry(win)
drink_entry2.place(x=80,y=250)
submit_button=Button(win,text="Submit",command=submit)
submit_button.place(x=80,y=280)
picture="Neha's_Billing_App_logo.png"
img=ImageTk.PhotoImage(Image.open(picture))
logo=Label(win,image=img)
logo.place(x=240,y=35)
d=Button(win,text="DELETE ALL",command=delete_all)
d.place(x=700,y=35)
q1=Entry(win,width=4)
q1.place(x=70,y=70)
q2=Entry(win,width=4)
q2.place(x=70,y=100)
q3=Entry(win,width=4)
q3.place(x=70,y=130)
q4=Entry(win,width=4)
q4.place(x=70,y=160)
q5=Entry(win,width=4)
q5.place(x=70,y=190)
q6=Entry(win,width=4)
q6.place(x=70,y=220)
q7=Entry(win,width=4)
q7.place(x=70,y=250)
win.mainloop()
