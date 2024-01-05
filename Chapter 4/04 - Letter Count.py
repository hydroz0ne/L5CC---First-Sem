#Exercise 4 - Letter Count
from tkinter import *
root = Tk()
root.geometry("500x200")
root.title("Letter Count")

#Counts the occurrences of a character in a file
def wholefile(char):
    try:
        #Reads the content of the file
        with open("sentences.txt", 'r') as file:
            text = file.read()
            #Counts the occurrences of the specified character
            lettercount = text.count(char)
            return lettercount
    except FileNotFoundError:
        return None

#Handles the button click and display character occurrences
def occurences():
    #Gets the character entered in the entry widget
    char = charentry.get()
    #Calls the wholefile function to get the count
    countresult = wholefile(char)
    
    if countresult is not None:
        #Displays the result in the label widget
        result.config(text=f"The character '{char}' has appeared {countresult} times.")
    else:
        result.config(text="File not found.")

wlclabel = Label(root, text="String Counter", font=(None, 14))
charlabel = Label(root, text="Enter a character:")
charentry = Entry(root)
findbutton = Button(root, text="Find Occurrences", command=occurences)
result = Label(root, text="")

wlclabel.grid(row=1, column=1, pady=5)
charlabel.grid(row=2, column=0, padx=10, pady=5)
charentry.grid(row=2, column=1, padx=10, pady=5)
findbutton.grid(row=3, column=1, pady=10)
result.grid(row=4, column=1, pady=5)

#Configures grid rows and columns for proper layout
root.grid_rowconfigure(0, weight=1)
root.grid_rowconfigure(4, weight=1)
root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(2, weight=1)

root.mainloop()