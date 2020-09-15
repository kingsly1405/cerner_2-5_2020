#Lets code and celebrate the 'Engineering Productivity' cerner_2^5_2020
#author - Kingsly, Philomin Irudayaraj
import time
import datetime as dt
import tkinter
from tkinter import messagebox
from tkinter import simpledialog
import winsound
# hide main window
root = tkinter.Tk()
root.withdraw()
total_pomodoros = 0
# Collect time information
t_now = dt.datetime.now()                       # Current time for reference.   [datetime object]
t_pom = 25*60                                    # Pomodoro time                 [int, seconds]
t_delta = dt.timedelta(0,t_pom)                 # Time delta in mins            [datetime object]
t_fut = t_now + t_delta                         # Future time for reference     [datetime object]
# GUI set pomodoro in motion!
messagebox.showinfo("Pomodoro Started!", "\nIt is now "+t_now.strftime("%H:%M") + " hrs. \nTimer set for 25 Min.")
# Main script
while True:
    if t_now < t_fut:
        #Focusing on work
        print('Focusing on work')
    else:
        # Ring a bell (with print('\a') to alert of end of program.
        # Annoy!
        for i in range(10):
            winsound.Beep((i+100), 500)
        usr_ans = messagebox.askyesno("Pomodoro Finished!","Would you like to start another pomodoro?")
        total_pomodoros += 1
        if usr_ans == True:
            # user wants another pomodoro! Update values to indicate new timeset.
            t_now = dt.datetime.now()
            t_fut = t_now + dt.timedelta(0,t_pom)
            continue
        elif usr_ans == False:
            messagebox.showinfo("Pomodoro Finished!", "\nIt is now "+timenow+ "\nYou completed "+str(total_pomodoros)+" pomodoros today!")
            break
    # check every 3 seconds and update current time
    time.sleep(30)
    t_now = dt.datetime.now()
    timenow = t_now.strftime("%H:%M")