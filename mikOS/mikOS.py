'''
@pdmzt  &  @NotJipp
Simple Python Operating System
mikOS
June 2022 // šta nije July? xd
'''

"""

n/a

@NotJipp

"""

import os
import sys
import psutil
import shutil
import cpuinfo
import platform
import datetime as dt
from tkinter import *
from time import strftime
from concurrent.futures import process

window_dimensions = "1100x620"
os_name           = "mikOS"
mikOS_version     = "mikOS 1.0"
darkMode          = "#252325"

def welcome_screen():
    global wifiIcon
    global enterIcon
    global wallpaper
    global sleepIcon
    global speakerIcon
    global welcomeScreen
    global loginPersonIcon
    global notificationsIcon
    global loginScreenWallpaper
    
    welcomeScreen = Tk()
    welcomeScreen.title(os_name)
    welcomeScreen.geometry(window_dimensions)
    welcomeScreen.resizable(0,0)
    welcomeScreen.config(cursor="arrow")

    wifiIcon             = PhotoImage(file="pictures/wifiIcon.png")
    wallpaper            = PhotoImage(file="pictures/wallpaperOption1.png")
    enterIcon            = PhotoImage(file="pictures/enterIcon.png")
    speakerIcon          = PhotoImage(file="pictures/speakerIcon.png")
    loginPersonIcon      = PhotoImage(file="pictures/loginPersonIcon.png")
    notificationsIcon    = PhotoImage(file="pictures/notificationIcon.png")
    loginScreenWallpaper = PhotoImage(file="pictures/wallpaperLogin.png")
    #sleepIcon           = PhotoImage(file="sleepIcon.png") --- vidim ne postoji u folderu, preporučam mjesec mali kao iconu

welcome_screen()

