#Exercise 1 - Greeting App
from tkinter import *
root = Tk()
root.geometry("400x270")
root.title("Greeting App")

#Frame for user input with a light blue background
inputframe = Frame(root, bg="LightBlue", padx=10, pady=15)
title = Label(inputframe, text="Personalized Greeting", bg="LightBlue", font="15")
name = Label(inputframe, text="Your Name:", bg="LightBlue")
nameinput = Entry(inputframe)

#Packs labels and entry widgets in the input frame
inputframe.pack(padx=10, pady=10)
title.pack()
name.pack()
nameinput.pack()

#Variable to store the selected color and set its default value to "Black"
colorvar = StringVar()
colorvar.set("Black")

#Labels and option menu for color selection
colorlabel = Label(inputframe, text="Select Color:", bg="LightBlue")
colormenu = OptionMenu(inputframe, colorvar, "Red", "Orange", "Green", "Blue", "Violet", "Black")
colorlabel.pack()
colormenu.pack()

#Function to update the greeting message based on the user's input
def greetingupdate():
    username = nameinput.get()
    pickedcolor = colorvar.get()
    greeting.config(text=f"Hello {username}, welcome to the TKinter program.", fg=pickedcolor)

#Create a button to trigger the greeting update
updatebutton = Button(inputframe, text="Update Greeting", command=greetingupdate)
updatebutton.pack()

#Create a frame for displaying the greeting message
displayframe = Frame(root, padx=10, pady=10)

#Create a label for displaying the greeting message with a light green background
greeting = Label(displayframe, text="", font="Arial 12", bg="LightGreen")

#Packs the display frame and greeting label
displayframe.pack()
greeting.pack()

root.mainloop()