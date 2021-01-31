from tkinter import *
from tkinter import messagebox
import datetime

root=Tk()
root.title('Age Calculator')
root.geometry('350x450')
root.resizable(width=FALSE,height=FALSE)
l=Label(root,text="AGE CALCULATOR",font=("Algerian",20,"bold"))
l.pack(side=TOP)
l1=Label(root,text="Enter date",font=("Algerian",15,"bold"))
l1.place(x=20,y=50)
e1=Entry(root,bd=5)
e1.place(x=200,y=50)
l2=Label(root,text="Enter month ",font=("Algerian",15,"bold"))
l2.place(x=20,y=80)
e2=Entry(root,bd=5)
e2.place(x=200,y=80)
l3=Label(root,text="Enter year ",font=("Algerian",15,"bold"))
l3.place(x=20,y=110)
e3=Entry(root,bd=5)
e3.place(x=200,y=110)


def age_cal():
    current_date=datetime.datetime.now()
    #converting input into date format
    t_bdate=datetime.date(int(e3.get()),int(e2.get()),int(e1.get()))
    #converting into string(because strptime() takes a string as a argument)
    tb1=t_bdate.strftime('%Y-%m-%d')

    #converting it in actual datetime
    tbday=datetime.datetime.strptime(tb1,'%Y-%m-%d')
    year=current_date-tbday

    # for years: total seconds lived/one year seconds
    years = ((year.total_seconds()) / (365.242 * 24 * 3600))
    yearsInt = int(years)

    month=(years-yearsInt)*12
    monthInt=int(month)

    days=((month-monthInt)*(365.242/12))-1
    daysInt=int(days)
    hours = (days-daysInt)*24
    hoursInt=int(hours)

    minutes = (hours-hoursInt)*60
    minutesInt=int(minutes)

    seconds = (minutes-minutesInt)*60
    secondsInt =int(seconds)
    l4 = Label(root, text="Hello there Buddy", font=("Algerian", 18, "bold"))
    l4.place(x=52, y=200)
    l5=Label(root,text='You are '+str(yearsInt)+' year,',font=("Algerian", 18, "bold"))
    l5.place(x=57,y=230)
    l6 = Label(root, text=str(monthInt) + ' month,'+str(daysInt) + ' day,', font=("Algerian", 18, "bold"))
    l6.place(x=57, y=260)
    l7 = Label(root, text=str(hoursInt) + ' hour,'+str(minutesInt) + ' minute,', font=("Algerian", 18, "bold"))
    l7.place(x=57, y=290)
    l8 = Label(root, text=str(secondsInt) + ' seconds old,', font=("Algerian", 18, "bold"))
    l8.place(x=57, y=320)


button=Button(root,text="Calculate Age",command=age_cal)
button.place(x=125,y=150)
root.mainloop()