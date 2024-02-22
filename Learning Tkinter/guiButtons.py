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

#creating a function to see if a button is clicked, when clicked displays text
def isClicked():
    label.configure(text="I got clicked")

#using the button widget from Tkinter to add a button with red text iside
button = Button(root, text="Click me", fg="red", command=isClicked)
#Setting the buttons place in grid
button.grid(column=1, row=0)

#executing Tkinter
root.mainloop()


