from tkinter import *
from tkinter import ttk
import datetime
import platform
try:
    import winsound
except:
    import os
import math
window = Tk()
window.title("Time Clock")
window.geometry('500x250')
stopwatch_counter_num = 66600
stopwatch_running = False

def time_in(time):
        print(time)


def clock():

        date_time = datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S/%p")
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

def clockin():
        emp1 = 'Melonie'
        emp2 = 'Meade'



def stopwatch(work):
         if work == 'start':
                 global stopwatch_running
                 stopwatch_running=True
                 stopwatch_start.config(state='disabled')
                 stopwatch_stop.config(state='enabled')
                 stopwatch_reset.config(state='enabled')

         elif work == 'stop':
                 stopwatch_running=False
                 stopwatch_start.config(state='enabled')
                 stopwatch_stop.config(state='disabled')
                 stopwatch_reset.config(state='enabled')
         elif work == 'reset':
                 global stopwatch_counter_num
                 stopwatch_running=False
                 stopwatch_counter_num=66600
                 stopwatch_label.config(text='Stopwatch')
                 stopwatch_start.config(state='enabled')
                 stopwatch_stop.config(state='disabled')
                 stopwatch_reset.config(state='disabled')

tabs_control = ttk.Notebook(window)
clock_tab = Frame(tabs_control)

stopwatch_tab = Frame(tabs_control)


tabs_control.add(clock_tab, text="Clock")

tabs_control.add(stopwatch_tab, text='Stopwatch')


tabs_control.pack(expand = 1, fill ="both")
time_label = Label(clock_tab, font = 'calibri 40 bold', foreground = 'black')
time_label.pack(anchor='center')
date_label = Label(clock_tab, font = 'calibri 40 bold', foreground = 'black')
date_label.pack(anchor='s')

stopwatch_label = Label(stopwatch_tab, font='calibri 40 bold', text='Stopwatch')
stopwatch_label.pack(anchor='center')
stopwatch_start = Button(stopwatch_tab, text='Start', command=lambda:stopwatch('start'))
stopwatch_start.pack(anchor='center')
stopwatch_stop = Button(stopwatch_tab, text='Stop', state='disabled',command=lambda:stopwatch('stop'))
stopwatch_stop.pack(anchor='center')
stopwatch_reset = Button(stopwatch_tab, text='Reset', state='disabled', command=lambda:stopwatch('reset'))
stopwatch_reset.pack(anchor='center')
time_in_button = Button(clock_tab,height=75, width=100, command=lambda:time_in(12))
time_in_button.pack(anchor='s')
clock()

window.mainloop()
