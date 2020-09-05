from tkinter import *

root = Tk()

# App screen size = weight x height
root.geometry("800x515")
root.title("This is my first GUI using Python")

# width, height
# root.minsize(800,515)
# root.maxsize(800,515)


photo = PhotoImage(file="welcome_splash_fb.png") # GUI Background photo
text_label = Label(text = "This is my first GUI using Python", borderwidth=3, relief=SUNKEN)
photo_label = Label(image = photo) #GUI Label

#To use JPG photo:
# from PIL import Image, ImageTk
# image = Image.open("1.jpg")
# photo = ImageTk.PhotoImage(image)

text_label.pack(pady=10, fill="x")
photo_label.pack(padx=34, pady=34, fill="x")

# GUI logic her

root.mainloop()