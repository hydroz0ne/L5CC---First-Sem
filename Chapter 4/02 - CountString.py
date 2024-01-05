#Exercise 2 - CountString
from tkinter import *
root = Tk()
root.geometry("500x300")
root.resizable(False, False)
root.title("String Counter")

#Function to count occurrences of strings in a file
def allstrings(file, allstrings):
    try:
        #Read the content of the file and convert to lowercase for case-insensitive matching
        with open(file, 'r') as file:
            text = file.read().lower()
            #Use a dictionary comprehension to count occurrences of each string
            counts = {stringsearch: text.count(stringsearch.lower()) for stringsearch in allstrings}
        return counts
    except FileNotFoundError:
        return None

#Function to handle the button click and display string counts
def stringcount():
    file = "sentences.txt"
    #List of strings to search for in the file
    strsearchitem = [
        "Hello my name is Peter Parker",
        "I love Python Programming",
        "Love",
        "Enemy"
    ]

    #Call the allstrings function to get the counts
    counts = allstrings(file, strsearchitem)
    if counts is not None:
        #Clear the previous results in the Text widget
        result.delete("1.0", END)
        #Display the counts for each string in the Text widget
        for stringsearch, count in counts.items():
            result.insert(END, f"'{stringsearch}': Appeared {count} times.\n")

wlclabel = Label(root, text="String Counter", font=(None, 14))
result = Text(root, height=4, width=50)
findbutton = Button(root, text="Find String Count", command=stringcount)

wlclabel.grid(row=0, column=1, pady=5)
result.grid(row=1, column=1)
findbutton.grid(row=2, column=1, pady=20)

#Configures grid rows and columns for proper layout
root.grid_rowconfigure(0, weight=1)
root.grid_rowconfigure(2, weight=1)
root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(2, weight=1)

root.mainloop()