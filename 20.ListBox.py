from tkinter import *

def add():
    global i
    lbx.insert(ACTIVE, f"{i}")
    i+=1

i = 0
root = Tk()
root.geometry("455x233")
root.title("Listbox tutorial")

lbx = Listbox(root)
lbx.pack()
lbx.insert(END, "First item of our listbox")

Button(root, text="Add Item", command=add).pack()

root.mainloop()