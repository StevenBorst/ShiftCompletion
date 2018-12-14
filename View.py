# TODO: Find and add relevant imports
import os
import made.py
from tkinter import ttk
from tkinter import *
from PIL import Image, ImageTk
from sys import exit
from tkinter import messagebox


def client_exit():
    exit()

class View(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)

        self.master = master
        self.init_window()

    def init_window(self):

        # method which returns the user-input values
        def get_entry():
            return self.rate.get()

        # button call to navigate funtion (Should be modified to call Model.py's navigate
        def Start():
            None

        self.master.title("Shift Completion")

        self.pack(fill=BOTH, expand=1)

        # Start coordinates area
        Label(self, text="Hourly Rate").grid(row=1, column=1, columnspan=2)
        Label(self).grid(row=2, column=1)
        self.rate = Entry(self, width=10)

        #Stats
        money = Label(self, text="Money Made: $").grid(row=7, column=1, columnspan=2)
        complete = Label(self, text="Shift Completion: ").grid(row=7, column=3, columnspan=2)

        # Navigate button which will execute the program
        Button(self, text="  Start  ", command=navigate).grid(row=2, column=5, rowspan=2)
