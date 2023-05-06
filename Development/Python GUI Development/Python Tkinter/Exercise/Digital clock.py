from tkinter import *
import datetime

def date_and_time():
    time = datetime.datetime.now()
    Hour = time.strftime('%I')
    Minute = time.strftime('%M')
    Second = time.strftime('%S')
    Am_Pm = time.strftime('%p')

    date = time.strftime('%d')
    month = time.strftime('%m')
    year = time.strftime('%y')
    day = time.strftime('%a')

    # set current date and time
    lab_hr.config(text=Hour)
    lab_min.config(text=Minute)
    lab_sec.config(text=Second)
    lab_AM_PM.config(text=Am_Pm)

    lab_date.config(text=date)
    lab_month.config(text=month)
    lab_year.config(text=year)
    lab_day.config(text=day)

    # Change the seconds in every 200 milliseconds
    lab_hr.after(200, date_and_time)

clock = Tk()
clock.title("Digital Clock")
clock.geometry("1000x500")
clock.config(bg="#f5f5dc")

# __________ For Time __________
lab_hr = Label(clock, text="00", font=("Aparajita", 60), bg="black", fg="#39ff14")
lab_hr.place(x=120, y=50, height=110, width=100)
lab_hr_txt = Label(clock, text="Hour", font=("Poor Richard", 25), bg="#f5f5dc", fg="red")
lab_hr_txt.place(x=120, y=190, height=40, width=100)

lab_min = Label(clock, text="00", font=("Aparajita", 60), bg="black", fg="#39ff14")
lab_min.place(x=340, y=50, height=110, width=100)
lab_min_txt = Label(clock, text="Minutes", font=("Poor Richard", 25), bg="#f5f5dc", fg="red")
lab_min_txt.place(x=340, y=190, height=40, width=100)

lab_sec = Label(clock, text="00", font=("Aparajita", 60), bg="black", fg="#39ff14")
lab_sec.place(x=560, y=50, height=110, width=100)
lab_sec_txt = Label(clock, text="Seconds", font=("Poor Richard", 25), bg="#f5f5dc", fg="red")
lab_sec_txt.place(x=560, y=190, height=40, width=100)

lab_AM_PM = Label(clock, text="00", font=("Aparajita", 60), bg="black", fg="#Bf00ff")
lab_AM_PM.place(x=780, y=50, height=110, width=100)
lab_AM_PM_txt = Label(clock, text="AM/PM", font=("Poor Richard", 22, "bold"), bg="#f5f5dc", fg="#Ca2c92")
lab_AM_PM_txt.place(x=780, y=190, height=40, width=100)

# __________ For date __________
lab_date = Label(clock, text="00", font=("Aparajita", 60), bg="black", fg="#39ff14")
lab_date.place(x=120, y=270, height=110, width=100)
lab_date_txt = Label(clock, text="Date", font=("Poor Richard", 25), bg="#f5f5dc", fg="red")
lab_date_txt.place(x=120, y=410, height=40, width=100)

lab_month = Label(clock, text="00", font=("Aparajita", 60), bg="black", fg="#39ff14")
lab_month.place(x=340, y=270, height=110, width=100)
lab_month_txt = Label(clock, text="Month", font=("Poor Richard", 25), bg="#f5f5dc", fg="red")
lab_month_txt.place(x=340, y=410, height=40, width=100)

lab_year = Label(clock, text="00", font=("Aparajita", 60), bg="black", fg="#39ff14")
lab_year.place(x=560, y=270, height=110, width=100)
lab_year_txt = Label(clock, text="year", font=("Poor Richard", 25), bg="#f5f5dc", fg="red")
lab_year_txt.place(x=560, y=410, height=40, width=100)

lab_day = Label(clock, text="00", font=("Aparajita", 60), bg="black", fg="#Bf00ff")
lab_day.place(x=780, y=270, height=110, width=100)
lab_day_txt = Label(clock, text="Day", font=("Poor Richard", 22, "bold"), bg="#f5f5dc", fg="#Ca2c92")
lab_day_txt.place(x=780, y=410, height=40, width=100)

date_and_time()
clock.mainloop()

