import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo

root = tk.Tk()

root.geometry('400x500')
root.resizable(False, False)
root.title('Posture reminder')
#root.configure(bg="#e3e3cb")

root.columnconfigure(0, weight = 2)
root.rowconfigure(0, weight=2)
root.rowconfigure(1, weight=4)
root.rowconfigure(2, weight=1)
root.rowconfigure(3, weight=1)

label1 = tk.Label(root, text="Posture reminder is now active")
label1.grid(row = 0)

info_btn = tk.Button(root, text="How it works", command=lambda: how_it_works())
info_btn.grid(row = 2)

credits_btn = tk.Button(root, text="Credits", command=lambda: credits())
credits_btn.grid(row = 3)

def how_it_works():
    pass

def credits():
    pass

root.mainloop()