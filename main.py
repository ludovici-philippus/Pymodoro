from tkinter import *
from tkinter import messagebox
from time import sleep
from threading import Thread

class Pomodoro(object):
    def __init__(self):
        self.root = Tk()

        self.time = [25, 00]
        self.timeout = IntVar()
        self.timeout.set(25)

        self.lb_clock = Label(self.root, text=f"{self.time[0]}:{self.time[1]}", font=("arial", 48))
        self.lb_clock.grid(row=0, column=0)

        self.timer = Entry(self.root, textvariable=self.timeout)
        self.timer.grid(row=1, column=0)

        self.bt_start = Button(self.root, text="Start!", command=lambda: Thread(target=self.start_pomodoro).start())
        self.bt_start.grid(row=2, column=0)

        self.main()

    def update_clock(self):
        if self.time[0] == 0 and self.time[1] == 0:
            self.stop_pomodoro()
        else:
            if self.time[1] != 00:
                self.time[1] = self.time[1] - 1
            else:
                self.time[0] = self.time[0] - 1
                self.time[1] = 59
        self.lb_clock = Label(self.root, text=f"{self.time[0]}:{self.time[1]}", font=("arial", 48))
        self.lb_clock.grid(row=0, column=0)
    
    def start_pomodoro(self):
        self.time[0] = self.timeout.get()
        self.lb_clock.grid(row=0, column=0)
        while self.running:
            sleep(1)
            self.update_clock()
            self.root.update()

    def stop_pomodoro(self):
        self.running = False
        try:
            import winsound
            winsound.MessageBeep(winsound.MB_ICONEXCLAMATION)
        except ImportError:
            import os
            os.system('beep -f 440 -l 1')
        messagebox.showinfo(title="End", message="The Pomodoro got to the end, go take a break!")
        self.time[0] = 5
        self.timeout.set(5)
    
    def main(self):
        self.running = True
        self.root.title("Pomodoro App")
        self.root.geometry("165x150")
        self.root.resizable(0, 0)
        self.root.mainloop()


pomodoro = Pomodoro()
