from tkinter import*
from tkinter.ttk import Progressbar
import re

"""
Popraviti ovo sranje sa ce funkcijom

Maknuti entryCOmmands height i width i lipo podesit da je sve u jednoj liniji
"""

windowBarColor    = "#302D2D"

terminalApp = Tk()
terminalApp.title("mikOS")
terminalApp.resizable(0,0)
terminalApp.geometry("1100x620")
terminalApp.config(bg="black")
terminalApp.config(cursor='left_ptr')

    
bar = Label(terminalApp, text=(" " * 100000), fg=windowBarColor, bg=windowBarColor)  # crna traka na vrhu 
bar.place(x=-1, y=-1, height=25)
def exit():
        terminalApp.destroy()

exitTerminal = Button(terminalApp, text="✕", bg="red", borderwidth=0, fg="white", command=exit) #popraviti command
exitTerminal.place(x=1060, y=0, height=24, width=40)

def dakako():
    def newCommand(event):
        def blackBg():
            blkBg = Label(terminalApp, bg="black", fg="black", borderwidth=0, text=('                                                                                                                                                                                                                                                                                                                                                                                                                       \n'*194))
            blkBg.place(x=1, y=50)

        usersCommand = str(entryCommands.get())
        heck = "sudo heck"

        if heck in usersCommand:
            blackBg()

         
            def jebiSebe(event):
                YNanswer = str(AreYouSure.get())


                def ifAnswerIsY():
                    HeckProgress = Progressbar(terminalApp, orient='horizontal', mode='determinate', length=450)
                    HeckProgress.place(x=1, y=100) 
                    HeckProgress.start()
                    terminalApp.after(9000, HeckProgress.destroy())

                
                YNanswer = str(AreYouSure.get())

                if YNanswer == "y":
                    ifAnswerIsY()
                    
                elif YNanswer == "n":
                    HeckingInterrupted = Label(terminalApp, font=("Terminal", 10), bg="black", fg="white", borderwidth=0, text=('Hecking interrupted.'))
                    HeckingInterrupted.place(x=1, y=140)

                else:
                    pass #- vamo ćem nešto stait
    
            pathKao1 = Label(terminalApp, font=("Terminal", 10), bg="black", fg="white", borderwidth=0, text=('Are you sure you want to heck (netko)? (y / n)'))
            pathKao1.place(x=1, y=60)
            AreYouSure = Entry(terminalApp, font=("Terminal", 10), bg="black", fg="white", borderwidth=0)
            AreYouSure.place(x=315,y=60, width=1100, height=15)
            AreYouSure.bind("<Return>", jebiSebe)
            AreYouSure.focus_set()
            




        elif usersCommand == "cls":
            blackBg()
            entryCommands.delete(0, END)

        else:
            blackBg()
            def delete(event):
                blackBg()
                entryCommands.delete(0, END)
                entryCommands.focus_set()

            diskutabilnaKomanda = Label(terminalApp, text=(str(usersCommand) + ": " + "command not found."),
            font=("Terminal", 10), bg="black", fg="white", borderwidth=0)
            diskutabilnaKomanda.place(x=1,y=50)
            deleteCommandWithEnter = Button(terminalApp, bg="black", borderwidth=0, command=delete)
            deleteCommandWithEnter.place(x=1000, y=1000)
            deleteCommandWithEnter.focus_set()
            deleteCommandWithEnter.bind("<Return>", delete)

    pathKao = Label(terminalApp, font=("Terminal", 10), bg="black", fg="white", borderwidth=0, text=('user@mikOS>  '))
    pathKao.place(x=1, y=35)
    entryCommands = Entry(terminalApp, font=("Terminal", 10), bg="black", fg="white", borderwidth=0)
    entryCommands.place(x=95,y=35, width=1100, height=15)
    entryCommands.bind("<Return>", newCommand)
    entryCommands.focus_set()

dakako()


terminalApp.mainloop()