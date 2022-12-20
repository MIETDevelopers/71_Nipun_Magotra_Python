from tkinter import *
from playsound import playsound
import time

root=Tk()
root.title("Timer")
root.geometry("400x600")
root.config(bg="#000")
root.resizable(False,False)
heading=Label(root,text="Timer",font="arial 30 bold",bg="#000",fg="#ea3548")
heading.pack(pady=10)

#clock
Label(root,font=("arial",15,"bold"),text="current time:",bg="papaya whip").place(x=65,y=70)

def clock():
    clock_time=time.strftime("%H:%M:%S %p")
    current_time.config(text=clock_time)
    current_time.after(1000,clock)

current_time=Label(root,font=("arial",15,"bold"),text="",fg="#356",bg="#fff")
current_time.place(x=190,y=70)
clock()


#Timer-Hours
hours=StringVar()
Entry(root,textvariable=hours,width=2,font="arial 50",bg="#000",fg="#fff",bd=0).place(x=30,y=155)
hours.set("00")
#Timer=Minutes
minutes=StringVar()
Entry(root,textvariable=minutes,width=2,font="arial 50",bg="#000",fg="#fff",bd=0).place(x=150,y=155)
minutes.set("00")
#Timer-Seconds
seconds=StringVar()
Entry(root,textvariable=seconds,width=2,font="arial 50",bg="#000",fg="#fff",bd=0).place(x=270,y=155)
seconds.set("00")

Label(root,text="hours",font="arial 12",bg="#000",fg="#fff").place(x=105,y=200)
Label(root,text="minutes",font="arial 12",bg="#000",fg="#fff").place(x=225,y=200)
Label(root,text="seconds",font="arial 12",bg="#000",fg="#fff").place(x=345,y=200)

def Timer():
    times=int(hours.get())*3600+int(minutes.get())*60+int(seconds.get())

    while times>-1:
        minute,second=(times//60,times%60)
        hour=0
        if minute>60:
            hour,minute=(minute//60,minute%60)
        seconds.set(second)
        minutes.set(minute)
        hours.set(hour)
        root.update()
        time.sleep(1)

        if(times==0):
            playsound("Python Projects\Timer\y2mate.com - Intro 10 seconds.mp3")
            seconds.set("00")
            minutes.set("00")
            hours.set("00")
        times -= 1

def brush():
    hours.set("00")
    minutes.set("02")
    seconds.set("00")

def face():
    hours.set("00")
    minutes.set("15")
    seconds.set("00")

def eggs():
    hours.set("00")
    minutes.set("10")
    seconds.set("00")
    
#Button

button=Button(root,text="Start",bg="#ea3548",bd=0,fg="#fff",width=20,height=2,font="arial 10 bold",command=Timer)
button.pack(padx=5,pady=40,side=BOTTOM)

Image1=PhotoImage(file="Python Projects/Timer/brush.png")
button1=Button(root,image=Image1,bg="#000",bd=0,command=brush)
button1.place(x=7,y=300)


Image2=PhotoImage(file="Python Projects/Timer/face.png")
button2=Button(root,image=Image2,bg="#000",bd=0,command=face)
button2.place(x=137,y=300)


Image3=PhotoImage(file="Python Projects\Timer\eggs.png")
button3=Button(root,image=Image3,bg="#000",bd=0,command=eggs)
button3.place(x=267,y=300)



root.mainloop()