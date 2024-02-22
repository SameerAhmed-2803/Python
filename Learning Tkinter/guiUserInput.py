#importing tkinter library
from tkinter import *
#creating root window
root = Tk()

#root window title and dimensions
root.title("Welcome to my first Python GUI")
#geometry = (width*height)
root.geometry('455x400')

#adds a label inside the gui box and uses grid to format it within it
label = Label(root, text="What do you think about the 1st GUI so far?")
label.grid()

#adding the user input through entry()
userTxt = Entry(root, width=10)
userTxt.grid(column=1, row=0)

#creating a function to see if a button is clicked, when clicked the button shows user input
def isClicked():
    clicked = "You wrote:"+ userTxt.get()
    label.configure(text= clicked)

#using the button widget from Tkinter to add a button with red text iside
button = Button(root, text="Click me", fg="red", command=isClicked)
#Setting the buttons place in grid
button.grid(column=2, row=0)



#executing Tkinter
root.mainloop()


