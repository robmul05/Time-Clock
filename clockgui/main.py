from tkinter import *
from tkinter import ttk
from tkinter import font as tkFont
import datetime
import platform
try:
    import winsound
except:
    import os
import math
window = Tk()
window.title("Time Clock")
window.geometry('900x500')

time_font = tkFont.Font(size=12,weight='bold')
current_time = datetime.datetime.now().strftime("%m-%d-%Y %H:%M %p")

def time_in(time):
	time_in_button.config(bg='green',state='disabled')
	print(time)
	if time_in_button['state'] == 'disabled':
		time_in_button.after(1500,refresh_button_in)

def time_out(time):
	time_out_button.config(bg='red',state='disabled')
	print(time)
	if time_out_button['state'] == 'disabled':
		time_out_button.after(1500,refresh_button_out)

def refresh_button_out():
	time_out_button.config(bg='gray', state='normal')
		

def refresh_button_in():
	time_in_button.config(bg='gray', state='normal')


def name():
	name_label.config(text='Insert Name')

def clock():
        date_time = datetime.datetime.now().strftime("%m-%d-%Y %H:%M:%S/%p")
        date,time1 = date_time.split()
        time2,time3 = time1.split('/')
        hour,minutes,seconds =  time2.split(':')
        if int(hour) > 12 and int(hour) < 24:
                time = str(int(hour) - 12) + ':' + minutes + ':' + seconds + ' ' + time3
        else:
                time = time2 + ' ' + time3
        time_label.config(text = time)
        date_label.config(text= date)
        time_label.after(1000, clock)

def get_name():
	names = description.get()
	print(names)



tabs_control = ttk.Notebook(window)
clock_tab = Frame(tabs_control)

name_label = Label(clock_tab,font='calibri 12',text='Insert Name')
name_label.grid(column=1,row=3,pady=20)
description = StringVar()
name_entry = Entry(clock_tab,width=20,textvariable=description)
name_entry.grid(row=3,column=2)

tabs_control.add(clock_tab, text="Clock")

tabs_control.pack(expand = 1, fill ="both")
time_label = Label(clock_tab, font = 'calibri 40 bold', foreground = 'black')
time_label.grid(row=0,column=1,columnspan=2)
date_label = Label(clock_tab, font = 'calibri 40 bold', foreground = 'black')
date_label.grid(row=1, column=1,columnspan=2)


time_in_button = Button(clock_tab,height=7, width=20, text='Clock In', font=time_font, bg='gray', command=lambda:[time_in(current_time),get_name()])
time_in_button.grid(row=4, padx=50,pady=50)

time_out_button = Button(clock_tab, height=7,width=20, text='Clock Out', font=time_font,bg='gray',command=lambda:[time_out(current_time),get_name()])
time_out_button.grid(row=4, column=3)

clock()

window.mainloop()
