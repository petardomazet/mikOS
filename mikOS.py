'''
@pdmzt
Simple Python Operating System
mikOS
June 2022

Project currently abandoned.
'''


from tkinter import*
from time import strftime
import datetime as dt
import psutil
import platform
import cpuinfo
import shutil

window_dimensions = "1100x620"
os_name = "mikOS"
mikOS_version = "1.0"
darkMode = "#252325"

password = open("password.txt", "r")        # default password ---> mikosadmin
password = password.readline()

def welcome_screen():
    global welcomeScreen
    global loginScreenWallpaper
    global loginPersonIcon
    global notificationsIcon
    global enterIcon
    global wifiIcon
    global sleepIcon
    global speakerIcon
    global wallpImage
    global wrong_password
    global correctPassword

    welcomeScreen = Tk()
    welcomeScreen.title(os_name)
    welcomeScreen.geometry(window_dimensions)
    welcomeScreen.resizable(0,0)
    welcomeScreen.config(cursor="arrow")
    windowImage = PhotoImage(file="iconphoto.png")
    welcomeScreen.iconphoto(False, windowImage)
    loginScreenWallpaper = PhotoImage(file="LockScreenWallpaper.png")
    loginPersonIcon = PhotoImage(file="loginPersonIcon.png")
    notificationsIcon = PhotoImage(file="NotificationsIcon.png")
    enterIcon = PhotoImage(file="EnterPassword.png")
    wifiIcon = PhotoImage(file="Wi-Fi_Icon.png")
    sleepIcon = PhotoImage(file="sleepMode_icon2.png")
    speakerIcon = PhotoImage(file="SpeakerIcon.png")
    wallpImage = PhotoImage(file="DesktopWallpaper.png")
    wrong_password = PhotoImage(file="wrong__password.png")
    correctPassword = PhotoImage(file="success_welcome.png")

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
 
def system_information(): 
    #System information app
    sysInf = Tk()
    sysInf.title(os_name)
    sysInf.geometry(window_dimensions) 
    sysInf.resizable(0,0)
    sysInf.config(bg=darkMode)
    welcomeScreen.after(1000, lambda:welcomeScreen.destroy()) 
    bar = Label(sysInf, text=(" " * 100000), fg="black", bg="black")  # crna traka na vrhu 
    bar.place(x=-1, y=-1, height=25)


    loginScreenWallpaper = PhotoImage(file="LockScreenWallpaper.png")
    loginPersonIcon = PhotoImage(file="loginPersonIcon.png")
    notificationsIcon = PhotoImage(file="NotificationsIcon.png")
    enterIcon = PhotoImage(file="EnterPassword.png")
    wifiIcon = PhotoImage(file="Wi-Fi_Icon.png")
    #sleepIcon = PhotoImage(file="sleep-icon.png")
    speakerIcon = PhotoImage(file="SpeakerIcon.png")
    
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
    totalDiskCapacity.place(x=45, y=232)

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
    
    hr4 = Label(sysInf, text=("_"*495), fg="grey", bg=darkMode, font=("Helvetica", 2)).place(x=45, y=365)
    
    passwordLabel = Label(sysInf, text="Privacy & Security", fg="#F6F6FA", font=("Segoe UI", 14, 'bold'), bg=darkMode)
    passwordLabel.place(x=45, y=372)
    
    def change_password():
        password = open("password.txt", "r")
        current_password = password.readline()
        password.close()
        entryOldLabel = Label(sysInf, text=("Enter old password: "), fg="#F6F6FA", font=("Segoe UI", 12), bg=darkMode)
        entryOldLabel.place(x=45,y=437)

        entryOldPassw = Entry(sysInf, bg="white", fg="black", font=("Helvetica"), show="•")
        entryOldPassw.place(x=205, y=443, width="200", height="18")

        entryNewLabel = Label(sysInf, text=("Enter new password: "), fg="#F6F6FA", font=("Segoe UI", 12), bg=darkMode)
        entryNewLabel.place(x=45,y=470)        
        
        entryNewPassw = Entry(sysInf, bg="white", fg="black", font=("Helvetica"), show="•")
        entryNewPassw.place(x=205, y=476, width="200", height="18")

        old_password = str(entryOldPassw.get())
        new_password = str(entryNewPassw.get())

        changePassword = Button(sysInf, text="Change Password", bg="#F6F6FA", fg=darkMode, command=change_password)
        changePassword.place(x=45, y=410)
        
    def defender():
        
        mikOS_DefenderApp = Button(sysInf, text="Check for Viruses", bg="#F6F6FA", fg=darkMode)
        mikOS_DefenderApp.place(x=45, y=485)

    sysInf.mainloop()

# Desktop !!! poslije dovršit

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
    
    def checkPassword():
        enteredPassword = str(entryPassword.get())
        if enteredPassword == password:
            loginScreenWallpaperLabel.config(image=correctPassword)
            welcomeScreen.update()
            system_information()

        else:
            loginScreenWallpaperLabel.config(image=wrong_password)
            entryPassword.delete(0, END)
            entryPassword.focus_set()

    passwButton = Button(welcomeScreen, image=enterIcon, borderwidth=0, command=checkPassword)
    passwButton.place(x=632, y=367)
    passwButton.focus_set()
    entryPassword.focus_set()

    notifIconOnTop = Button(welcomeScreen, image=notificationsIcon, borderwidth=0, bg="black").place(x=1074, y=-1.6)     # button za notifikacije/obavijesti

    date = dt.datetime.now()
    date_label = Label(welcomeScreen, text=f"{date:%B %d, %Y}", font=("Arial", 8), fg="white", bg="black")
    date_label.place(x=930, y=1.5)

    wifi_icon = Button(welcomeScreen, image=wifiIcon, borderwidth=0, bg="black")
    wifi_icon.place(x=897, y=-7)

    speaker_icon = Button(welcomeScreen, image=speakerIcon, borderwidth=0, bg="black", command=lambda:[volume_mixer()])
    speaker_icon.place(x=875, y=-2)

    def buttonSleep():
        def dakako(event):
            sleepMode.destroy()
            welcomeScreen.config(cursor="arrow")
        def dakako1():
            sleepMode.destroy()
            welcomeScreen.config(cursor="arrow")
        sleepMode = Button(welcomeScreen, text=(""*4323), fg="black", bg="black", activebackground="black", borderwidth=0, command=dakako)
        sleepMode.place(x=-1,y=-1, height=4430, width=4343)
        sleepMode2 = Button(welcomeScreen, text=(""*4323), fg="black", bg="black", activebackground="black", borderwidth=0, command=dakako1)
        sleepMode2.place(x=-1,y=-1, height=4430, width=4343)

        welcomeScreen.config(cursor="None")
        sleepMode.focus_set()
        sleepMode.bind('<Key>', dakako)

    sleepBtn = Button(welcomeScreen, image=sleepIcon, command=buttonSleep, borderwidth=0)
    sleepBtn.place(x=54, y=473, height=48, width=48)
    welcomeScreen.mainloop()

"""
def notepadApp():
    notepad = Tk()
    notepad.title(os_name)
    notepad.geometry(window_dimensions)

    notepad.mainloop()
"""


def video_call():
    videoCall = Tk()
    videoCall.title(os_name)
    videoCall.geometry(window_dimensions)
    videoCall.config(bg=darkMode)
    
    videoCall.mainloop()

widgeti_na_welcome()

