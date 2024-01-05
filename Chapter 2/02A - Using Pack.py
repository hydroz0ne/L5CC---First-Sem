#Exercise 2A - Using Pack 
from tkinter import *
root = Tk()
root.title("Managing Layout")
root.configure(bg="LightGray")

#Create Label widgets with specified attributes
l1 = Label(root, bg="Red", padx=30, pady=5, relief=SUNKEN, text="A")
l2 = Label(root, bg="Yellow", padx=30, pady=5, relief=SUNKEN, text="B")
l3 = Label(root, bg="Blue", padx=30, pady=5, text="C")
l4 = Label(root, bg="White", padx=30, pady=5, text="D")

#Pack and configure all labels 
l1.pack(side=TOP, fill=X, expand=TRUE)
l2.pack(side=BOTTOM, fill=NONE)
l3.pack(side=LEFT, expand=TRUE)
l4.pack(fill=NONE)

root.mainloop()