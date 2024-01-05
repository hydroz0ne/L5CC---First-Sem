#Exercise 3 - Login Page
from tkinter import *
root = Tk()
root.title("Login")
root.geometry("225x200")
root.resizable(False, False)

#Create labels and set their properties
form = Label(root, text="Login", font="comicsans 13 bold", pady=15)
user = Label(root, text="Username")
password = Label(root, text="Password")

#Grid placement of labels
user.grid(row=2, column=2)
password.grid(row=3, column=2)

#Create StringVar instances to store input values
uservalue = StringVar()
passvalue = StringVar()

#Create entry widgets and link them to StringVar instances
userentry = Entry(root, textvariable=uservalue)
passentry = Entry(root, textvariable=passvalue, show="*")

#Grid placement of entry widgets
form.grid(row=1, column=3, padx=10, pady=5)
userentry.grid(row=2, column=3, padx=10, pady=5)
passentry.grid(row=3, column=3, padx=10, pady=5)

#Function to show user's input values
def login():
    print("You have successfully logged in.")
    print(f"Your username is {uservalue.get()}.")
    print(f"Your password is {passvalue.get()}.")

#Create a button and link it to the login function
button = Button(root, text="Login", command=login)
button.grid(row=4, column=3, padx=10, pady=10)

root.mainloop()