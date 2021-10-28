from tkinter import *

root = Tk()
#width x Height
root.geometry('300x500')
root.minsize(100,200)
root.maxsize(500,800)

# dumpy = Label(text="Dumpy is a goodboy in GUI")
# dumpy.pack()

photo = PhotoImage(file="new.jpg")
label =Label(image=photo)
label.pack()
root.mainloop()