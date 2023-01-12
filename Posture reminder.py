import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo
import random
from PIL import ImageTk, Image

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
root.rowconfigure(4, weight=1)

label1 = tk.Label(root, text="Posture reminder is now active")
label1.grid(row = 0)

time_interv = tk.IntVar()
time_interval = ttk.Combobox(root, textvariable = time_interv)
time_interval['values'] = (15, 20, 30, 45, 60)
# Setting first option as default:
time_interval.current(0)
time_interval['state'] = 'readonly'
time_interval.grid(row = 2)


'''
info_btn = tk.Button(root, text="How it works", command=lambda: how_it_works())
info_btn.grid(row = 3)

credits_btn = tk.Button(root, text="Credits", command=lambda: credits())
credits_btn.grid(row = 4)
'''

class Reminder(object):
    
    current_image = 0
    image_list = ["posture awareness 1", "posture awareness 2", "posture awareness 3", "posture awareness 4"]
    random.shuffle(image_list)
    
    def __init__(self, show_interval=3, hide_interval=6): #30
        self.hide_int = hide_interval
        self.show_int = show_interval
        self.root = tk.Tk()
        self.root.geometry('400x500')
        self.root.resizable(False, False)
        self.root.title('Reminder')
        #tk.Frame(self.root, width=250, height=100).pack()
        
        image = Image.open(Reminder.image_list[Reminder.current_image] + ".png")
        img = image.resize((250, 250), Image.ANTIALIAS)
        img = ImageTk.PhotoImage(img, master = self.root)
        self.label = tk.Label(self.root, image=img)
        self.label.grid(row=0, column=0)
        self.root.after_idle(self.show)
        self.root.mainloop()
        
    def next_image(self):
        Reminder.current_image += 1
        if Reminder.current_image == len(Reminder.image_list):
            Reminder.current_image = 0
        image = Image.open(Reminder.image_list[Reminder.current_image] + ".png")
        img = image.resize((250, 250), Image.ANTIALIAS)
        img = ImageTk.PhotoImage(img, master = self.root)
        self.label.configure(image= img)
        self.label.image = img
        
    def hide(self):
        self.root.withdraw() 
        self.root.after(1000 * self.hide_int, self.show)

    def show(self):
        self.next_image()
        self.root.deiconify()
        self.root.after(1000 * self.show_int, self.hide)
        
    def set_show(self, event):
        pass
        # updated = event.widget.get()
        # self.show_int = int(updated)
        # print(self.show_int)
        
    # combobox selection change
    # time_interval.bind("<<ComboboxSelected>>", set_show)


r = Reminder()


def how_it_works():
    pass

def credits():
    pass


root.mainloop()

