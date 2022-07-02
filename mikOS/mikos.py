'''
@pdmzt

Simple Python Operating System
mikOS

June 2022
'''
from tkinter import*
from time import strftime
import datetime as dt
import os


window_dimensions = "1100x620"
os_name = "mikOS"

root = Tk()
root.title(os_name)
root.geometry(window_dimensions)
root.resizable(0,0)
root.config(cursor="arrow")


def volume_mixer():
    volumeSlider = Label(root, bg="black", borderwidth=0)
    volumeSlider.place(x=800, y=24, height=76, width=300)
    vol = Scale(
    root,
    from_ = 0,
    to = 100,
    orient = HORIZONTAL,
    bg="white"
    )
    vol.place(x=800, y=49, width=300)
    speaker_device = "Realtek High Definition Audio"
    speaker_name = Label(root, text=speaker_device, font=("Arial", 10), fg="white", bg="black")
    speaker_name.place(x=802, y=23)

# images
loginScreenWallpaper = PhotoImage(file="wallpaper.png")
loginPersonIcon = PhotoImage(file="loginPersonIcon.png")
notificationsIcon = PhotoImage(file="notifIcon.png")
enterIcon = PhotoImage(file="enter.png")
wifiIcon = PhotoImage(file="wifi.png")
sleepIcon = PhotoImage(file="sleep-icon.png")
speakerIcon = PhotoImage(file="speaker-icon.png")

loginScreenWallpaperLabel = Label(root, image=loginScreenWallpaper, borderwidth=0)      # wallpaper na login screen-u
loginScreenWallpaperLabel.place(x=-65, y=0)

bar = Label(root, text=(" " * 100000), fg="black", bg="black")  # crna traka na vrhu 
bar.place(x=-1, y=-1, height=25)

b = Label(root) # sat na vrhu welcome screen-a
b.place(x=1037, y=3.8)

def time():
    c = strftime('%H:%M')   # redoslijed pisanja vremena (sat:minuta)
    b.config(text=c,font=('DS-DIGITAL', 8), borderwidth=0, fg="white", bg="black")
    b.after(1000, time)

time()
"""

loginPersonIconLabel = Label(root, image=loginPersonIcon, borderwidth=0)
loginPersonIconLabel.place(x=487, y=160, height=100, width=100)
"""
"""
username = Label(root, text="User", font=("Arial", 14), fg="black")     # prikaz username-a na welcome zaslonu
username.place(x=515, y=270)"""

entryPassword = Entry(root, show="•", font=("Arial", 11))        # polje za unos lozinke
#entryPassword.place(x=437, y=348, width=200, height=22)
entryPassword.place(x=467, y=367)
passwButton = Button(root, image=enterIcon, borderwidth=0)
passwButton.place(x=632, y=367)


notifIconOnTop = Button(root, image=notificationsIcon, borderwidth=0, bg="black").place(x=1074, y=-1.6)     # button za notifikacije/obavijesti


date = dt.datetime.now()
date_label = Label(root, text=f"{date:%B %d, %Y}", font=("Arial", 8), fg="white", bg="black")
date_label.place(x=959, y=1.5)

wifi_icon = Button(root, image=wifiIcon, borderwidth=0, bg="black")
wifi_icon.place(x=918, y=-7)

speaker_icon = Button(root, image=speakerIcon, borderwidth=0, bg="black", command=lambda:[volume_mixer()])
speaker_icon.place(x=890, y=-2)

"""
def sleep_mode():
    
    returnToLoginScreen = Button(root, text=(""*4343), bg="black", fg="black", borderwidth=0, activebackground="black")
    returnToLoginScreen.place(x=0,y=0, width=4930, height=4343)   
    root.config(cursor="None")
    returnToLoginScreen.destroy()

"""
#  - - - - -   Nadodati root.bind_all('<anykey>', dakako)

def buttonSleep():
    def dakako(event):
        sleepMode.destroy()
        root.config(cursor="arrow")
    sleepMode = Button(root, text=(""*4323), fg="black", bg="black", activebackground="black", borderwidth=0, command=dakako)
    sleepMode.place(x=-1,y=-1, height=4430, width=4343)
    sleepMode.bind('<Return>', dakako)
    root.config(cursor="None")



    
    
sleepBtn = Button(root, text="Spavaj", command=buttonSleep)
sleepBtn.place(x=54, y=473)

root.update()
root.mainloop()
