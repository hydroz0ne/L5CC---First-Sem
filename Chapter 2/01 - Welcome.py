#Exercise 1 - Welcome
from tkinter import *
root = Tk()
root.title("Welcome Message")
root.geometry("400x200") #Sets the dimensions of the window (width x height)
root.resizable(False, False) #Disables window resizing
root.configure(bg='LightGreen') #Sets the background color of the window

#Create a Label widget to display the welcome message
wlclabel = Label(root, text="Welcome to TKinter GUI!", font = 'Helvetica 14 bold')
wlclabel.pack(pady=20)

root.mainloop()