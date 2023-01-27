import tkinter as tk
from tkinter.ttk import * 
#from tk import ttk



root = tk.Tk()

root.title("Snoog")

style = Style()

style.configure('W.TButton',font= ('Arial',15, 'bold'), foreground = 'red', padding = 0, background = 'black', width = 5, border = 0)

label = Label(root)
label['text'] = "hi, gello"

label.pack()

root.geometry("600x900+60+60")

root.resizable(False, False)

radio = Radiobutton(root, text="Radio")
radio.pack()

field = Entry(root ,name='field')
field.pack()


progress = Progressbar(root, name='progress', length=100, maximum=23)
progress.pack()


btn = Button(root, text="btn",style='W.TButton')
btn.pack()

root.mainloop()