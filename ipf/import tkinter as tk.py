import tkinter as tk
from tkinter import Label,filedialog,Entry,Checkbutton,scrolledtext
from tkinter.ttk import Combobox, Frame
window = tk.Tk()
window.title("form")
window.geometry("600x400")

# Heading
title_frame = Frame(window)
title_frame.pack()

label2 = Label(title_frame,text="REGISTRATION  FORM",anchor="center",font=(15),fg="#FF00FF")
label2.grid(row=0,column=2) 

# Details
details_frame = Frame(window)
details_frame.pack()

label3 = Label(details_frame,text="First Name")
entry1 = Entry(details_frame,width=30)
label3.grid(row=5,column=1)
entry1.grid(row=5,column=5)
label4 = Label(details_frame,text="Last Name")
entry2 = Entry(details_frame,width=30)
label4.grid(row=8,column=1)
entry2.grid(row=8,column=5)

label5 = Label(details_frame,text="Gender")
label5.grid(row=11,column=1)
check=Checkbutton(details_frame,text="male",selectcolor="white")
check.grid(row=11,column=3)
check1=Checkbutton(details_frame,text="female")
check1.grid(row=11,column=5)

label6= Label(details_frame,text="Age")
label6.grid(row=14,column=1)
entry3 = Entry(details_frame,width=30)
entry3.grid(row=14,column=5)
label7 = Label(details_frame,text="date of birth")
entry4 = Entry(details_frame,width=30)
label7.grid(row=17,column=1)
entry4.grid(row=17,column=5)
label8= Label(details_frame,text="date of birth")
entry5 = Entry(details_frame,width=30)
label8.grid(row=20,column=1)
entry5.grid(row=20,column=5)
label8= Label(details_frame,text="Email address")
entry5 = Entry(details_frame,width=30)
label8.grid(row=23,column=1)
entry5.grid(row=23,column=5)
label8= Label(details_frame,text="password")
password = Entry(details_frame,width=30,show="&")
label8.grid(row=26,column=1)
password.grid(row=26,column=5)
label9= Label(details_frame,text="confirm password")
password1 = Entry(details_frame,width=30,show="&")
label9.grid(row=29,column=1)
password1.grid(row=29,column=5)

phone= Label(details_frame,text="Phone number")
phone.grid(row=32,column=1)

num=['+91','+92','+93']
combobox=Combobox(details_frame,value=num ,width=2)
combobox.grid(row=32,column=4)
entry5 = Entry(details_frame,width=30)
entry5.grid(row=32,column=5)

address= Label(details_frame,text="Address")
address.grid(row=37,column=1)

scroll=scrolledtext.ScrolledText(details_frame,width=35,height=5)
scroll.grid(row=37,column=5)


statel=Label(details_frame,text="state")
statel.grid(row=43,column=1)

state=['kerala','tamilnadu','andrapradesh']
combostate =Combobox(details_frame,value=state,width=10)
combostate.grid(row=43,column=10)
entrystate = Entry(details_frame,width=30)
entrystate.grid(row=43,column=5)

pin = Label(details_frame,text="enter your pin")
pin.grid(row=47,column=1)
pinentry = Entry(details_frame,width=30)
pinentry.grid(row=47,column=5)

hobbies = Label(details_frame,text="hobbies")
hobbies.grid(row=50,column=1)
hentry = Entry(details_frame,width=30)
hentry.grid(row=50,column=5)




details_frame.mainloop() 