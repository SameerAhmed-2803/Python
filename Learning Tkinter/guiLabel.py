#importing tkinter library
from tkinter import *
#creating root window
root = Tk()

#root window title and dimensions
root.title("Welcome to my first Python GUI")
#geometry = (width*height)
root.geometry('350x300')

#adds a label inside the gui box and uses grid to format it within it
label = Label(root, text="The first label to the first gui")
label.grid()

#executing Tkinter
root.mainloop()


