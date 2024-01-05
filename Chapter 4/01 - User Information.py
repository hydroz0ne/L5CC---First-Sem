#Exercise 1 - User Information
from tkinter import *
root = Tk()
root.geometry("235x325")
root.title("User Information")

#Writes the txt file
def filecreate():
    name = nameentry.get()
    age = ageentry.get()
    hometown = hometownentry.get()

    with open("bio.txt", "w") as file:
        file.write("-----User Information-----")
        file.write(f"\nName: {name}\n")
        file.write(f"Age: {age}\n")
        file.write(f"Hometown: {hometown}")

#Reads the txt file
def fileread():
    try:
        with open("bio.txt", "r") as file:
            content = file.read()
            outputlabel.config(text=content)
    except FileNotFoundError:
        outputlabel.config(text="File not found.")

wlclabel = Label(root, text="User Information", font=(None, 14))
wlclabel.grid(row=0, column=0, columnspan=2, pady=20)

namelabel = Label(root, text="Name:")
agelabel = Label(root, text="Age:")
hometownlabel = Label(root, text="Hometown:")
namelabel.grid(row=1, column=0, padx=10)
agelabel.grid(row=2, column=0, padx=10)
hometownlabel.grid(row=3, column=0, padx=10)

namevalue = StringVar()
agevalue = IntVar()
hometownvalue = StringVar()

#Input Areas
nameentry = Entry(root, textvariable=namevalue)
ageentry = Entry(root, textvariable=agevalue)
hometownentry = Entry(root, textvariable=hometownvalue)
nameentry.grid(row=1, column=1, padx=10)
ageentry.grid(row=2, column=1, padx=10)
hometownentry.grid(row=3, column=1, padx=10)

#Buttons
createbutton = Button(root, text="Create File", command=filecreate)
createbutton.grid(row=4, column=0, columnspan=2, pady=10)
readbutton = Button(root, text="Read File", command=fileread)
readbutton.grid(row=5, column=0, columnspan=2)

#Prints the user's inputs from the file
outputlabel = Label(root, text="")
outputlabel.grid(row=6, column=0, columnspan=2, pady=20)

#Configures grid rows and columns for proper layout
root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=1)
root.rowconfigure(0, weight=1)
root.rowconfigure(6, weight=1)

root.mainloop()