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
    
    current_title = 0
    title_list = ["This is how correct posture looks like", "Is this the way you are sitting right now?", "Avoid hyper-arched lower back", "Hold the phone at eye level"]
    
    current_description = 0
    description_list = ["Keep your ears, shoulders and hips aligned. Check that your head is not protruding forward. According to the research, for every inch your head moves forward, there is an extra 10 pounds of weight placed on your neck. Also, to sit correctly, Keep your hips and knees at 90 degrees."\
                        ,"Posture presented on the image is incorrect. Sitting with excessive upper back curve can lead to hyperkyphosis (spine deformity). You need to be aware about your posture and sit straight. Keep your ears, shoulders and hips aligned. If you spend a lot of time in front of the computer, you should use an ergonomically designed chair."\
                        ,"You should avoid to overly arch your lower back as you straighten up. Lower back should have a small curve, which is called lordosis. Sitting with excessive low back arch often leads to hyperlordosis, also called anterior pelvis tilt. This spinal deformity is usually incurable. To provide support to the lower back, you can use small pillow or ergonomically designed chair."\
                        ,"Neck has to be straight while using phone. Be aware of your posture when using smartphone. The further your head and neck is extended forward and focused downward, the more your head will weigh, which can lead to neck and spine deformities. The higher you hold your phone, the less you slouch."]
    
    def __init__(self, show_interval=3, hide_interval=6): #30
        self.hide_int = hide_interval
        self.show_int = show_interval
        self.root = tk.Tk()
        self.root.geometry('400x500')
        self.root.resizable(False, False)
        self.root.title('Reminder')
        self.root.columnconfigure(0, weight = 2)
        #tk.Frame(self.root, width=250, height=100).pack()
        
        self.label1 = tk.Label(self.root, text = Reminder.title_list[Reminder.current_title])
        self.label1.grid(row=0, column=0, columnspan = 2)
        
        image = Image.open(Reminder.image_list[Reminder.current_image] + ".png")
        img = image.resize((250, 250), Image.ANTIALIAS)
        img = ImageTk.PhotoImage(img, master = self.root)
        self.label2 = tk.Label(self.root, image = img)
        self.label2.grid(row=1, column=0, columnspan = 2)
        
        self.label3 = tk.Label(self.root, text = Reminder.description_list[Reminder.current_description])
        self.label3.grid(row=2, column=0, columnspan = 2)
        
        self.root.after_idle(self.show)
        self.root.mainloop()
        
    def next_image(self):
        Reminder.current_image += 1
        Reminder.current_title += 1
        Reminder.current_description += 1
        if Reminder.current_image == len(Reminder.image_list):
            Reminder.current_image = 0
            Reminder.current_title = 0
            Reminder.current_description = 0
        image = Image.open(Reminder.image_list[Reminder.current_image] + ".png")
        img = image.resize((250, 250), Image.ANTIALIAS)
        img = ImageTk.PhotoImage(img, master = self.root)
        self.label1.configure(text = Reminder.title_list[Reminder.current_title])
        self.label2.configure(image= img)
        self.label2.image = img
        self.label3.configure(text = Reminder.description_list[Reminder.current_description])
        
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