def time():
    global c
    global b
    c = strftime('%H:%M')   # redoslijed pisanja vremena (sat:minuta)
    b.config(text=c,font=('DS-DIGITAL', 8), borderwidth=0, fg="white", bg="black")
    b.after(1000, time)


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
    sysInf.config(bg=darkMode)
    welcomeScreen.after(1000, lambda:welcomeScreen.destroy()) 
    bar = Label(sysInf, text=(" " * 100000), fg="black", bg="black")  # crna traka na vrhu 
    bar.place(x=-1, y=-1, height=25)


    wifiIcon             = PhotoImage(file="pictures/wifiIcon.png")
    wallpaper            = PhotoImage(file="pictures/wallpaperOption1.png")
    enterIcon            = PhotoImage(file="pictures/enterIcon.png")
    speakerIcon          = PhotoImage(file="pictures/speakerIcon.png")
    loginPersonIcon      = PhotoImage(file="pictures/loginPersonIcon.png")
    notificationsIcon    = PhotoImage(file="pictures/notificationIcon.png")
    loginScreenWallpaper = PhotoImage(file="pictures/wallpaperLogin.png")
    #sleepIcon           = PhotoImage(file="sleepIcon.png") --- vidim ne postoji u folderu, preporučam mjesec mali kao iconu
    
    # Computer Specs:
    release = mikOS_version
    processor = platform.processor()
    ramCapacity = psutil.virtual_memory().total #/ 1000000000
    ramCapacity = ramCapacity / 1000000000
    RamCapacityy = round(ramCapacity)
    RamCapacityRounded = (round(RamCapacityy))
    RamCapacityRounded = str(RamCapacityRounded)
    processor1 = cpuinfo.get_cpu_info()['brand_raw']
    total, used, free = shutil.disk_usage("/")
    ComputerName = platform.uname()
    ComputerName = ComputerName.node

    total = int()
    used  = int()
    free  = int()
    for disk in psutil.disk_partitions():
        if disk.fstype:
            total += int(psutil.disk_usage(disk.mountpoint).total)
            used  += int(psutil.disk_usage(disk.mountpoint).used)
            free  += int(psutil.disk_usage(disk.mountpoint).free)

    totalDiskSpace = round(total / (1024.0 ** 3))
    
    totalDiskSpaceString = str(totalDiskSpace)

    usedDiskSpace = round(used / (1024.0 ** 3))
    usedDiskSpaceString = str(usedDiskSpace)

    freeDiskSpace = (round(free / (1024.0 ** 3)))
    freeDiskSpaceString = str(freeDiskSpace)

    # --- labels ---        
    SystemInformationLabel = Label(sysInf, text="System Information Overview", fg="#F6F6FA", font=("Segoe UI", 22), bg=darkMode)
    SystemInformationLabel.place(x=45, y=27.5)
    hr1 = Label(sysInf, text=("_"*495), fg="grey", bg=darkMode, font=("Helvetica", 2)).place(x=45, y=75)

    mikOSVersion = Label(sysInf, text="mikOS", fg="#F6F6FA", font=("Franklin Gothic Medium", 18), bg=darkMode)
    mikOSVersion.place(x=45, y=93)
    
    r_elease = Label(sysInf, text=(release), fg="#F6F6FA", font=("Segoe UI", 16), bg=darkMode)
    r_elease.place(x=117.5, y=91.5)
    
    copyrightLabel = Label(sysInf, text="© 2022 MiK Corporation. All rights reserved.", fg="#F6F6FA", font=("Segoe UI", 12), bg=darkMode)
    copyrightLabel.place(x=45, y=125)
    
    hr2 = Label(sysInf, text=("_"*495), fg="grey", bg=darkMode, font=("Helvetica", 2)).place(x=45, y=150)


    hardwareLabel = Label(sysInf, text="Hardware", fg="#F6F6FA", font=("Segoe UI", 14, 'bold'), bg=darkMode)
    hardwareLabel.place(x=45, y=157)

    processorLabel = Label(sysInf, text=("Processor: " + processor1), fg="#F6F6FA", font=("Segoe UI", 12), bg=darkMode)
    processorLabel.place(x=45, y=189)

    InstalledMemoryRAM = Label(sysInf, text=("Installed Memory (RAM): " + RamCapacityRounded + ",00" + " GB"), fg="#F6F6FA", font=("Segoe UI", 12), bg=darkMode)
    InstalledMemoryRAM.place(x=45, y=210)

    totalDiskCapacity = Label(sysInf, text=("Total Disk Capacity: " + totalDiskSpaceString + " GB"), fg="#F6F6FA", font=("Segoe UI", 12), bg=darkMode)
    totalDiskCapacity.place(x=45, y=231)

    usedDiskCapacity = Label(sysInf, text=("Used Disk Capacity: " + usedDiskSpaceString + " GB"), fg="#F6F6FA", font=("Segoe UI", 12), bg=darkMode)
    usedDiskCapacity.place(x=45, y=252)

    freeDiskCapacity = Label(sysInf, text=("Free Disk Capacity: " + freeDiskSpaceString + " GB"), fg="#F6F6FA", font=("Segoe UI", 12), bg=darkMode)
    freeDiskCapacity.place(x=45, y=273)

    hr3 = Label(sysInf, text=("_"*495), fg="grey", bg=darkMode, font=("Helvetica", 2)).place(x=45, y=298)

    nameAndOther = Label(sysInf, text="Computer Name And Other Details", fg="#F6F6FA", font=("Segoe UI", 14, 'bold'), bg=darkMode)
    nameAndOther.place(x=45, y=305)

    computer_name = Label(sysInf, text=("Computer Name: " + str(ComputerName)), fg="#F6F6FA", font=("Segoe UI", 12), bg=darkMode)
    computer_name.place(x=45, y=337)

    exitSysInfo = Button(sysInf, text="X", bg="red", borderwidth=0, fg="white", command=welcome_screen) #popraviti command
    exitSysInfo.place(x=1050, y=26, height=23, width=40)

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
    global notifIconOnTop
    global bar
    global b
    global loginScreenWallpaperLabel
    global date
    global date_label
    global wifi_icon
    global speaker_icon
    loginScreenWallpaperLabel = Label(welcomeScreen, image=loginScreenWallpaper, borderwidth=0)      # wallpaper na login screen-u
    loginScreenWallpaperLabel.place(x=-65, y=0)

    bar = Label(welcomeScreen, text=(" " * 100000), fg="black", bg="black")  # crna traka na vrhu 
    bar.place(x=-1, y=-1, height=25)
    b = Label(welcomeScreen) # sat na vrhu welcome screen-a
    b.place(x=1037, y=3.8)

    def time():
        global c
        global b
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

    def buttonSleep():
        def dakako():
            sleepMode.destroy()
            welcomeScreen.config(cursor="arrow")
        sleepMode = Button(welcomeScreen, text=(""*4323), fg="black", bg="black", activebackground="black", borderwidth=0, command=dakako)
        sleepMode.place(x=-1,y=-1, height=4430, width=4343)
        welcomeScreen.config(cursor="None")
    sleepBtn = Button(welcomeScreen, text="Spavaj", command=buttonSleep)
    sleepBtn.place(x=54, y=473)
    welcomeScreen.mainloop()

widgeti_na_welcome()
