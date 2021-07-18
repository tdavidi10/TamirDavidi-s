#Readsy
import tkinter as tk

text = "hi eveyone i am tamir davidi and this is my fast reading helper application. you can read now much much faster than you used to."
text = text.split()
i = 0
def do_stuff():
    global i
    s = text[i]
    i = i + 1
    color = 'black'
    l.config(text=s, fg=color)
    root.after(170, do_stuff) # speed delay

root = tk.Tk()
root.wm_overrideredirect(True)
root.geometry("{0}x{1}+0+0".format(root.winfo_screenwidth(), root.winfo_screenheight()))
root.bind("<Button-1>", lambda evt: root.destroy())

l = tk.Label(text='', font=("Helvetica", 60)) # font and size
l.pack(expand=True)

do_stuff()
root.mainloop()
