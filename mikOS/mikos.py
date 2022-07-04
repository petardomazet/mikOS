'''
@pdmzt  &  @notjipp
Simple Python Operating System
mikOS
June 2022
'''

"""

~napomena za Jippa:

stavio sam (za probu) da kad se klikne Enter tipka na Entry-u za password, da se odma ide na System Info aplikaciju.
I primijetio sam da system information app triba malo duže da se učita pa sam stavio after(1000) da se istovremeno ugasi 
welcome zaslon i upali system information, jer bi u suprotnom se ugasio samo welcome zaslon i onda nakon nekog vrimena upalio
system information.


(ako si registrira šta sam napisa)

@pdmzt

"""
import sys
from tkinter import*
from time import strftime
import datetime as dt
import os
import psutil
import platform
import cpuinfo



window_dimensions = "1100x620"
os_name = "mikOS"
mikOS_version = "mikOS 1.0"

def welcome_screen():
    global welcomeScreen
    global loginScreenWallpaper
    global loginPersonIcon
    global notificationsIcon
    global enterIcon
    global wifiIcon
    global sleepIcon
    global speakerIcon
    global wallpaper

    welcomeScreen = Tk()
    welcomeScreen.title(os_name)
    welcomeScreen.geometry(window_dimensions)
    welcomeScreen.resizable(0,0)
    welcomeScreen.config(cursor="arrow")
    
    loginScreenWallpaper = PhotoImage(file="wallpaper.png")
    loginPersonIcon = PhotoImage(file="loginPersonIcon.png")
    notificationsIcon = PhotoImage(file="notifIcon.png")
    enterIcon = PhotoImage(file="enter.png")
    wifiIcon = PhotoImage(file="wifi.png")
    #sleepIcon = PhotoImage(file="sleep-icon.png")
    speakerIcon = PhotoImage(file="speaker-icon.png")
    wallpaper = PhotoImage(file="wallpaperBrBa.png")

    

welcome_screen()

def volume_mixer():
    volumeSlider = Label(welcomeScreen, bg="black", borderwidth=0)
    volumeSlider.place(x=800, y=24, height=76, width=300)
    vol = Scale(
    welcomeScreen,
    from_ = 0,
    to = 100,
    orient = HORIZONTAL,
    bg="white"
    )
    vol.place(x=800, y=49, width=300)
    speaker_device = "Realtek High Definition Audio"
    speaker_name = Label(welcomeScreen, text=speaker_device, font=("Arial", 10), fg="white", bg="black")
    speaker_name.place(x=802, y=23)

def system_information():       #System information app
    sysInf = Tk()
    sysInf.title(os_name)
    sysInf.geometry(window_dimensions) 
    sysInf.resizable(0,0)
    welcomeScreen.after(1000, lambda:welcomeScreen.destroy()) 
    
    # Computer Specs
    operatingSystem = mikOS_version
    processor = platform.processor()
    ramCapacity = psutil.virtual_memory().total #/ 1000000000
    RamDakako = ramCapacity / 1000000000
    processor1 = cpuinfo.get_cpu_info()['brand_raw']
    processorInfo = Label(sysInf, text=processor1, font=("Arial", 13), fg="#0C084D")
    processorInfo.config(bg="white")
    processorInfo.pack()

    sysInf.mainloop()


# Desktop !!! poslije dovršit

def desktop():
    global desktop
    desktop = Tk()
    desktop.title(os_name)
    desktop.geometry(window_dimensions)
    desktop.resizable(0,0)
    welcomeScreen.destroy()
    desktopWallpaper = Label(desktop, image=wallpaper)
    desktopWallpaper.place(x=-30,y=-2)
    desktop.mainloop()
    







def widgeti_na_welcome():
    global loginScreenWallpaperLabel
    loginScreenWallpaperLabel = Label(welcomeScreen, image=loginScreenWallpaper, borderwidth=0)      # wallpaper na login screen-u
    loginScreenWallpaperLabel.place(x=-65, y=0)

    bar = Label(welcomeScreen, text=(" " * 100000), fg="black", bg="black")  # crna traka na vrhu 
    bar.place(x=-1, y=-1, height=25)
    b = Label(welcomeScreen) # sat na vrhu welcome screen-a
    b.place(x=1037, y=3.8)

    def time():
        c = strftime('%H:%M')   # redoslijed pisanja vremena (sat:minuta)
        b.config(text=c,font=('DS-DIGITAL', 8), borderwidth=0, fg="white", bg="black")
        b.after(1000, time)

    time()

 
   
    entryPassword = Entry(welcomeScreen, show="•", font=("Arial", 11))        # polje za unos lozinke
    #entryPassword.place(x=437, y=348, width=200, height=22)
    entryPassword.place(x=467, y=367)
    passwButton = Button(welcomeScreen, image=enterIcon, borderwidth=0, command=system_information)
    passwButton.place(x=632, y=367)


    notifIconOnTop = Button(welcomeScreen, image=notificationsIcon, borderwidth=0, bg="black").place(x=1074, y=-1.6)     # button za notifikacije/obavijesti


    date = dt.datetime.now()
    date_label = Label(welcomeScreen, text=f"{date:%B %d, %Y}", font=("Arial", 8), fg="white", bg="black")
    date_label.place(x=959, y=1.5)

    wifi_icon = Button(welcomeScreen, image=wifiIcon, borderwidth=0, bg="black")
    wifi_icon.place(x=918, y=-7)

    speaker_icon = Button(welcomeScreen, image=speakerIcon, borderwidth=0, bg="black", command=lambda:[volume_mixer()])
    speaker_icon.place(x=890, y=-2)

    """
    def sleep_mode():
        
        returnToLoginScreen = Button(welcomeScreen, text=(""*4343), bg="black", fg="black", borderwidth=0, activebackground="black")
        returnToLoginScreen.place(x=0,y=0, width=4930, height=4343)   
        welcomeScreen.config(cursor="None")
        returnToLoginScreen.destroy()
    """
    #  - - - - -   Nadodati welcomeScreen.bind_all('<anykey>', dakako)

    def buttonSleep():
        def dakako():
            sleepMode.destroy()
            welcomeScreen.config(cursor="arrow")
        sleepMode = Button(welcomeScreen, text=(""*4323), fg="black", bg="black", activebackground="black", borderwidth=0, command=dakako)
        sleepMode.place(x=-1,y=-1, height=4430, width=4343)
        welcomeScreen.config(cursor="None")
    sleepBtn = Button(welcomeScreen, text="Spavaj", command=buttonSleep)
    sleepBtn.place(x=54, y=473)
    welcomeScreen.update()
    welcomeScreen.mainloop()

widgeti_na_welcome()



#Desktop

