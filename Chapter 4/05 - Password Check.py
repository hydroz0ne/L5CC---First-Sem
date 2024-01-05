#Exercise 5 - Password Check
from tkinter import *
root = Tk()
root.geometry("500x300")
root.resizable(False, False)
root.title("Password Test")

#Checks if the password meets the requirements
def validpass(password):
    return (
        6 <= len(password) <= 12 and
        any(char.islower() for char in password) and
        any(char.isupper() for char in password) and
        any(char.isdigit() for char in password) and
        any(char in '$#@' for char in password)
    )

#Initial number of attempts
attempts = [5]

#Handles the password button and checks the password
def passcheck():
    password = passentry.get()
    while attempts[0] > 0:
        if validpass(password):
            #Displays a success message if the password is valid
            statuspass.config(text="Password is valid!", fg="green")
            checkbutton.config(state=DISABLED)
            break
        else:
            #Decreases the number of attempts and display appropriate messages
            attempts[0] -= 1
            if attempts[0] > 0:
                statuspass.config(text=f"Invalid password, you have {attempts[0]} attempts remaining.", fg="red")
                break
            else:
                statuspass.config(text="You have exceeded the maximum number of attempts. The authorities have been alerted!", fg="red")
                break

#List of password requirements
passrequirements = [
    "Requirements:",
    "Contain at least 1 uppercase & lowercase letter between A and Z.",
    "Contain at least 1 number between 0 and 9.",
    "Contain at least 1 character from $, #, @.",
    "Minimum length of password: 6",
    "Maximum length of password: 12"
]

wlclabel = Label(root, text="Password Checker", font=(None, 14))
requirementlabel = Label(root, text="\n".join(passrequirements))
passlabel = Label(root, text="Enter Password:")
passentry = Entry(root, show="*")
checkbutton = Button(root, text="Check Password", command=passcheck)
statuspass = Label(root, text="", fg="green")

wlclabel.pack(pady=15)
requirementlabel.pack(pady=10)
passlabel.pack()
passentry.pack()
checkbutton.pack(pady=10)
statuspass.pack()

root.mainloop()